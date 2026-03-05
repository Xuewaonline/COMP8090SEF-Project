"""
library.py - Library System Core Logic
COMP8090SEF - Task 1 OOP Application: Library Management System
Student: HE Xue (SID: 13927408)

This module contains:
- Member class: Represents a library member
- BorrowRecord class: Tracks a borrowing transaction
- Library class: Main system that manages items, members, and operations

Demonstrates:
- Composition (Library has Members, Items, data structures)
- Multiple inheritance (PremiumMember inherits Member + Printable mixin)
- Encapsulation, properties, class methods, static methods
- Use of custom data structures (LinkedList, Stack, Queue)
"""

from datetime import datetime, timedelta
from models import LibraryItem, Book, Magazine, DVD, DigitalBook
from data_structures import LinkedList, Stack, Queue


class Printable:
    """
    Mixin class providing formatted display capability.
    Demonstrates: Multiple inheritance (mixin pattern).
    """

    def display_info(self):
        """Print formatted information. Subclasses should override _get_info_lines()."""
        print("\n  " + "-" * 40)
        for line in self._get_info_lines():
            print(f"  {line}")
        print("  " + "-" * 40)

    def _get_info_lines(self):
        """Override in subclasses to provide info lines."""
        return [str(self)]


class Member(Printable):
    """
    Represents a library member.

    Demonstrates:
    - Inheritance from Printable mixin
    - Encapsulation (private attributes)
    - Properties with validation
    """

    _member_count = 0  # Class variable

    def __init__(self, member_id, name, email):
        self.__member_id = member_id
        self.__name = name
        self.__email = email
        self.__borrowed_items = []  # List of item_ids currently borrowed
        self.__join_date = datetime.now()
        self.__max_borrow_limit = 5
        Member._member_count += 1

    @property
    def member_id(self):
        return self.__member_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string.")
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address.")
        self.__email = value

    @property
    def borrowed_items(self):
        return list(self.__borrowed_items)  # Return a copy

    @property
    def max_borrow_limit(self):
        return self.__max_borrow_limit

    @property
    def join_date(self):
        return self.__join_date

    def can_borrow(self):
        """Check if member can borrow more items."""
        return len(self.__borrowed_items) < self.__max_borrow_limit

    def add_borrowed_item(self, item_id):
        """Add an item to the member's borrowed list."""
        self.__borrowed_items.append(item_id)

    def remove_borrowed_item(self, item_id):
        """Remove an item from the member's borrowed list."""
        if item_id in self.__borrowed_items:
            self.__borrowed_items.remove(item_id)

    def _get_info_lines(self):
        """Override from Printable mixin."""
        return [
            f"Member ID: {self.__member_id}",
            f"Name: {self.__name}",
            f"Email: {self.__email}",
            f"Type: Standard",
            f"Items borrowed: {len(self.__borrowed_items)}/{self.__max_borrow_limit}",
            f"Joined: {self.__join_date.strftime('%Y-%m-%d')}",
        ]

    @classmethod
    def get_member_count(cls):
        """Return total number of members created."""
        return cls._member_count

    @staticmethod
    def validate_email(email):
        """Static method to validate email format."""
        return isinstance(email, str) and "@" in email and "." in email

    def __str__(self):
        return f"Member({self.__member_id}: {self.__name})"

    def __repr__(self):
        return f"Member(id={self.__member_id!r}, name={self.__name!r})"

    def __eq__(self, other):
        if isinstance(other, Member):
            return self.__member_id == other.__member_id
        return False

    def __hash__(self):
        return hash(self.__member_id)


