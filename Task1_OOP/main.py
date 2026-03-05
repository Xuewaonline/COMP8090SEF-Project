"""
main.py - Main Application Entry Point
COMP8090SEF - Task 1 OOP Application: Library Management System
Student: HE Xue (SID: 13927408)

This module provides a menu-driven interface for the Library Management System.
It demonstrates the usage of all OOP concepts through a real-life application.

How to run:
    python main.py

The system will pre-load sample data and present an interactive menu.
"""

from models import Book, Magazine, DVD, DigitalBook, LibraryItem
from data_structures import LinkedList, Stack, Queue
from library import Library, Member, PremiumMember


def load_sample_data(lib):
    """
    Pre-load the library with sample items and members for demonstration.
    This makes it easy to test all features without manual data entry.
    """
    print("\n  Loading sample data...")
    print("  " + "-" * 40)

    # Add Books
    lib.add_item(Book("B001", "Python Crash Course", 2023, "Eric Matthes", "978-1593279288", 544))
    lib.add_item(Book("B002", "Clean Code", 2008, "Robert C. Martin", "978-0132350884", 464))
    lib.add_item(Book("B003", "Data Structures Using Python", 2021, "Rance Necaise", "978-0470618295", 520))
    lib.add_item(Book("B004", "Introduction to Algorithms", 2009, "Thomas Cormen", "978-0262033848", 1312))

    # Add Magazines
    lib.add_item(Magazine("M001", "National Geographic", 2024, 256, "National Geographic Society"))
    lib.add_item(Magazine("M002", "Scientific American", 2024, 198, "Springer Nature"))

    # Add DVDs
    lib.add_item(DVD("D001", "The Matrix", 1999, "Wachowskis", 136))
    lib.add_item(DVD("D002", "Inception", 2010, "Christopher Nolan", 148))

    # Add Digital Book (multi-level inheritance demo)
    lib.add_item(DigitalBook("E001", "Learning Python", 2024, "Mark Lutz",
                             "978-1449355739", 1648, "PDF", 25.3))

    # Add Members
    lib.add_member(Member("STU001", "Alice Wong", "alice@hkmu.edu.hk"))
    lib.add_member(Member("STU002", "Bob Chen", "bob@hkmu.edu.hk"))
    lib.add_member(PremiumMember("STU003", "Charlie Li", "charlie@hkmu.edu.hk"))

    print("  " + "-" * 40)
    print("  Sample data loaded successfully!\n")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("  LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("  1.  List all items")
    print("  2.  List available items")
    print("  3.  Search items by keyword")
    print("  4.  View item details")
    print("  5.  Add a new book")
    print("  6.  Remove an item")
    print("  7.  List all members")
    print("  8.  View member info")
    print("  9.  Register new member")
    print("  10. Borrow an item")
    print("  11. Return an item")
    print("  12. View borrow history")
    print("  13. View member history")
    print("  14. View waitlist")
    print("  15. Undo last action")
    print("  16. Library statistics")
    print("  17. Run demo scenario")
    print("  0.  Exit")
    print("=" * 50)


def run_demo_scenario(lib):
    """
    Run a complete demo scenario showing all features.
    This demonstrates the system workflow without manual input.
    """
    print("\n" + "#" * 60)
    print("  RUNNING DEMO SCENARIO")
    print("#" * 60)

    # 1. Show all items
    print("\n--- Step 1: View all library items ---")
    lib.list_all_items()

    # 2. Show available items
    print("\n--- Step 2: View available items ---")
    lib.list_available_items()

    # 3. Search
    print("\n--- Step 3: Search for 'Python' ---")
    results = lib.search_items("Python")
    for item in results:
        print(f"  Found: {item}")

    # 4. View item details (polymorphism in action)
    print("\n--- Step 4: View item details (Polymorphism Demo) ---")
    for item_id in ["B001", "M001", "D001", "E001"]:
        item = lib.get_item(item_id)
        if item:
            print(f"\n  [{item.get_type()}]")
            print(f"  {item.get_details()}")
            print(f"  Late fee per day: ${item.get_late_fee_per_day():.2f}")

    # 5. Member info (multiple inheritance demo)
    print("\n--- Step 5: Member Info (Inheritance Demo) ---")
    for mid in ["STU001", "STU003"]:
        member = lib.get_member(mid)
        if member:
            member.display_info()  # Uses Printable mixin

    # 6. Borrow items
    print("\n--- Step 6: Borrow Items ---")
    lib.borrow_item("STU001", "B001")  # Alice borrows Python Crash Course
    lib.borrow_item("STU002", "B001")  # Bob tries to borrow same book -> waitlist
    lib.borrow_item("STU002", "D001")  # Bob borrows The Matrix
    lib.borrow_item("STU003", "E001")  # Charlie borrows digital book
    lib.borrow_item("STU001", "E001")  # Alice also borrows same digital book (allowed!)

    # 7. Check status after borrows
    print("\n--- Step 7: Items After Borrowing ---")
    lib.list_all_items()

    # 8. View borrow history (LinkedList traversal)
    print("\n--- Step 8: Borrow History (LinkedList) ---")
    lib.view_borrow_history()

    # 9. Return an item
    print("\n--- Step 9: Return Items ---")
    lib.return_item("STU001", "B001")  # Alice returns -> Bob gets notified

    # 10. View waitlist
    print("\n--- Step 10: View Waitlist ---")
    lib.view_waitlist("B001")

    # 11. Undo last action
    print("\n--- Step 11: Undo Last Action (Stack) ---")
    lib.undo_last_action()

    # 12. Statistics
    print("\n--- Step 12: Library Statistics ---")
    lib.get_statistics()

    # 13. Demonstrate magic methods
    print("\n--- Step 13: Magic Methods Demo ---")
    b1 = lib.get_item("B001")
    b2 = lib.get_item("B002")
    if b1 and b2:
        print(f"  str(b1):  {str(b1)}")
        print(f"  repr(b1): {repr(b1)}")
        print(f"  b1 == b2: {b1 == b2}")
        print(f"  b1 < b2:  {b1 < b2} (compared by title)")

    # 14. Class method and static method demo
    print("\n--- Step 14: Class & Static Methods ---")
    print(f"  Total items created (class method): {LibraryItem.get_total_items_created()}")
    print(f"  Total members created (class method): {Member.get_member_count()}")
    print(f"  Validate year 2024 (static method): {LibraryItem.validate_year(2024)}")
    print(f"  Validate year 3000 (static method): {LibraryItem.validate_year(3000)}")
    print(f"  Validate email (static method): {Member.validate_email('test@hkmu.edu.hk')}")

    # 15. Data structure demo
    print("\n--- Step 15: Custom Data Structures Demo ---")
    print("  LinkedList (borrow history):")
    print(f"    Length: {len(lib._Library__borrow_history)}")

    # Stack demo
    s = Stack()
    s.push("Action 1")
    s.push("Action 2")
    s.push("Action 3")
    print(f"\n  Stack demo: {s}")
    print(f"    Pop: {s.pop()}")
    print(f"    After pop: {s}")

    # Queue demo
    q = Queue()
    q.enqueue("Person A")
    q.enqueue("Person B")
    q.enqueue("Person C")
    print(f"\n  Queue demo: {q}")
    print(f"    Dequeue: {q.dequeue()}")
    print(f"    After dequeue: {q}")

    print("\n" + "#" * 60)
    print("  DEMO SCENARIO COMPLETED")
    print("#" * 60)


def main():
    """Main application loop with menu-driven interface."""
    print("\n" + "*" * 60)
    print("  COMP8090SEF - Library Management System")
    print("  Student: HE Xue (SID: 13927408)")
    print("  An OOP-based Python Application")
    print("*" * 60)

    # Initialize library
    lib = Library("HKMU Central Library")
    load_sample_data(lib)

    while True:
        display_menu()
        choice = input("\n  Enter your choice (0-17): ").strip()

        if choice == "0":
            print("\n  Thank you for using the Library Management System!")
            print("  Goodbye!\n")
            break

        elif choice == "1":
            lib.list_all_items()

        elif choice == "2":
            lib.list_available_items()

        elif choice == "3":
            keyword = input("  Enter search keyword: ").strip()
            results = lib.search_items(keyword)
            if results:
                print(f"\n  Found {len(results)} result(s):")
                for item in results:
                    print(f"    {item}")
            else:
                print("  No items found.")

        elif choice == "4":
            item_id = input("  Enter item ID: ").strip()
            item = lib.get_item(item_id)
            if item:
                print(f"\n  {item.get_details()}")
                print(f"  Status: {'Available' if item.is_available else 'Borrowed'}")
                print(f"  Late fee: ${item.get_late_fee_per_day():.2f}/day")
            else:
                print("  Item not found.")

        elif choice == "5":
            print("\n  Add a new book:")
            item_id = input("    Item ID: ").strip()
            title = input("    Title: ").strip()
            year = int(input("    Year: ").strip())
            author = input("    Author: ").strip()
            isbn = input("    ISBN: ").strip()
            pages = int(input("    Pages: ").strip())
            book = Book(item_id, title, year, author, isbn, pages)
            lib.add_item(book)

        elif choice == "6":
            item_id = input("  Enter item ID to remove: ").strip()
            lib.remove_item(item_id)

        elif choice == "7":
            lib.list_all_members()

        elif choice == "8":
            member_id = input("  Enter member ID: ").strip()
            member = lib.get_member(member_id)
            if member:
                member.display_info()
            else:
                print("  Member not found.")

        elif choice == "9":
            print("\n  Register new member:")
            member_id = input("    Member ID: ").strip()
            name = input("    Name: ").strip()
            email = input("    Email: ").strip()
            mtype = input("    Type (1=Standard, 2=Premium): ").strip()
            if mtype == "2":
                member = PremiumMember(member_id, name, email)
            else:
                member = Member(member_id, name, email)
            lib.add_member(member)

        elif choice == "10":
            member_id = input("  Enter member ID: ").strip()
            item_id = input("  Enter item ID to borrow: ").strip()
            lib.borrow_item(member_id, item_id)

        elif choice == "11":
            member_id = input("  Enter member ID: ").strip()
            item_id = input("  Enter item ID to return: ").strip()
            lib.return_item(member_id, item_id)

        elif choice == "12":
            lib.view_borrow_history()

        elif choice == "13":
            member_id = input("  Enter member ID: ").strip()
            lib.view_member_history(member_id)

        elif choice == "14":
            item_id = input("  Enter item ID: ").strip()
            lib.view_waitlist(item_id)

        elif choice == "15":
            lib.undo_last_action()

        elif choice == "16":
            lib.get_statistics()

        elif choice == "17":
            run_demo_scenario(lib)

        else:
            print("  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
