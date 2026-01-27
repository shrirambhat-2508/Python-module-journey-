import calendar
calendar.setfirstweekday(calendar.SUNDAY)

while True:  # Main loop to allow restart
    # Simple instructions shown to the user
    print(f"""
{"="*10}Welcome to Calendar Generator!{"="*10}

Instructions:
- Enter the year as a number, e.g., 2026
- Type 'year' to see the full year or 'month' to see a single month
- If you choose 'month', enter the month number (1-12)
""")

    # Ask for year safely
    while True:
        try:
            year = int(input("Enter a year (e.g., 2026): "))
            break
        except ValueError:
            print("Please enter a valid number!")

    # Ask for full year or single month
    while True:
        choice = input("Full year or single month? (year/month): ").lower()
        if choice in ('year', 'month'):
            break
        print("Please type 'year' or 'month'.")

    # Show calendar
    if choice == "year":
        print(f"\n{"="*50}{"\n" + calendar.calendar(year)}{"="*50}")
    else:
        while True:
            try:
                month = int(input("Enter month number (1-12): "))
                if 1 <= month <= 12:
                    break
                else:
                    print("Month must be between 1 and 12!")
            except ValueError:
                print("Please enter a valid number!")
        print(f"{"="*20}{"\n" + calendar.month(year, month)}{"="*20}")

    # Restart or exit
    restart = input("\nDo you want to generate another calendar? (yes/no): ").lower()
    if restart != "yes":
        print(f"\n{"="*10}Thanks for using Calendar Generator.{"="*10}")
        break
