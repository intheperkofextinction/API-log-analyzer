# parse_logs.py

from collections import defaultdict
from datetime import datetime 

log_counts = defaultdict(int)
hourly_counts = defaultdict(int)

with open("request.log","r") as file:
    for line in file:
        timestamp, method_url = line.strip().split(" - ")
        dt = datetime.fromisoformat(timestamp)
        hour = dt.strftime("%H:00")
        method, endpoint = method_url.split(" ",1)

        log_counts[endpoint] += 1
        hourly_counts[hour] += 1

with open("logs_summary.txt", "w") as out:
    out.write("Request Count by Endpoint:\n")
    for endpoint, count in log_counts.items():
        out.write(f"{endpoint}: {count}\n")

    out.write("\n Request Count by hour:\n")
    for hour, count in sorted(hourly_counts.items()):
        out.write(f"{hour}: {count} requests\n")
