
import subprocess
from config import OUTPUT_FILE
from core.logger import log_action
from core.history import save_history
from rich.console import Console

console = Console()

def run_command(command, target=None):
    console.print(f"[bold green]Executing:[/bold green] {command}")
    log_action(command)
    if target:
        save_history(target)
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        with open(OUTPUT_FILE, "w") as f:
            f.write(output)
        console.print("[blue]Command output saved to:[/blue] " + OUTPUT_FILE)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error running command:[/red] {e}")
        with open(OUTPUT_FILE, "w") as f:
            f.write(e.output)
