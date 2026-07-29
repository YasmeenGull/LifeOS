import requests
import time

URL = "http://127.0.0.1:8000/score"

TOTAL_REQUESTS = 50

start = time.time()

for _ in range(TOTAL_REQUESTS):

    response = requests.get(URL)

    if response.status_code != 200:
        print("Request Failed")

end = time.time()

print(f"Completed {TOTAL_REQUESTS} requests")
print(f"Total Time: {round(end-start,2)} seconds")