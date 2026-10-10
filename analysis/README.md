Cowrie Log Analyzer

A Python script for summarizing Cowrie JSON event logs.

Requirements

- Python 3
- No external Python packages required

Run

From the repository root:

python3 analysis/log_analyzer.py

Input

The script reads the sanitized sample log at "data/sample_cowrie.json".

Output

- Event counts
- Most common usernames
- Most common source IP addresses

Security

Use sanitized logs only. Do not publish real credentials, sensitive IP information, or private honeypot data.
