# Storing server information using Python data types

server_name = "web-server-01"
cpu_cores = 4
memory_gb = 16.0
is_production = True

installed_services = ["nginx", "docker", "ssh"]

server_details = {
    "name": server_name,
    "cpu": cpu_cores,
    "memory": memory_gb,
    "production": is_production,
    "services": installed_services
}

print("Server Details:")

for key, value in server_details.items():
    print(f"{key}: {value}")
