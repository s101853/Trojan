import subprocess

def firewall_info():
    try:
        # Command to check firewall status on Windows
        command = "netsh advfirewall show allprofiles"

        # Run the command and capture its output
        output = subprocess.check_output(command, shell=True, universal_newlines=True)

        return output
    except Exception as e:
        return f"Failed to retrieve firewall status: {str(e)}"
