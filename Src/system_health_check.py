import platform
import subprocess
from datetime import datetime

def get_system_info():
    return {
        "os": platform.system(),
        "os_version": platform.release(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception as error:
        return f"Error executing command: {error}"
    
def generate_report():
    system_info = get_system_info()
    report_lines = []

    report_lines.append("System Health Report")
    report_lines.append(f"Generated at: {system_info['time']}")
    report_lines.append(f"OS: {system_info['os']} {system_info['os_version']}")
    report_lines.append("-" * 30)

    if platform.system() == "Windows":
        report_lines.append("Uptime:")
        report_lines.append(run_command('systeminfo | find "System Boot Time"'))

        report_lines.append("\nDisk Usage:")
        report_lines.append(run_command("wmic logicaldisk get size,freespace,caption"))

        report_lines.append("\nMemory Usage:")
        report_lines.append(run_command('systeminfo | find "Total Physical Memory"'))
    else:
        report_lines.append("Uptime:")
        report_lines.append(run_command("uptime"))

        report_lines.append("\nDisk Usage:")
        report_lines.append(run_command("df -h"))

        report_lines.append("\nMemory Usage:")
        report_lines.append(run_command("free -h"))

    return "\n".join(report_lines)

def write_report(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
        print("System health report generated successfully.")
    except Exception as error:
        print(f"Failed to write report: {error}")

if __name__ == "__main__":
    report = generate_report()
    write_report("system_health_report.txt", report)