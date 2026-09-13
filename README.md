# NetWatch – Network Monitoring & Diagnostics Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-Educational-green)

NetWatch is a lightweight, Python-based command-line tool for basic network troubleshooting and diagnostics. It demonstrates practical networking concepts such as DNS resolution, TCP sockets, port connectivity, IP addressing, latency, and ICMP ping.

## Features

- **Host Connectivity Check** – Resolves a host and tests TCP connectivity on port 80.
- **Common Port Scanner** – Checks a predefined list of common TCP ports.
- **DNS Lookup** – Resolves a domain name to an IPv4 address.
- **Local IP Detection** – Displays the computer hostname and local IP address.
- **Ping Test** – Uses the operating system's ping command to test reachability.
- **Cross-platform logic** – Supports Windows and Unix-like ping syntax.
- **Simple CLI menu** – Easy to use without external Python packages.

## Technologies and Concepts

| Technology / Concept | Usage |
|---|---|
| Python | Application development |
| `socket` | DNS, TCP connections, and port checks |
| `subprocess` | Operating-system ping command |
| `platform` | Operating-system detection |
| TCP/IP | Network communication concepts |
| DNS | Domain-to-IP resolution |

## Project Structure

```text
network-monitoring-tool/
├── NetWatch.py
└── README.md
```

## Requirements

- Python 3.8 or later
- An active network connection for external host tests

No third-party libraries are required.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/vincentcibin-a11y/network-monitoring-tool.git
   cd network-monitoring-tool
   ```

2. Run the application:

   ```bash
   python NetWatch.py
   ```

   On Windows, you can also use:

   ```bash
   py NetWatch.py
   ```

## Example Menu

```text
========================================
       NETWATCH - NETWORK MONITOR
========================================
1. Check Host Connectivity
2. Scan Common Ports
3. DNS Lookup
4. Show Local IP
5. Ping Test
6. Exit
```

## Networking Concepts Demonstrated

- IP addresses and hostnames
- DNS resolution
- TCP socket connections
- Port numbers and service availability
- Client-server communication
- Network latency
- Basic connectivity troubleshooting

## Safety Notice

Use this tool only on systems and networks you own or are authorized to test. Port scanning can be considered intrusive when performed without permission.

## Future Enhancements

- Add continuous monitoring and periodic refresh
- Export results to CSV or JSON
- Add network-interface information
- Add logging and alert notifications
- Build a graphical user interface
- Add configurable ports and timeout values

## Author

**Cibin Vincent**

GitHub: [vincentcibin-a11y](https://github.com/vincentcibin-a11y)
