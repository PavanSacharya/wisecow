import os
import psutil
import logging
from datetime import datetime

s
log_dir = os.path.join(os.path.dirname(__file__), '../logs')
os.makedirs(log_dir, exist_ok=True)

g
logging.basicConfig(
    filename=os.path.join(log_dir, 'system_health.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    process_count = len(psutil.pids())

    logging.info(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Processes: {process_count}")

    if cpu > 80:
        logging.warning(" High CPU usage detected!")
    if memory > 80:
        logging.warning(" High Memory usage detected!")
    if disk > 90:
        logging.warning(" Low Disk Space!")

if __name__ == "__main__":
    print("Running System Health Monitor...")
    check_system_health()
    print("Check complete. Logs updated.")
