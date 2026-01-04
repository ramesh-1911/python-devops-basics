def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print (content)
    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except PermissionError:
        print(f"Error: Permission denied for {filename}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")

read_file("server_report.txt")