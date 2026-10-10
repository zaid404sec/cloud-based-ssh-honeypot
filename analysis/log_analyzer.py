
import json
from collections import Counter
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent.parent / "data" / "sample_cowrie.json"

def analyze_logs():
    if not LOG_FILE.exists():
        print(f"Log file not found: {LOG_FILE}")
        print("Place a sanitized Cowrie JSON log file there.")
        return

    event_counts = Counter()
    usernames = Counter()
    source_ips = Counter()

    with LOG_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            event_counts[event.get("eventid", "unknown")] += 1

            username = event.get("username")
            if username:
                usernames[username] += 1

            src_ip = event.get("src_ip")
            if src_ip:
                source_ips[src_ip] += 1

    print("=== Cowrie Log Summary ===")
    print("\nEvent types:")
    for name, count in event_counts.most_common():
        print(f"{name}: {count}")

    print("\nTop usernames:")
    for name, count in usernames.most_common(10):
        print(f"{name}: {count}")

    print("\nTop source IPs:")
    for ip, count in source_ips.most_common(10):
        print(f"{ip}: {count}")

if __name__ == "__main__":
    analyze_logs()
