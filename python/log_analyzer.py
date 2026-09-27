error_count = 0
warning_count = 0

with open("device_log.txt", "r") as file:
    for line in file:
        line = line.strip()

        if "ERROR" in line:
            error_count += 1
            print("Found error:", line)

        elif "WARNING" in line:
            warning_count += 1
            print("Found warning:", line)

print()
print("Total Errors:", error_count)
print("Total Warnings:", warning_count)
