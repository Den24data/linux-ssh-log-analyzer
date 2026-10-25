# Linux SSH Log Analyzer

## Project Overview

This project explores Linux, SSH security, and security log analysis using Python.

The goal is to develop a simple tool that analyzes SSH authentication logs and identifies potentially suspicious login activity, such as repeated failed login attempts.

The project is developed as a hands-on cybersecurity learning exercise using Ubuntu on Windows Subsystem for Linux (WSL2). It uses synthetic SSH authentication logs.

## Objectives

- Practice Linux administration and terminal commands.
- Understand SSH authentication and system logging.
- Examine SSH authentication events.
- Develop a Python script to parse and analyze log data.
- Identify repeated failed login attempts using simple detection rules.
- Document findings, limitations, and lessons learned.

## Technologies

| Technology | Purpose |
|---|---|
| Linux (Ubuntu / WSL2) | Development environment |
| SSH | Understanding secure remote access and authentication |
| Python 3 | Log parsing and analysis |
| Bash | Linux terminal commands |
| Git & GitHub | Version control and documentation |

## Implementation

The current Python script:

1. Reads a synthetic SSH authentication log.
2. Identifies failed password authentication attempts.
3. Extracts the source IP address from each matching log entry.
4. Counts failed attempts per IP address.
5. Displays a warning when an IP address reaches three or more failed attempts.

## Project Structure

```text
linux-ssh-log-analyzer/
├── data/
│   └── sample_auth.log
├── src/
│   └── analyze_ssh.py
├── .gitignore
└── README.md
```

## How to Run

From the project root directory, execute:

```bash
python3 src/analyze_ssh.py
```

No external Python packages are required.

## Example Results

```text
Failed SSH logins by IP:
------------------------
192.0.2.10: 3 failed attempts
192.0.2.30: 2 failed attempts

Potential suspicious activity:
------------------------------
WARNING: 192.0.2.10 has 3 failed login attempts
```

The script also prints the Python `Counter` object before the formatted results.

## Project Status

**Status: Initial implementation completed**

The first version of the SSH log analyzer has been implemented and tested using synthetic authentication events.

Development is organized using Git feature branches.

## Security and Privacy

- All authentication logs included in this repository are synthetic.
- Sample IP addresses are reserved for documentation purposes.
- No real server authentication logs, private SSH keys, credentials, or sensitive configuration files are published.

## Limitations

- Failed attempts are counted across the entire log file without considering a time window.
- The parser assumes a specific SSH log format.
- The detection threshold is currently set to three failed attempts.
- A warning indicates potentially suspicious activity, not confirmed malicious behavior.

## Future Improvements

Potential extensions include:

- Time-based detection rules.
- Additional authentication event types.
- Automated log analysis.
- Unit tests and improved error handling.
- Structured JSON output.
- Optional analysis of appropriately sanitized logs from a Linux server.
