
from config import HISTORY_FILE
from rich.console import Console

console = Console()

def save_history(target):
    from datetime import datetime
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{datetime.now()} {target}\n")

def show_history():
    if not HISTORY_FILE or not HISTORY_FILE.strip():
        console.print("[yellow]History path not set correctly.[/yellow]")
        return
    try:
        with open(HISTORY_FILE, "r") as f:
            console.print("[bold cyan]Target History:[/bold cyan]")
            console.print(f.read())
    except FileNotFoundError:
        console.print("[yellow]No history yet.[/yellow]")
