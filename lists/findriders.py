riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ("(1) Reserve place in line.\n"  # Add rider to line
        "(2) Reserve place in VIP line.\n"  # Add VIP
        "(3) Dispatch riders.\n"  # Dispatch next ride car
        "(4) Find rider.\n"  # Find a rider's current position in line
        "(5) Remove rider.\n"  # Remove a rider from the line
        "(6) Print riders.\n"
        "(7) Exit.\n\n")

user_input = input(menu).strip().lower()

while user_input != "7":
    if user_input == "1":  # Add rider
        name = input("Enter name: ").strip().lower()
        print(name)
        line.append(name)

    elif user_input == "2":  # Add VIP
        print("Add new VIP")
        name = input("Enter name: ").strip().lower()
        print(name)
        # Add new rider behind last VIP in line
        line.insert(num_vips, name)
        # Don't forget to increment num_vips.
        num_vips += 1

    elif user_input == "3":  # Dispatch ride
        print(f"{line[0]} is now on the ride")
        # Remove last riders_per_ride from front of line.
        line.pop(0)
        # Don't forget to decrease num_vips, if necessary.
        if num_vips > 0:
            num_vips -= 1

    elif user_input == "4":  # Find a rider's current position in line
        name = input("Enter name to find: ").strip().lower()
        if name in line:
            print(f"{name} is in line at position {str(line.index(name))}")
        else:
            print(f"{name} is not in line")

    elif user_input == "5":  # Remove a rider from the line
        name = input("Enter name to remove: ").strip().lower()
        if name in line:
            num = line.index(name)
            if num < num_vips:
                num_vips -= 1
            line.remove(name)
            print(f"{name} was removed from the line")
        else:
            print(f"{name} was not in line")

    elif user_input == "6":  # Print riders waiting in line
        print(f"{len(line)} person(s) waiting: {line}")

    else:
        print("Unknown menu option")

    user_input = input("Enter command: ").strip().lower()
    print(user_input)