def check_server_status(server):
    if server["status"] == "running":
        return f"server {server['name']}is running"
    else:
        return f"server {server['name']}is not running"

def CpuUsage(server):
    if server["cpu"] > 80:
        return f"warning: high CPU usage on server {server['name']}"
    return f"CPU usage on server {server['name']} is normal"

Servers = [
    {"name": "web 01", "status": "running", "cpu": 75},
    {"name": "db", "status": "stopped", "cpu": 90},
    {"name": "backend", "status": "running", "cpu": 45}
]

for server in Servers:
    print(check_server_status(server))
    print(CpuUsage(server))
    print("-----")
