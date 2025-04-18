# 🧠 API Log Analyzer

This project contains a simple Node.js API that logs every incoming request to a file. A Python script then analyzes the log file and provides a summary of API usage by endpoint and by hour.

## 🚀 How It Works

1. **Express API (Node.js):**
   - Logs every incoming request to `request.log`.

2. **Python Script:**
   - Parses the log file.
   - Outputs a summary to `logs_summary.txt`.

## 📦 Getting Started

### Prerequisites
- Node.js
- Python 3

### Installation
```bash
git clone https://github.com/YOUR_USERNAME/api-log-analyzer.git
cd api-log-analyzer
npm install

 Technologies
Node.js + Express

Python 3
