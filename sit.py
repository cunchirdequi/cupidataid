import requests

def handle_response(response):
    # Check if the response status code indicates success (200 OK)
    if response.status_code == 200:
        print("Snowball #1: ", response.text)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

try:
    # Attempt to make the HTTP GET request
    snowball_prompt_response_1 = requests.get('https://api.example.com/data')
    handle_response(snowball_prompt_response_1)
except requests.RequestException as e:
    print(f"An error occurred: {e}")
