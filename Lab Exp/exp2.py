import socket

target = input("Enter authorized target IP or hostname: ").strip()
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

if not (1 <= start_port <= end_port <= 65535):
    raise ValueError("Ports must be between 1 and 65535, with start <= end.")

print(f"\nScanning {target} from port {start_port} to {end_port}")
for port in range(start_port, end_port + 1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.4)
        try:
            if sock.connect_ex((target, port)) == 0:
                print(f"Port {port}: OPEN")
        except socket.gaierror:
            print("Could not resolve target hostname.")
            break
        except OSError as error:
            print(f"Port {port}: scan error ({error})")
print("Scan completed. Scan only systems you are authorized to assess.")
