import psutil
import time
import csv
from datetime import datetime

# Tạo (hoặc ghi đè) file CSV để lưu dữ liệu
with open("mac_syslog.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "cpu_percent", "memory_percent", "pid", "name", "cpu_process", "memory_process"])

    try:
        while True:
            timestamp = datetime.now().isoformat()
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_percent = psutil.virtual_memory().percent

            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    writer.writerow([
                        timestamp,
                        cpu_percent,
                        memory_percent,
                        proc.info['pid'],
                        proc.info['name'],
                        proc.info['cpu_percent'],
                        proc.info['memory_percent']
                    ])
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            time.sleep(5)  # Chờ 5 giây rồi lặp lại
    except KeyboardInterrupt:
        print("Đã dừng ghi log.")
