

try:
    total_class = int(input("Enter total classes held: "))

    if total_class <= 0:
        print("Error: Total classes must be greater than zero.")
        raise SystemExit

    attended = int(input("Enter classes attended: "))

    if attended <= 0:
        print("Error: Classes attended must be greater than zero.")
        raise SystemExit

    if attended > total_class:
        print("Error: Attended classes cannot exceed classes held.")
        raise SystemExit

    required = float(input("Enter required attendance percentage: "))

    if required <= 0 or required > 100:
        print("Error: Required percentage must be between 1 and 100.")

    else:
        attendance = (attended / total_class) * 100

        print("\n--- Attendance Report ---")
        print("Total Classes:", total_class)
        print("Classes Attended:", attended)
        print("Classes Absent:", total_class - attended)
        print("Current Attendance:", round(attendance, 2), "%")
        print("Required Attendance:", required, "%")

        if attendance >= required:
            print("Status: Your attendance is sufficient!")

        else:
            needed = 0

            while ((attended + needed) /
                   (total_class + needed)) * 100 < required:
                needed += 1

            print("Status: Attendance shortage!")
            print(
                "You must attend the next",
                needed,
                "consecutive classes without absence."
            )

except ValueError:
    print("Error: Enter a valid number.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Attendance report generated successfully.")

finally:
    print("Attendance checking process completed.")