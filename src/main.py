import subprocess
import time

def start_tcpdump_capture(ip_address, port, output_file):
    """
    Start capturing traffic for a specific IP address and port using tcpdump.
    
    Args:
    - ip_address (str): The IP address to monitor.
    - port (int): The port number to monitor.
    - output_file (str): The file to save the captured packets.

    Returns:
    - subprocess.Popen: The tcpdump process.
    """
    cmd = [
        "sudo",
        "tcpdump",
        "-i", "any",
        "-n",
        f"tcp port {port} and host {ip_address}",
        "-w", output_file
    ]
    
    process = subprocess.Popen(cmd)
    return process

def main():
    IP_ADDRESS = input("Enter the IP address to monitor: ")
    PORT = input("Enter the port number to monitor (e.g., 23 for telnet): ")
    OUTPUT_FILE = "traffic_capture.pcap"

    print(f"Starting tcpdump capture for IP: {IP_ADDRESS} on port {PORT}")
    tcpdump_process = start_tcpdump_capture(IP_ADDRESS, PORT, OUTPUT_FILE)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping tcpdump capture...")
        tcpdump_process.terminate()

if __name__ == "__main__":
    main()
