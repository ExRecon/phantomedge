
     ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗    ███████╗██████╗  ██████╗ ███████╗
     ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║    ██╔════╝██╔══██╗██╔════╝ ██╔════╝
     ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║    █████╗  ██║  ██║██║  ███╗█████╗  
     ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║    ██╔══╝  ██║  ██║██║   ██║██╔══╝  
     ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║    ███████╗██████╔╝╚██████╔╝███████╗
     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝    ╚══════╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                                    


**PHANTOM EDGE** is a modular command-line toolkit designed for Kali Linux to streamline offensive security operations. It simplifies the execution of commonly used reconnaissance tools while keeping results logged, organized, and repeatable. The project is built for ethical hackers, red teamers, and cybersecurity students.

---

## 🔥 Features

- 📡 Recon Modules (Nmap, Netrange scan, Autodiscover probe)
- 🕵️ Passive Recon Tools (WHOIS, DNS, Subdomains, Email Harvesting)
- 📁 Target History Tracking
- 🧪 Virtual Environment with Isolated Dependencies
- ⚙️ Modular Design – Easily Extendable with New Tools

---

## 📂 Module Overview

| Module            | Description                                  |
|-------------------|----------------------------------------------|
| `Recon Tools`     | Active network and host scanning             |
| `Passive Recon`   | Collects OSINT and passive metadata          |
| `Target History`  | View and track scanned targets               |
| `Installer`       | Auto-installs APT & Python packages + venv   |

---

## 🛠️ Installation

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/yourusername/kali-launcher.git
cd kali-launcher
```

### ✅ 2. Run the Installer
```bash
python3 installer.py
```

This will:
- Install system tools: `nmap`, `whois`, `dig`, `sublist3r`, `theHarvester`, etc.
- Set up a Python virtual environment in `./venv`
- Install Python packages (e.g., `rich`) inside the venv

> 🔥 **Important:** `netcat` is a virtual package. If the installer fails to choose one:
```bash
sudo apt install netcat-traditional
```

---

## 🚀 Usage

### ✅ 1. Activate the Environment
```bash
source venv/bin/activate
```

### ✅ 2. Launch the Tool
```bash
python main.py
```

### 🧭 Menu Preview
```
Kali Launcher Menu
[1] Recon Tools
[2] Passive Recon Tools
[3] Show Target History
[4] Exit
```

---

## 📋 Tool Dependencies

| Type         | Name                        |
|--------------|-----------------------------|
| System Tools | `nmap`, `whois`, `dnsutils`, `sublist3r`, `theharvester`, `netcat`, `curl` |
| Python       | `rich`                      |

---

## 📁 Folder Structure

```
kali-launcher/
├── main.py
├── installer.py
├── config.py
├── core/
│   ├── logger.py
│   └── history.py
├── modules/
│   ├── recon.py
│   └── passive.py
├── logs/
│   └── [output logs]
├── venv/
│   └── [virtual environment]
```

---



## 📜 License

MIT License  
**For educational, ethical hacking, and authorized penetration testing only.**

---

## 🧑‍💻 Author

**ExRecon**  
🔗 https://www.linkedin.com/in/exrecon
🔗 https://medium.com/@exreconnaissance
