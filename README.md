# Network Packet Analyzer

A Python packet analyzer that uses Scapy to capture and summarize up to 20 network packets.

## Features

- Captures packets from an available network interface
- Displays source and destination IP addresses for IPv4, IPv6, and ARP packets
- Identifies TCP, UDP, ICMP, ICMPv6, and ARP traffic
- Displays packet length and a Scapy packet summary
- Shows a hexadecimal preview of up to 32 raw payload bytes

## Requirements

- Python 3.8 or newer
- Scapy
- On Windows, Npcap is generally required for live packet capture

## Installation

From this project directory, create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, allow it for the current terminal session and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

Install the dependency:

```powershell
python -m pip install -r requirements.txt
```

Install Npcap on Windows if needed. Packet capture may also require elevated privileges.

## Usage

```powershell
python packet_analyzer.py
```

The analyzer stops after 20 packets, or earlier if you press Ctrl+C. Capture only traffic on your own device or on a network for which you have permission. Packet payload previews may contain sensitive data.

## Uploading to GitHub

Create an empty repository on GitHub, then run these commands from this project directory (replace `YOUR_USERNAME` with your GitHub username):

```powershell
git init
git add packet_analyzer.py README.md requirements.txt .gitignore
git commit -m "Add network packet analyzer"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/network-packet-analyzer.git
git push -u origin main
```
