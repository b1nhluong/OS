# 📊 OS Scheduler Baseline Policy Using Offline Machine Learning

## 🔍 Overview

This project collects, labels, and preprocesses system telemetry data from Ubuntu ARM64 running in UTM on macOS M1, aimed at building a baseline scheduling policy via offline machine learning.

Key components include:
- System data collection with Python scripts
- Generating synthetic workloads using `stress-ng`
- Auto-labeling system states based on workload schedule
- Data cleaning, normalization, and balancing for ML

---

## 🛠 Tools Used

- Ubuntu Desktop ARM64 in UTM on macOS M1
- Python (`pandas`, `scikit-learn`, `imbalanced-learn`)
- `stress-ng` for workload simulation
- Shell scripts for workload orchestration

---

## 🧪 Data Collection Process

System metrics are collected periodically during a 10-minute workload schedule with stages:

- Total CPU and RAM usage
- Process-level CPU and RAM usage
- Load averages (1, 5, 15 min)
- I/O read/write bytes
- Context switches and nice values

Data is saved as `.csv` for further analysis and ML training.

---

## 📦 Synthetic Workload Timeline

| Stage | Time (minutes) | Workload Type               | Label        |
|-------|----------------|----------------------------|--------------|
| 1     | 0–1            | Idle                       | idle         |
| 2     | 1–2            | CPU-bound                  | cpu-heavy    |
| 3     | 2–3            | RAM-bound                  | ram-heavy    |
| 4     | 3–4            | Mixed CPU + RAM            | mixed        |
| 5     | 4–5            | Idle                       | idle         |
| 6     | 5–6            | I/O-heavy                  | io-heavy     |
| 7     | 6–7            | Mixed (CPU + RAM + I/O)    | mixed-heavy  |
| 8     | 7–8            | RAM-heavy                  | ram-heavy    |
| 9     | 8–9            | CPU-heavy                  | cpu-heavy    |
| 10    | 9–10           | Idle                       | idle         |

---

## 🧹 Data Preprocessing

- Aggregated and merged logs by timestamp
- Removed outliers beyond 1st and 99th percentiles in numeric features
- Normalized numeric features using Min-Max scaling
- Automatically labeled logs based on workload time windows
- Balanced dataset via SMOTE to address class imbalance

---

## 📈 Dataset Summary

- Final dataset contains ~1,045 samples evenly distributed across 6 labels.
- Data saved as `linux_syslog_balanced.csv` ready for ML model training.

---

## 📁 Files

- `raw.csv`: Raw data
- `linux_syslog_labeled.csv`: Raw data with auto-assigned labels
- `linux_syslog_balanced.csv`: Balanced dataset for ML training
- `collect_log.py`: Python script to periodically collect system telemetry data including CPU usage, memory usage, process-level statistics, load averages, I/O bytes, context switches, and nice values. Uses libraries like `psutil` to extract metrics and logs data in CSV format for further processing.

---
