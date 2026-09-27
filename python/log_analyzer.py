error_count = 0
warning_count = 0
can_error_count = 0
sensor_timeout_count = 0

with open("device_log.txt", "r") as file:
    for line in file:
        line = line.strip()

        if "ERROR" in line:
            error_count += 1

        if "WARNING" in line:
            warning_count += 1

        if "CAN" in line and "ERROR" in line:
            can_error_count += 1
            print("CAN Error:", line)

        if "Sensor timeout" in line:
            sensor_timeout_count += 1
            print("Sensor Timeout:", line)

print()
print("Summary")
print("Total Errors:", error_count)
print("Total Warnings:", warning_count)
print("CAN Errors:", can_error_count)
print("Sensor Timeouts:", sensor_timeout_count)
