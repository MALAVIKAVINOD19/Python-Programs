import json
import os
try:
    # Get path of logs.json in the same folder
    file_path = os.path.join(os.path.dirname(__file__), "logs.json")

    with open(file_path, "r") as file:
        logs = json.load(file)

    info_count = 0
    warning_count = 0
    error_count = 0
    print("\n===== Log Records =====\n")

    for log in logs:
        print("Timestamp :", log["timestamp"])
        print("Level     :", log["level"])
        print("Message   :", log["message"])
        print("-" * 30)

        if log["level"] == "INFO":
            info_count += 1
        elif log["level"] == "WARNING":
            warning_count += 1
        elif log["level"] == "ERROR":
            error_count += 1
    print("\n===== Log Summary =====")
    print("INFO Messages    :", info_count)
    print("WARNING Messages :", warning_count)
    print("ERROR Messages   :", error_count)

except FileNotFoundError:
    print("Error: logs.json file not found.")

except json.JSONDecodeError:
    print("Error: Invalid JSON data.")
    