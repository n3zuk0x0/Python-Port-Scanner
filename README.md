#  Python Port Scanner

A fast, multithreaded **port scanner** built in Python with **banner grabbing** capability. It scans a target for open ports and attempts to identify the services running on them.

>  **For educational and authorized use only.** Only scan systems you own or have explicit permission to test.

---

##  Features

-  **Multithreaded scanning** — checks multiple ports simultaneously for speed
-  **Banner grabbing** — identifies services/versions on open ports
-  **Custom port range** — scan any range you choose
-  **Clean summary report** — lists all open ports at the end
-  **Lightweight** — uses only Python's built-in libraries

---

##  Tech Stack

- **Python 3**
- `socket` (networking)
- `threading` (concurrent scanning)

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-port-scanner.git
cd python-port-scanner
```

No external dependencies needed — it uses Python's standard library!

---

##  Usage

Run the scanner:

```bash
python port_scanner.py
```

Then enter the target and port range when prompted:

```
Enter target IP/hostname: 127.0.0.1
Start port: 1
End port: 9000
```

---

##  Example Output

```
==================================================
             Python Port Scanner
==================================================
Enter target IP/hostname: scanme.nmap.org
Start port: 1
End port: 100

Scanning scanme.nmap.org from port 1 to 100...

[+] Port 22 OPEN  →  SSH-2.0-OpenSSH_6.6.1p1
[+] Port 80 OPEN  →  HTTP/1.0 200 OK

--- Scan Complete ---
Open ports: [22, 80]
```

---

##  What I Learned

- How TCP connections and sockets work
- Multithreading for performance
- Banner grabbing and service identification
- Writing clean, modular Python code

---

## Legal Disclaimer

This tool is intended for **educational purposes** and **authorized security testing only**. Scanning networks or systems without permission is **illegal**. The author is not responsible for any misuse.

Safe practice targets:
- `127.0.0.1` (your own machine)
- `scanme.nmap.org` (Nmap's official legal test server)

---

##  Future Improvements

- [ ] Thread pool for handling large port ranges safely
- [ ] Save scan results to a file
- [ ] Map common ports to service names (e.g., 22 → SSH)
- [ ] Colored terminal output

