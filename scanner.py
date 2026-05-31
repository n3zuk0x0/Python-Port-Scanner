import socket
import threading

def print_banner():
    print("=" * 50)
    print("          Python Port Scanner")
    print("=" * 50)

open_ports = []

def scan_port(target, port):
    """Scan a single port and grab its banner if open."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        open_ports.append(port)
        try:
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = s.recv(1024).decode().strip()
            first_line = banner.split("\n")[0] if banner else "(no banner)"
            print(f"[+] Port {port} OPEN  →  {first_line}")
        except:
            print(f"[+] Port {port} OPEN  →  (no banner)")

    s.close()

def main():
    print_banner()

    target = input("Enter target IP/hostname: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n--- Scan Complete ---")
    print(f"Open ports: {sorted(open_ports) if open_ports else 'None found'}")

if __name__ == "__main__":
    main()