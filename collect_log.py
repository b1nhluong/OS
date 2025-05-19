import time
import psutil
import pandas as pd
import os

data = []
print("⏺️ Ghi log nâng cao... Nhấn Ctrl+C để dừng.")

try:
    while True:
        ts = time.time()
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        load1, load5, load15 = os.getloadavg()

        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                info = proc.info
                io = proc.io_counters() if proc.io_counters() else None
                ctx = proc.num_ctx_switches()
                nice = proc.nice()

                data.append({
                    'timestamp': ts,
                    'cpu_percent': cpu,
                    'memory_percent': mem,
                    'load_avg_1': load1,
                    'load_avg_5': load5,
                    'load_avg_15': load15,
                    'pid': info['pid'],
                    'name': info['name'],
                    'cpu_process': info['cpu_percent'],
                    'memory_process': info['memory_percent'],
                    'read_bytes': io.read_bytes if io else 0,
                    'write_bytes': io.write_bytes if io else 0,
                    'ctx_voluntary': ctx.voluntary,
                    'ctx_involuntary': ctx.involuntary,
                    'nice': nice,
                    'label': 'unlabeled'
                })

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

except KeyboardInterrupt:
    df = pd.DataFrame(data)
    df.to_csv('linux_syslog_extended.csv', index=False)
    print("✅ Đã lưu vào linux_syslog_extended.csv")
