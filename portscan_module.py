# portscan_module.py
import socket

def port_scan(host, ports):
    try:
        open_ports = []
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1) 
                if s.connect_ex((host, port)) == 0:
                    open_ports.append(port)
        return {"host": host, "open_ports": open_ports}
    except Exception as e:
        print(f"Failed to perform port scan: {str(e)}")
        return {}

if __name__ == "__main__":
    result = port_scan("127.0.0.1", range(1, 1025))
    print(result)
