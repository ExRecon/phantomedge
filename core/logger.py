
from datetime import datetime
from config import LOG_FILE

def log_action(action, result="Executed"):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {action} => {result}\n")
