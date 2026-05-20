import os
import time
import random

# Colors
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

os.system("clear")

# Banner
banner = f"""
{GREEN}

██╗  ██╗███╗   ███╗████████╗
██║ ██╔╝████╗ ████║╚══██╔══╝
█████╔╝ ██╔████╔██║   ██║
██╔═██╗ ██║╚██╔╝██║   ██║
██║  ██╗██║ ╚═╝ ██║   ██║
╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝

==================================
      K M T   S Y S T E M
==================================

{RESET}
"""

print(banner)

# Fake loading
print(f"{CYAN}[~] Connecting To TikTok Server...{RESET}")
time.sleep(2)

print(f"{CYAN}[~] Bypassing Security...{RESET}")
time.sleep(2)

print(f"{CYAN}[~] Access Granted...{RESET}")
time.sleep(1)

# Username input
username = input(f"{YELLOW}[?] Enter TikTok Username : {RESET}")

os.system("clear")
print(banner)

print(f"{GREEN}[✓] Target Locked : @{username}{RESET}")
time.sleep(1)

# Fake delete loop
while True:

    percent = random.randint(10, 99)

    print(f"{RED}[!] Deleting Account @{username} ... {percent}%{RESET}")

    fake_logs = [
        "Removing Videos...",
        "Deleting Followers...",
        "Disconnecting Device...",
        "Removing Profile Data...",
        "Clearing Cloud Storage...",
        "Destroying TikTok Cache...",
        "Accessing Database...",
        "Finalizing Delete Request..."
    ]

    print(f"{GREEN}[+] {random.choice(fake_logs)}{RESET}")

    time.sleep(1.5)
