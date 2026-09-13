import socket
import subprocess
import platform
import time


def check_connectivity():
    host = input("Enter host (e.g., google.com): ")

    try:
        ip = socket.gethostbyname(host)

        start = time.time()

        # Port 80 connection test
        sock = socket.create_connection((host, 80), timeout=3)
        sock.close()

        end = time.time()
        response_time = (end - start) * 1000

        print("\n[+] Host:", host)
        print("[+] IP Address:", ip)
        print("[+] Status: Reachable")
        print(f"[+] Response Time: {response_time:.2f} ms")

    except Exception as e:
        print("\n[-] Host is unreachable or connection failed.")
        print("Reason:", e)


def scan_ports():
    host = input("Enter host or IP address: ")

    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

    try:
        ip = socket.gethostbyname(host)
        print(f"\nScanning {host} ({ip})...\n")

        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"[OPEN] Port {port}")

            sock.close()

        print("\nScan completed.")

    except socket.gaierror:
        print("[-] Invalid host name.")


def dns_lookup():
    domain = input("Enter domain name: ")

    try:
        ip = socket.gethostbyname(domain)

        print("\n[+] DNS Lookup Result")
        print("[+] Domain:", domain)
        print("[+] IP Address:", ip)

    except socket.gaierror:
        print("[-] Could not resolve domain.")


def show_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        print("\n[+] Computer Name:", hostname)
        print("[+] Local IP Address:", local_ip)

    except Exception as e:
        print("[-] Error:", e)


def ping_test():
    host = input("Enter host to ping: ")

    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "4", host]
    else:
        command = ["ping", "-c", "4", host]

    try:
        subprocess.run(command)

    except Exception as e:
        print("[-] Ping failed:", e)


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

        choice = input("\nEnter your choice: ")

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
            print("[-] Invalid choice. Try again.")


if __name__ == "__main__":
    main()