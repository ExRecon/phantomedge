from rich.console import Console
from rich.prompt import Prompt
from core.history import show_history
from modules.recon import recon_menu
from modules.passive import passive_menu

console = Console()

def show_banner():
    banner = """
 ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗    ███████╗██████╗  ██████╗ ███████╗
██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║    ██╔════╝██╔══██╗██╔════╝ ██╔════╝
██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║    █████╗  ██║  ██║██║  ███╗█████╗  
██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║    ██╔══╝  ██║  ██║██║   ██║██╔══╝  
██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║    ███████╗██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝    ╚══════╝╚═════╝  ╚═════╝ ╚══════╝
"""
    console.print(f"[cyan]{banner}[/cyan]")

def main_menu():
    show_banner()
    while True:
        console.print("\n[bold underline]PhantomEdge Menu[/bold underline]")
        console.print("[1] Recon Tools")
        console.print("[2] Passive Recon Tools")
        console.print("[3] Show Target History")
        console.print("[4] Exit")

        choice = Prompt.ask("Select option", choices=["1", "2", "3", "4"])

        if choice == "1":
            recon_menu()
        elif choice == "2":
            passive_menu()
        elif choice == "3":
            show_history()
        elif choice == "4":
            console.print("[cyan]Exiting PhantomEdge. Stay stealthy.[/cyan]")
            break

if __name__ == "__main__":
    main_menu()
