# System Load Monitoring on macOS
# 🔍 Overview
This project collects, labels, and prepares real system telemetry data from macOS for use in Machine Learning (ML) and Reinforcement Learning (RL) applications, particularly for operating system scheduling simulations.

It includes:

Data logging with Python (psutil)

Creating synthetic workloads (CPU, memory, I/O, network)

Auto-labeling system state

Preprocessing & normalization

Visualization

# 🛠 Tools Used
Python + psutil

Shell (yes > /dev/null &) to simulate CPU load

pandas, matplotlib, sklearn

macOS Terminal

# 🧪 Data Collection Process
Data is logged in real-time every 5 seconds. Each entry includes:

timestamp: Time of recording

cpu_percent, memory_percent: System-level usage

pid, name: Process info

cpu_process, memory_process: Resource usage per process

# 📦 Synthetic Workload Timeline
|Stage |Start |Time	|Activity	|Label|
|------|------|-----|---------|-----||
|1  |00:31	|System idle	|idle|
|2	|00:34	|20x yes CPU stress	|high_cpu|
|3	|00:38	|Open Chrome, Xcode	|high_mem|
|4	|00:42	|Copy & zip large files	|disk_io|
|5	|00:45	|Watch video, download file	|network_load|
|6	|00:48	|Stop all apps → idle again	|idle|

# 🧹 Data Preprocessing
Rows with missing process info were removed

Features normalized (cpu_process, memory_process) using MinMaxScaler

Labels added automatically by comparing timestamp with known workload intervals

# 📈 Visualization
The chart below shows how CPU usage per process changes over time, segmented by labeled workload phases:


# 🧠 Future Applications
This labeled dataset can be used for:

Supervised learning to classify system load

Training RL agents to simulate or optimize OS scheduling

Benchmarking resource management strategies

# 📁 Files
mac_syslog_labeled_clean.csv: Cleaned, labeled, normalized dataset

system_load_over_time.png: Visualization image

log_system.py: Python script to collect data using psutil

📌 Feel free to fork or adapt for Linux or Windows systems, or extend it with more resource types (GPU, network packets, etc.).

