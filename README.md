# Linux SSH Log Analyzer

## Project Overview

This project explores basic Linux system administration, SSH security, and security log analysis using Python.

The goal is to develop a simple tool that analyzes SSH authentication logs and identifies potentially suspicious login activity, such as repeated failed login attempts.

The project is developed as a hands-on learning exercise using a personal Linux VPS.

## Objectives

- Learn basic Linux administration and terminal commands.
- Understand SSH authentication and system logging.
- Collect and examine SSH authentication events.
- Develop a Python script to parse and analyze log data.
- Identify repeated failed login attempts using simple detection rules.
- Document findings, limitations, and lessons learned.

## Technologies

| Technology | Purpose |
|---|---|
| Linux (Ubuntu, planned) | Server environment |
| SSH | Secure remote administration |
| Python | Log parsing and analysis |
| Bash | Linux commands and basic scripting |
| Git & GitHub | Version control and documentation |

## Planned Workflow

1. Set up and secure a Linux VPS.
2. Explore SSH authentication logs.
3. Create synthetic sample log data.
4. Develop a Python log parser.
5. Implement a rule for detecting repeated failed login attempts.
6. Test and document the results.

## Project Status

**Status: Planning / Not yet implemented**

Development will be carried out incrementally using feature branches and pull requests.

## Security and Privacy

This project uses a personally controlled VPS and synthetic or sanitized sample data.

Private SSH keys, credentials, sensitive configuration files, and raw server logs will not be published in this repository.

## Future Improvements

Potential extensions include:

- Time-based detection rules.
- Additional authentication event types.
- Automated log analysis.
- Unit tests and improved error handling.
- Structured output for further analysis.
