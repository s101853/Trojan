import psutil

def network_info():
    try:
        network_info = {
            "bytes_sent": psutil.net_io_counters().bytes_sent,
            "bytes_recv": psutil.net_io_counters().bytes_recv,
            "packets_sent": psutil.net_io_counters().packets_sent,
            "packets_recv": psutil.net_io_counters().packets_recv,
            # Add more network info as needed
        }
        
        # Print or send the network info as desired
        print("Network Information:")
        print(network_info)
    except Exception as e:
        print(f"Failed to retrieve network information: {str(e)}")

# You may need to install psutil first:
# pip install psutil
