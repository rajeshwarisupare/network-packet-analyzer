# Network Packet Analyzer

A Python network packet analyzer that uses Scapy to capture and summarize up to 20 packets.

## Features

- Captures packets from an available network interface
- Displays source and destination IP addresses for IPv4, IPv6, and ARP packets
- Identifies TCP, UDP, ICMP, ICMPv6, and ARP traffic
- Displays packet length and a Scapy packet summary
- Shows a hexadecimal preview of up to 32 raw payload bytes

## Requirements

- Python 3.8 or newer
- Scapy (installed from `requirements.txt`)
- Npcap on Windows for live packet capture

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

Install Scapy:

```powershell
python -m pip install -r requirements.txt
```

On Windows, install Npcap if needed. Packet capture may require elevated privileges and a valid capture interface.

## Usage

```powershell
python packet_analyzer.py
```

The analyzer stops after 20 packets, or earlier if you press Ctrl+C. Capture only traffic on your own device or on a network for which you have permission. Packet payload previews may contain sensitive data.

## GitHub

From this project directory, stage, commit, and push changes to the configured remote:

```powershell
git add packet_analyzer.py README.md requirements.txt .gitignore
git commit -m "Update network packet analyzer"
git push
```
