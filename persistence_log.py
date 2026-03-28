"""
Team Daily Status System
"""

import os

DATABASE_FILE = "database.txt"


def show_menu():
    """Display the main menu options"""
    print("\n" + "=" * 40)
    print("TEAM DAILY STATUS SYSTEM")
    print("=" * 40)
    print("1. Add a new daily blocker")
    print("2. View all blockers")
    print("3. Clear all blockers")
    print("4. Exit")
    print("-" * 40)


def add_blocker():
    """
    Step 2: Persistent creation using append mode (a)
    """
    try:
        blocker = input("\nWhat is your daily blocker? ").strip()

        if not blocker:
            print("✗ Blocker cannot be empty.")
            return

        # Using append mode ensures persistence without overwriting previous data
        with open(DATABASE_FILE, "a", encoding="utf-8") as file:
            file.write(blocker + "\n")

        print(f"✓ Blocker saved successfully: '{blocker}'")

    except Exception as e:
        print(f"✗ Error saving blocker: {e}")


def view_blockers():
    """
    Step 3: Read operation using 'r'
    Step 4: Validation and error handling
    """
    try:
        # Validate file existence before attempting to read
        if not os.path.exists(DATABASE_FILE):
            print("\n⚠ No blockers found. File does not exist.")
            return

        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            blockers = file.readlines()

        if len(blockers) == 0:
            print("\n⚠ No blockers found. File is empty.")
            return

        print("\n" + "=" * 40)
        print("DAILY BLOCKERS")
        print("=" * 40)

        # Using enumerate for indexed display
        for i, blocker in enumerate(blockers, start=1):
            print(f"{i}. {blocker.strip()}")

        print("-" * 40)
        print(f"Total: {len(blockers)} blocker(s)")

    except Exception as e:
        print(f"✗ Unexpected error while reading: {e}")


def clear_blockers():
    """
    Demonstrates overwrite behavior using 'w' mode
    Includes safety confirmation before destructive action
    """
    try:
        if not os.path.exists(DATABASE_FILE):
            print("\n⚠ No file exists to clear.")
            return

        print("\n⚠ WARNING: This will permanently delete ALL blockers!")

        confirm = input("Type 'yes' to confirm: ").strip().lower()

        if confirm == "yes":
            # 'w' mode truncates the file (overwrite)
            with open(DATABASE_FILE, "w", encoding="utf-8") as file:
                file.write("")

            print("✓ All blockers have been cleared.")
        else:
            print("✓ Operation cancelled.")

    except Exception as e:
        print(f"✗ Error clearing blockers: {e}")


def main():
    """
    Main loop controlling program execution
    Uses a control variable instead of while True (best practice adaptation)
    """
    running = True

    print("\n✓ Welcome to Team Daily Status System")
    print("✓ Data persistence is enabled via file storage.")

    while running:
        show_menu()

        try:
            choice = input("\nSelect an option (1-4): ").strip()

            if choice == "1":
                add_blocker()
            elif choice == "2":
                view_blockers()
            elif choice == "3":
                clear_blockers()
            elif choice == "4":
                print("\n✓ Goodbye! Your data persists.\n")
                running = False
            else:
                print("✗ Invalid option. Please choose 1-4.")

        except KeyboardInterrupt:
            print("\n\n⚠ Program interrupted by user.")
            running = False
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}")


"""
===========================
STEP 5: ENGLISH PRACTICE
===========================

PROTOCOL SELECTION (3-C Rule: Clear, Concise, Courteous):

1. "I will reach out via Slack because this is an immediate blocker and requires quick team visibility."
2. "If the issue is not urgent, I will create a Jira ticket with detailed reproduction steps."
3. "For formal communication, I will send an email including logs and a clear description of the issue."

VOCABULARY INTEGRATION:

This script ensures Persistence by storing blockers in a file.
It uses Fetch operations to retrieve and display stored data.
To prevent accidental data loss, it warns users before any Overwrite action.
If an issue occurs, I would Reach out to the team using appropriate communication channels.
"""

if __name__ == "__main__":
    main()