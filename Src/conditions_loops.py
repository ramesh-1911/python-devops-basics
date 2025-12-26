Servers = [{"name" : "web 01", "status" : "running", "Memory Usage" : 70},
         {"name" : "db 01", "status" : "stopped", "Memory Usage" : 0},
         {"name" : "cache 01", "status" : "running", "Memory Usage" : 55},
         {"name" : "web 02", "status" : "running", "Memory Usage" : 80},]

for server in Servers:
    if server["status"] == "running":
        print(f"{server['name']} is running.")
        if server["Memory Usage"] >= 75:
            print(f"warning: {server['name']} has high memory usage: {server['Memory Usage']}%")
        else:
            print(f"{server['name']} memory usage is normal: {server['Memory Usage']}%")