class PremiumMember(Member):
    """
    Premium member with extended borrowing privileges.

    Demonstrates:
    - Inheritance (from Member)
    - Multiple inheritance (Member already inherits Printable)
    - Method overriding
    """

    def __init__(self, member_id, name, email):
        super().__init__(member_id, name, email)
        self.__max_borrow_limit = 10  # Premium members can borrow more
        self.__discount_rate = 0.5    # 50% discount on late fees

    @property
    def max_borrow_limit(self):
        return self.__max_borrow_limit

    @property
    def discount_rate(self):
        return self.__discount_rate

    def can_borrow(self):
        """Override: premium members have higher limit."""
        return len(self.borrowed_items) < self.__max_borrow_limit

    def _get_info_lines(self):
        """Override to show premium status."""
        base = super()._get_info_lines()
        # Replace type line
        base = [line.replace("Type: Standard", "Type: Premium") for line in base]
        base.append(f"Late fee discount: {int(self.__discount_rate * 100)}%")
        return base

    def __str__(self):
        return f"PremiumMember({self.member_id}: {self.name})"


class BorrowRecord:
    """
    Represents a single borrow/return transaction.

    Demonstrates:
    - Encapsulation
    - Operator overloading (__str__, __lt__)
    """

    def __init__(self, member_id, item_id, item_title):
        self.__member_id = member_id
        self.__item_id = item_id
        self.__item_title = item_title
        self.__borrow_date = datetime.now()
        self.__due_date = self.__borrow_date + timedelta(days=14)  # 14-day loan
        self.__return_date = None
        self.__late_fee = 0.0

    @property
    def member_id(self):
        return self.__member_id

    @property
    def item_id(self):
        return self.__item_id

    @property
    def borrow_date(self):
        return self.__borrow_date

    @property
    def due_date(self):
        return self.__due_date

    @property
    def return_date(self):
        return self.__return_date

    @property
    def late_fee(self):
        return self.__late_fee

    @property
    def is_returned(self):
        return self.__return_date is not None

    def process_return(self, fee_per_day=1.0):
        """
        Process the return of the item. Calculate late fee if overdue.
        Returns the late fee amount.
        """
        self.__return_date = datetime.now()
        if self.__return_date > self.__due_date:
            days_late = (self.__return_date - self.__due_date).days
            self.__late_fee = days_late * fee_per_day
        return self.__late_fee

    def __str__(self):
        status = "Returned" if self.__return_date else "Active"
        return (f"[{status}] '{self.__item_title}' "
                f"(Borrowed: {self.__borrow_date.strftime('%Y-%m-%d')}, "
                f"Due: {self.__due_date.strftime('%Y-%m-%d')})")

    def __lt__(self, other):
        """Compare by borrow date for sorting."""
        if isinstance(other, BorrowRecord):
            return self.__borrow_date < other.__borrow_date
        return NotImplemented


