import os
import requests
import logging
from datetime import datetime


log_dir = os.path.join(os.path.dirname(__file__), '../logs')
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    filename=os.path.join(log_dir, 'app_status.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


URL = "http://localhost:5000"  

def check_app_health():
    """Check if the application is running and responding correctly."""
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            logging.info(f" App is UP ({response.status_code})")
            print("App is UP ")
        else:
            logging.warning(f" App responded with unexpected status {response.status_code}")
            print(f"App responded with status {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"App is DOWN - {e}")
        print("App is DOWN")

if __name__ == "__main__":
    print("Running Application Health Checker...")
    check_app_health()
    print("Check complete. Logs updated.")
