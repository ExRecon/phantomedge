import os
import subprocess
from rich.console import Console
from rich.prompt import Prompt
from config import LOG_DIR
from core.logger import log_action

console = Console()

def passive_menu():
    console.print("[bold blue]Passive Recon Module[/bold blue]")
    console.print("[1] WHOIS Lookup")
    console.print("[2] DNS Records (A, MX, NS, TXT)")
    console.print("[3] Subdomain Enumeration (Sublist3r)")
    console.print("[4] Email Harvesting (theHarvester)")

    choice = Prompt.ask("Choose tool", choices=["1", "2", "3", "4"])
    domain = Prompt.ask("Enter target domain (e.g., target.com)")
    timestamp = str(os.getpid())
    output_file = os.path.join(LOG_DIR, f"passive_{choice}_{domain}_{timestamp}.txt")

    if choice == "1":
        cmd = f"whois {domain}"
    elif choice == "2":
        cmd = (
            f"dig A {domain} +short && "
            f"dig MX {domain} +short && "
            f"dig NS {domain} +short && "
            f"dig TXT {domain} +short"
        )
    elif choice == "3":
        cmd = f"sublist3r -d {domain} -o {output_file}"
    elif choice == "4":
        cmd = f"theHarvester -d {domain} -b all -f {output_file}"

    console.print(f"[green]Running:[/green] {cmd}")
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        if choice in ["1", "2"]:  # output comes from stdout
            with open(output_file, "w") as f:
                f.write(output)
        console.print(f"[cyan]Output saved to:[/cyan] {output_file}")
        log_action(f"Passive Recon [{choice}]: {domain}", f"Output: {output_file}")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error running command:[/red] {e}")
