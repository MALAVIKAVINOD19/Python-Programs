import os
print(os.getcwd())

try:
    current_folder = os.path.dirname(__file__)
    file_path = os.path.join(current_folder, "log.txt")

    with open(file_path, "r") as file:
        error_count = 0

        print("Log File Contents:\n")

        for line in file:
            print(line.strip())

            if "ERROR" in line:
                error_count += 1

        print("\nTotal number of ERROR messages:", error_count)

except FileNotFoundError:
    print("Error: log.txt file does not exist.")