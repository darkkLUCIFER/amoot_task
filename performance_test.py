import concurrent.futures
import random
import time

import requests
import json

# URL of the web service
URL = 'http://localhost:8000/api/v1/doctors/create-ticket/'


def generate_random_patient_id():
    # Generate a random integer for patient_id
    return random.randint(1, 1000)


# Function to send a single request
def send_request():
    # Generate a random patient_id
    patient_id = generate_random_patient_id()

    # Prepare the payload with the random patient_id
    payload = {
        'patient_id': patient_id
    }
    start_time = time.time()

    result = {'patient_id': patient_id, 'status_code': None, 'time': None}

    try:
        response = requests.post(URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        result['status_code'] = response.status_code
        result['time'] = elapsed_time
        result['response'] = response.text
    except Exception as e:
        result['status_code'] = None
        result['response'] = f"Request failed: {e}"
        result['time'] = time.time() - start_time

    return result


def main():
    num_requests = 100
    response_times = []
    errors = 0

    # Record the start time for the total elapsed time
    total_start_time = time.time()

    # Using ThreadPoolExecutor to send requests concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result['status_code'] != 200:
                errors += 1
            response_times.append(result['time'])
            print(
                f"Patient ID: {result['patient_id']} - Status Code: {result['status_code']}, Response: {result['response']}, Time: {result['time']:.2f}s")

        # Wait for all futures to complete
        concurrent.futures.wait(futures)

    # Calculate the total elapsed time
    total_elapsed_time = time.time() - total_start_time

    avg_response_time = sum(response_times) / len(response_times)
    error_rate = errors / num_requests * 100

    print(f"Average Response Time: {avg_response_time:.2f}s")
    print(f"Error Rate: {error_rate:.2f}%")
    print(f"Total Elapsed Time: {total_elapsed_time:.2f}s")


if __name__ == '__main__':
    main()
