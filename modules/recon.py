import os
import re
import subprocess
from time import time
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import Progress
from config import LOG_DIR
from core.logger import log_action
from core.runner import run_command

console = Console()

def recon_menu():
    console.print("[bold blue]Recon Menu[/bold blue]")
    console.print("[1] Nmap Aggressive Scan")
    console.print("[2] Nmap Top 1000 Ports")
    console.print("[3] Scan Network Range")
    console.print("[4] Investigate Mail Services via Autodiscover")

    choice = Prompt.ask("Choose tool", choices=["1", "2", "3", "4"])

    if choice in ["1", "2"]:
        target = Prompt.ask("Enter target IP or domain")
        if choice == "1":
            cmd = f"nmap -A -T4 {target}"
        elif choice == "2":
            cmd = f"nmap --top-ports 1000 -T4 {target}"
        run_command(cmd, target)

    elif choice == "3":
        scan_netrange()
    elif choice == "4":
        investigate_autodiscover()


def scan_netrange():
    netrange = Prompt.ask("Enter network range in CIDR (e.g., 192.168.1.0/24)")
    timestamp = int(time())
    output_file = os.path.join(LOG_DIR, f"netrange_scan_{timestamp}.txt")
    live_hosts_file = os.path.join(LOG_DIR, f"live_hosts_{timestamp}.txt")

    console.print(f"[bold green]Starting scan of:[/bold green] {netrange}")

    with Progress() as progress:
        task = progress.add_task("[cyan]CIDR sweep...", total=3)

        try:
            cmd = f"nmap -sn {netrange}"
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            with open(output_file, "w") as f:
                f.write(output)
            progress.update(task, advance=1)

            live_hosts = re.findall(r"Nmap scan report for ([\\d.]+)", output)
            with open(live_hosts_file, "w") as f:
                for ip in live_hosts:
                    f.write(ip + "\n")
            progress.update(task, advance=1)

            console.print(f"[cyan]Scan output saved to:[/cyan] {output_file}")
            console.print(f"[green]Live hosts saved to:[/green] {live_hosts_file}")
            log_action(f"Nmap netrange scan: {netrange}", f"Live hosts: {len(live_hosts)}")

            if live_hosts:
                console.print("\n[bold magenta]Choose chained scan mode:[/bold magenta]")
                console.print("[1] Run default script scan (-sC)")
                console.print("[2] Run vuln NSE scripts (--script vuln)")
                console.print("[3] Run both")
                console.print("[4] Skip chained scan")
                input("Press [Enter] to select scan mode...")
                mode = Prompt.ask("Select option", choices=["1", "2", "3", "4"])

                scan_flags = "-T4"
                if mode == "1":
                    scan_flags += " -sC"
                elif mode == "2":
                    scan_flags += " --script vuln"
                elif mode == "3":
                    scan_flags += " -sC --script vuln"
                elif mode == "4":
                    console.print("[yellow]Skipping chained scan.[/yellow]")
                    progress.update(task, advance=1)
                    return

                live_ip_string = " ".join(live_hosts)
                chained_cmd = f"nmap {scan_flags} {live_ip_string}"
                chained_scan_file = os.path.join(LOG_DIR, f"chained_scan_{timestamp}.txt")
                console.print(f"[bold blue]Running:[/bold blue] {chained_cmd}")
                chained_output = subprocess.check_output(chained_cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                with open(chained_scan_file, "w") as f:
                    f.write(chained_output)
                console.print(f"[bold green]Chained scan results saved to:[/bold green] {chained_scan_file}")
                log_action(f"Chained Nmap: {scan_flags}", f"Saved to {chained_scan_file}")
                progress.update(task, advance=1)
            else:
                console.print("[yellow]No live hosts found to scan.[/yellow]")
                progress.update(task, advance=1)

        except subprocess.CalledProcessError as e:
            console.print(f"[red]Error scanning netrange:[/red] {e}")
            with open(output_file, "w") as f:
                f.write(e.output)
            progress.update(task, advance=1)

    return


def investigate_autodiscover():
    domain = Prompt.ask("Enter domain to investigate (e.g., target.com)")
    timestamp = int(time())
    output_file = os.path.join(LOG_DIR, f"autodiscover_{domain}_{timestamp}.txt")

    console.print(f"[bold green]Probing mail services for:[/bold green] {domain}")
    with open(output_file, "w") as f:
        try:
            f.write(f"==== MX Records ====\n")
            mx = subprocess.check_output(f"dig +short MX {domain}", shell=True, text=True)
            f.write(mx + "\n")

            f.write(f"==== Autodiscover Subdomain Check ====\n")
            auto_url = f"https://autodiscover.{domain}/autodiscover/autodiscover.xml"
            f.write(f"URL: {auto_url}\n")
            curl_result = subprocess.check_output(f"curl -s -I {auto_url}", shell=True, text=True)
            f.write(curl_result + "\n")

            f.write(f"==== CNAME Lookup for Autodiscover ====\n")
            cname = subprocess.check_output(f"dig +short CNAME autodiscover.{domain}", shell=True, text=True)
            f.write(cname + "\n")

            f.write(f"==== SMTP Banner (if available) ====\n")
            smtp = subprocess.run(f"nc -v mail.{domain} 25", shell=True, capture_output=True, text=True, timeout=10)
            f.write(smtp.stdout + smtp.stderr)

            console.print(f"[bold cyan]Results saved to:[/bold cyan] {output_file}")
            log_action(f"Autodiscover probe: {domain}", f"Saved to {output_file}")
        except subprocess.CalledProcessError as e:
            console.print(f"[red]Command failed:[/red] {e}")
        except subprocess.TimeoutExpired:
            console.print("[yellow]SMTP banner timeout.[/yellow]")