class Library:
    """
    Main Library Management System.

    Demonstrates:
    - Composition (contains Members, Items, data structures)
    - Use of custom LinkedList, Stack, Queue
    - Encapsulation of complex state
    """

    def __init__(self, name):
        self.__name = name
        self.__items = {}           # {item_id: LibraryItem}
        self.__members = {}         # {member_id: Member}
        self.__borrow_history = LinkedList()  # All borrow records
        self.__undo_stack = Stack()           # For undo operations
        self.__waitlists = {}       # {item_id: Queue of member_ids}

    @property
    def name(self):
        return self.__name

    # --- Item Management ---

    def add_item(self, item):
        """Add a library item to the collection."""
        if not isinstance(item, LibraryItem):
            print("  Error: Only LibraryItem objects can be added.")
            return False
        if item.item_id in self.__items:
            print(f"  Error: Item '{item.item_id}' already exists.")
            return False
        self.__items[item.item_id] = item
        self.__undo_stack.push(("add_item", item.item_id))
        print(f"  Added: {item}")
        return True

    def remove_item(self, item_id):
        """Remove an item from the library."""
        if item_id not in self.__items:
            print(f"  Error: Item '{item_id}' not found.")
            return False
        item = self.__items.pop(item_id)
        self.__undo_stack.push(("remove_item", item))
        print(f"  Removed: {item}")
        return True

    def get_item(self, item_id):
        """Get an item by ID."""
        return self.__items.get(item_id)

    def search_items(self, keyword):
        """Search items by title keyword (case-insensitive)."""
        keyword_lower = keyword.lower()
        results = [
            item for item in self.__items.values()
            if keyword_lower in item.title.lower()
        ]
        return sorted(results)  # Uses __lt__ for sorting

    def list_all_items(self):
        """List all items in the library."""
        if not self.__items:
            print("  No items in the library.")
            return
        print(f"\n  {'ID':<10} {'Type':<15} {'Title':<30} {'Status':<12}")
        print(f"  {'-'*67}")
        for item in sorted(self.__items.values()):
            status = "Available" if item.is_available else "Borrowed"
            print(f"  {item.item_id:<10} {item.get_type():<15} {item.title:<30} {status:<12}")

    def list_available_items(self):
        """List only available items."""
        available = [item for item in self.__items.values() if item.is_available]
        if not available:
            print("  No items available.")
            return
        print(f"\n  Available items ({len(available)}):")
        for item in sorted(available):
            print(f"    {item}")

    # --- Member Management ---

    def add_member(self, member):
        """Register a new member."""
        if not isinstance(member, Member):
            print("  Error: Only Member objects can be added.")
            return False
        if member.member_id in self.__members:
            print(f"  Error: Member '{member.member_id}' already exists.")
            return False
        self.__members[member.member_id] = member
        print(f"  Registered: {member}")
        return True

    def get_member(self, member_id):
        """Get a member by ID."""
        return self.__members.get(member_id)

    def list_all_members(self):
        """List all registered members."""
        if not self.__members:
            print("  No members registered.")
            return
        print(f"\n  {'ID':<10} {'Name':<20} {'Email':<30} {'Borrowed'}")
        print(f"  {'-'*70}")
        for m in self.__members.values():
            print(f"  {m.member_id:<10} {m.name:<20} {m.email:<30} {len(m.borrowed_items)}")

    # --- Borrow / Return Operations ---

    def borrow_item(self, member_id, item_id):
        """
        Process a borrow request.
        Returns True if successful, False otherwise.
        """
        member = self.__members.get(member_id)
        item = self.__items.get(item_id)

        if not member:
            print(f"  Error: Member '{member_id}' not found.")
            return False
        if not item:
            print(f"  Error: Item '{item_id}' not found.")
            return False
        if not member.can_borrow():
            print(f"  Error: {member.name} has reached the borrowing limit.")
            return False
        if not item.is_available:
            # Add to waitlist
            if item_id not in self.__waitlists:
                self.__waitlists[item_id] = Queue()
            if member_id not in self.__waitlists[item_id]:
                self.__waitlists[item_id].enqueue(member_id)
                print(f"  '{item.title}' is not available. {member.name} added to waitlist "
                      f"(position: {len(self.__waitlists[item_id])}).")
            else:
                print(f"  {member.name} is already on the waitlist for '{item.title}'.")
            return False

        # Process borrow
        item.borrow()
        member.add_borrowed_item(item_id)
        record = BorrowRecord(member_id, item_id, item.title)
        self.__borrow_history.append(record)
        self.__undo_stack.push(("borrow", member_id, item_id))

        print(f"  Success: {member.name} borrowed '{item.title}'.")
        print(f"  Due date: {record.due_date.strftime('%Y-%m-%d')}")
        return True

    def return_item(self, member_id, item_id):
        """
        Process a return.
        Returns the late fee amount (0 if on time).
        """
        member = self.__members.get(member_id)
        item = self.__items.get(item_id)

        if not member:
            print(f"  Error: Member '{member_id}' not found.")
            return 0
        if not item:
            print(f"  Error: Item '{item_id}' not found.")
            return 0
        if item_id not in member.borrowed_items:
            print(f"  Error: {member.name} did not borrow '{item.title}'.")
            return 0

        # Find the active borrow record
        fee = 0
        for record in self.__borrow_history:
            if (record.item_id == item_id and
                    record.member_id == member_id and
                    not record.is_returned):
                fee = record.process_return(item.get_late_fee_per_day())
                break

        item.return_item()
        member.remove_borrowed_item(item_id)
        self.__undo_stack.push(("return", member_id, item_id))

        print(f"  Success: {member.name} returned '{item.title}'.")
        if fee > 0:
            # Apply discount for premium members
            if isinstance(member, PremiumMember):
                fee *= (1 - member.discount_rate)
                print(f"  Late fee (with premium discount): ${fee:.2f}")
            else:
                print(f"  Late fee: ${fee:.2f}")
        else:
            print(f"  Returned on time. No late fee.")

        # Notify next person on waitlist
        if item_id in self.__waitlists and not self.__waitlists[item_id].is_empty():
            next_member_id = self.__waitlists[item_id].dequeue()
            next_member = self.__members.get(next_member_id)
            if next_member:
                print(f"  Notification: '{item.title}' is now available for {next_member.name}!")

        return fee

    # --- History & Undo ---

    def view_borrow_history(self):
        """Display all borrow records using LinkedList traversal."""
        if self.__borrow_history.is_empty():
            print("  No borrow history.")
            return
        print("\n  Borrow History:")
        for i, record in enumerate(self.__borrow_history, 1):
            print(f"    {i}. {record}")

    def view_member_history(self, member_id):
        """View borrow history for a specific member."""
        member = self.__members.get(member_id)
        if not member:
            print(f"  Error: Member '{member_id}' not found.")
            return
        print(f"\n  History for {member.name}:")
        count = 0
        for record in self.__borrow_history:
            if record.member_id == member_id:
                count += 1
                print(f"    {count}. {record}")
        if count == 0:
            print("    No records found.")

    def undo_last_action(self):
        """Undo the last action using the Stack."""
        if self.__undo_stack.is_empty():
            print("  Nothing to undo.")
            return
        action = self.__undo_stack.pop()
        action_type = action[0]

        if action_type == "add_item":
            item_id = action[1]
            if item_id in self.__items:
                del self.__items[item_id]
                print(f"  Undo: Removed item '{item_id}'.")
        elif action_type == "remove_item":
            item = action[1]
            self.__items[item.item_id] = item
            print(f"  Undo: Restored item '{item.title}'.")
        elif action_type == "borrow":
            member_id, item_id = action[1], action[2]
            item = self.__items.get(item_id)
            member = self.__members.get(member_id)
            if item and member:
                item.return_item()
                member.remove_borrowed_item(item_id)
                print(f"  Undo: Returned '{item.title}' from {member.name}.")
        elif action_type == "return":
            member_id, item_id = action[1], action[2]
            item = self.__items.get(item_id)
            member = self.__members.get(member_id)
            if item and member:
                item.borrow()
                member.add_borrowed_item(item_id)
                print(f"  Undo: Re-borrowed '{item.title}' for {member.name}.")
        else:
            print(f"  Undo: Unknown action type '{action_type}'.")

    # --- Waitlist ---

    def view_waitlist(self, item_id):
        """View the waitlist for a specific item."""
        item = self.__items.get(item_id)
        if not item:
            print(f"  Error: Item '{item_id}' not found.")
            return
        if item_id not in self.__waitlists or self.__waitlists[item_id].is_empty():
            print(f"  No waitlist for '{item.title}'.")
            return
        print(f"\n  Waitlist for '{item.title}':")
        for i, mid in enumerate(self.__waitlists[item_id], 1):
            member = self.__members.get(mid)
            name = member.name if member else mid
            print(f"    {i}. {name}")

    # --- Statistics ---

    def get_statistics(self):
        """Display library statistics."""
        total_items = len(self.__items)
        available = sum(1 for item in self.__items.values() if item.is_available)
        borrowed = total_items - available
        total_members = len(self.__members)
        total_records = len(self.__borrow_history)

        print(f"\n  Library: {self.__name}")
        print(f"  {'='*40}")
        print(f"  Total items:      {total_items}")
        print(f"  Available:        {available}")
        print(f"  Borrowed:         {borrowed}")
        print(f"  Total members:    {total_members}")
        print(f"  Borrow records:   {total_records}")
        print(f"  Undo stack size:  {len(self.__undo_stack)}")

    def __str__(self):
        return f"Library('{self.__name}', items={len(self.__items)}, members={len(self.__members)})"
