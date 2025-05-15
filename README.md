# 📊 System Load Monitoring on macOS

## 🔍 Overview

This project collects, labels, and prepares real system telemetry data from macOS for use in Machine Learning (ML) and Reinforcement Learning (RL) applications, particularly for operating system scheduling simulations.

It includes:
- Data logging with Python (`psutil`)
- Creating synthetic workloads (CPU, memory, I/O, network)
- Auto-labeling system state based on timeline
- Preprocessing & normalization
- Visualization

---

## 🛠 Tools Used

- Python + `psutil`
- Shell (`yes > /dev/null &`) to simulate CPU load
- `pandas`, `matplotlib`, `sklearn`
- macOS Terminal

---

## 🧪 Data Collection Process

Data is logged in real-time every 5 seconds. Each entry includes:

- `timestamp`: Time of recording
- `cpu_percent`, `memory_percent`: System-level usage
- `pid`, `name`: Process info
- `cpu_process`, `memory_process`: Normalized per-process resource usage

---

## 📦 Synthetic Workload Timeline

| Stage | Start Time          | Activity                         | Label          |
|-------|---------------------|----------------------------------|----------------|
| 1     | 13:46:53            | System idle                      | idle           |
| 2     | 13:47:30            | 20x `yes` CPU stress             | high_cpu       |
| 3     | 13:48:30            | Open Chrome, Xcode, VSCode       | high_mem       |
| 4     | 13:49:30            | Copy and compress large files    | disk_io        |
| 5     | 13:50:30            | Watch video, download files      | network_load   |
| 6     | 13:51:30            | Mix all workload types           | mixed          |
| 7     | 13:52:30            | Stop all apps → idle again       | idle           |

---

## 🧹 Data Preprocessing

- Rows with missing process data were removed
- `cpu_process` and `memory_process` were normalized to [0, 1] using `MinMaxScaler`
- Labels were added automatically by matching `timestamp` with predefined workload phases

---

## 📈 Visualization

The chart below shows how CPU usage per process changes over time, segmented by labeled workload phases:

![System Load Over Time](output.png)

---

## 📁 Files

- `mac_syslog.csv`: Cleaned, labeled, and normalized dataset
- `output.png`: Visualization image
- `log_system.py`: Python script to collect data using `psutil`
