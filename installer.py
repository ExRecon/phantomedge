import os
import subprocess
from rich.console import Console

console = Console()

VENV_DIR = "venv"
APT_PACKAGES = [
    "whois",
    "dnsutils",       # dig
    "sublist3r",
    "theharvester",
    "nmap",
    "curl",
    "netcat-openbsd",
    "netcat-traditional",
    "python3-pip",
    "python3-venv"
]

PYTHON_PACKAGES = [
    "rich"
]

def install_apt_packages():
    console.print("[bold blue]Installing APT packages...[/bold blue]")
    for pkg in APT_PACKAGES:
        console.print(f"[green]Installing:[/green] {pkg}")
        subprocess.call(f"sudo apt-get install -y {pkg}", shell=True)

def setup_virtualenv():
    if not os.path.isdir(VENV_DIR):
        console.print(f"[bold blue]Creating virtual environment at ./{VENV_DIR}[/bold blue]")
        subprocess.call(f"python3 -m venv {VENV_DIR}", shell=True)
    else:
        console.print(f"[yellow]Virtual environment already exists at {VENV_DIR}[/yellow]")

def install_python_packages():
    console.print("[bold blue]Installing Python packages inside virtual environment...[/bold blue]")
    pip_path = os.path.join(VENV_DIR, "bin", "pip")
    for pkg in PYTHON_PACKAGES:
        console.print(f"[green]Installing:[/green] {pkg}")
        subprocess.call(f"{pip_path} install {pkg}", shell=True)

def main():
    console.print("[bold underline]Kali Launcher Installer with Virtual Environment[/bold underline]")
    install_apt_packages()
    setup_virtualenv()
    install_python_packages()
    console.print(f"\n[bold cyan]✔️ Setup complete. To activate your environment:[/bold cyan]")
    console.print(f"[green]source {VENV_DIR}/bin/activate[/green]")
    console.print(f"[bold cyan]Then run:[/bold cyan] python main.py")

if __name__ == "__main__":
    main()
