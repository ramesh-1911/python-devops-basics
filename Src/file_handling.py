servers = [{"name":"web 01", "status":"running", "cpuusage": 75},
           {"name":"db 01", "status":"stopped", "cpuusage": 0},
           {"name":"cache 01", "status":"running", "cpuusage": 55}]

with open("server_report.txt", "w") as file:
    for server in servers:
        file.write(f"server: {server['name']}\n")
        file.write(f"status: {server['status']}\n")
        file.write(f"cpu usage: {server['cpuusage']}\n")
        file.write("-" * 20 + "\n")

print("Server report has been created successfully")