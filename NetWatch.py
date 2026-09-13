import platform
import socket
import subprocess
import time


COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]


def check_connectivity():
    host = input("Enter host (e.g., google.com): ").strip()

    if not host:
        print("[-] Host cannot be empty.")
        return

    try:
        ip = socket.gethostbyname(host)
        start = time.perf_counter()

        # Test TCP connectivity using HTTP port 80.
        with socket.create_connection((host, 80), timeout=3):
            pass

        response_time = (time.perf_counter() - start) * 1000
        print(f"\n[+] Host: {host}")
        print(f"[+] IP Address: {ip}")
        print("[+] Status: Reachable")
        print(f"[+] TCP Response Time: {response_time:.2f} ms")

    except socket.gaierror:
        print("[-] Could not resolve the host name.")
    except OSError as error:
        print("[-] Host is unreachable or the connection failed.")
        print(f"    Reason: {error}")


def scan_ports():
    host = input("Enter host or IP address: ").strip()

    if not host:
        print("[-] Host cannot be empty.")
        return

    try:
        ip = socket.gethostbyname(host)
        print(f"\nScanning {host} ({ip})...\n")
        open_ports = []

        for port in COMMON_PORTS:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((ip, port))

            if result == 0:
                open_ports.append(port)
                print(f"[OPEN] Port {port}")

        if not open_ports:
            print("No open ports found in the selected list.")

        print("\nScan completed.")

    except socket.gaierror:
        print("[-] Invalid host name or IP address.")


def dns_lookup():
    domain = input("Enter domain name: ").strip()

    if not domain:
        print("[-] Domain cannot be empty.")
        return

    try:
        ip = socket.gethostbyname(domain)
        print("\n[+] DNS Lookup Result")
        print(f"[+] Domain: {domain}")
        print(f"[+] IP Address: {ip}")
    except socket.gaierror:
        print("[-] Could not resolve the domain.")


def show_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        # The fallback is useful when the hostname resolves to loopback.
        if local_ip.startswith("127."):
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.connect(("8.8.8.8", 80))
                local_ip = sock.getsockname()[0]

        print(f"\n[+] Computer Name: {hostname}")
        print(f"[+] Local IP Address: {local_ip}")
    except OSError as error:
        print(f"[-] Could not determine local IP: {error}")


def ping_test():
    host = input("Enter host to ping: ").strip()

    if not host:
        print("[-] Host cannot be empty.")
        return

    system = platform.system().lower()
    command = ["ping", "-n", "4", host] if system == "windows" else ["ping", "-c", "4", host]

    try:
        result = subprocess.run(command, check=False)
        if result.returncode != 0:
            print("[-] Ping completed, but the host did not respond successfully.")
    except FileNotFoundError:
        print("[-] The ping command was not found on this system.")
    except OSError as error:
        print(f"[-] Ping failed: {error}")


def main():
    while True:
        print("\n" + "=" * 40)
        print("       NETWATCH - NETWORK MONITOR")
        print("=" * 40)
        print("1. Check Host Connectivity")
        print("2. Scan Common Ports")
        print("3. DNS Lookup")
        print("4. Show Local IP")
        print("5. Ping Test")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            check_connectivity()
        elif choice == "2":
            scan_ports()
        elif choice == "3":
            dns_lookup()
        elif choice == "4":
            show_local_ip()
        elif choice == "5":
            ping_test()
        elif choice == "6":
            print("Thank you for using NetWatch!")
            break
        else:
            print("[-] Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
