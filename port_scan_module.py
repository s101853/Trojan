def port_scan():
    target = "localhost"  
    port_range = (1, 1024)
    open_ports = []
    
    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
    
    return {"target": target, "open_ports": open_ports}
