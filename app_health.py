import requests
import time
from datetime import datetime

# URL to monitor
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Function to log messages
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_msg = f"{timestamp} - {message}"
    print(final_msg)

# Function to check application health
def check_app():
    try:
        response = requests.get(URL, timeout=5)

        if response.status_code == 200:
            log(f"APP UP - Status Code: {response.status_code}")
        else:
            log(f"APP DOWN - Status Code: {response.status_code}")

    except requests.exceptions.RequestException:
        log("APP DOWN - No Response / Timeout")

# Main function
def main():
    print("Application Health Checker Started...\n")

    while True:
        check_app()
        time.sleep(10)

# Run program
if __name__ == "__main__":
    main()