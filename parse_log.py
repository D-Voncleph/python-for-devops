with open("application.log", "r") as log_file:
    for line in log_file:
        if "ERROR" in line:
            print(line)