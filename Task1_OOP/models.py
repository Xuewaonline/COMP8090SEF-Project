"""
models.py - Abstract Base Classes and Item Models
COMP8090SEF - Task 1 OOP Application: Library Management System
Student: HE Xue (SID: 13927408)

This module demonstrates:
- Abstraction (ABC, abstract methods)
- Inheritance (Item -> Book, Magazine, DVD)
- Encapsulation (private attributes with property decorators)
- Polymorphism (method overriding, __str__)
- Magic/Dunder methods (__str__, __repr__, __eq__, __lt__, __hash__)
- Static methods and Class methods
1
"""

from abc import ABC, abstractmethod
from datetime import datetime


class LibraryItem(ABC):
    """
    Abstract base class for all library items.

    Demonstrates:
    - Abstraction: Cannot instantiate directly, must be subclassed.
    - Encapsulation: Private attributes with property getters/setters.
    - Magic methods: __str__, __repr__, __eq__, __lt__, __hash__.
    """

    # Class variable: tracks total items created across all types
    _total_items_created = 0

    def __init__(self, item_id, title, year):
        """
        Initialize a library item.

        Args:
            item_id (str): Unique identifier for the item
            title (str): Title of the item
            year (int): Year of publication/release
        """
        self.__item_id = item_id        # Private: cannot be changed after creation
        self.__title = title            # Private: controlled access via property
        self.__year = year              # Private
        self.__is_available = True      # Private: tracks borrow status
        self.__borrow_count = 0         # Private: tracks popularity
        LibraryItem._total_items_created += 1

    # --- Properties (Encapsulation) ---

    @property
    def item_id(self):
        """Read-only property for item ID."""
        return self.__item_id

    @property
    def title(self):
        """Get the title of the item."""
        return self.__title

    @title.setter
    def title(self, new_title):
        """Set the title with validation."""
        if not new_title or not isinstance(new_title, str):
            raise ValueError("Title must be a non-empty string.")
        self.__title = new_title

    @property
    def year(self):
        """Get the publication year."""
        return self.__year

    @property
    def is_available(self):
        """Check if the item is available for borrowing."""
        return self.__is_available

    @property
    def borrow_count(self):
        """Get how many times this item has been borrowed."""
        return self.__borrow_count

    # --- Abstract Methods (Abstraction) ---

    @abstractmethod
    def get_type(self):
        """Return the type of library item. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def get_details(self):
        """Return detailed info about the item. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def get_late_fee_per_day(self):
        """Return the daily late fee for this item type."""
        pass

    # --- Concrete Methods ---

    def borrow(self):
        """Mark the item as borrowed."""
        if not self.__is_available:
            return False
        self.__is_available = False
        self.__borrow_count += 1
        return True

    def return_item(self):
        """Mark the item as returned."""
        self.__is_available = True

    # --- Class Method ---

    @classmethod
    def get_total_items_created(cls):
        """Return the total number of items created (class method)."""
        return cls._total_items_created

    # --- Static Method ---

    @staticmethod
    def validate_year(year):
        """Validate that a year is reasonable (static method)."""
        current_year = datetime.now().year
        return isinstance(year, int) and 1000 <= year <= current_year + 1

    # --- Magic Methods (Polymorphism) ---

    def __str__(self):
        """Human-readable string representation."""
        status = "Available" if self.__is_available else "Borrowed"
        return f"[{self.get_type()}] {self.__title} ({self.__year}) - {status}"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"{self.__class__.__name__}(id={self.__item_id!r}, title={self.__title!r})"

    def __eq__(self, other):
        """Two items are equal if they have the same item_id."""
        if isinstance(other, LibraryItem):
            return self.__item_id == other.__item_id
        return False

    def __lt__(self, other):
        """Compare items by title for sorting."""
        if isinstance(other, LibraryItem):
            return self.__title.lower() < other.__title.lower()
        return NotImplemented

    def __hash__(self):
        """Hash based on item_id for use in sets and dicts."""
        return hash(self.__item_id)


class Book(LibraryItem):
    """
    Book class inheriting from LibraryItem.

    Demonstrates:
    - Single inheritance
    - Method overriding (polymorphism)
    - Additional encapsulated attributes
    """

    def __init__(self, item_id, title, year, author, isbn, pages):
        super().__init__(item_id, title, year)
        self.__author = author
        self.__isbn = isbn
        self.__pages = pages

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def pages(self):
        return self.__pages

    # Override abstract methods
    def get_type(self):
        return "Book"

    def get_details(self):
        return (f"Title: {self.title}\n"
                f"  Author: {self.__author}\n"
                f"  ISBN: {self.__isbn}\n"
                f"  Pages: {self.__pages}\n"
                f"  Year: {self.year}")

    def get_late_fee_per_day(self):
        return 1.0  # $1 per day


class Magazine(LibraryItem):
    """
    Magazine class inheriting from LibraryItem.

    Demonstrates:
    - Single inheritance
    - Method overriding with different behavior (polymorphism)
    """

    def __init__(self, item_id, title, year, issue_number, publisher):
        super().__init__(item_id, title, year)
        self.__issue_number = issue_number
        self.__publisher = publisher

    @property
    def issue_number(self):
        return self.__issue_number

    @property
    def publisher(self):
        return self.__publisher

    def get_type(self):
        return "Magazine"

    def get_details(self):
        return (f"Title: {self.title}\n"
                f"  Issue: #{self.__issue_number}\n"
                f"  Publisher: {self.__publisher}\n"
                f"  Year: {self.year}")

    def get_late_fee_per_day(self):
        return 0.5  # $0.5 per day (cheaper than books)


class DVD(LibraryItem):
    """
    DVD class inheriting from LibraryItem.

    Demonstrates:
    - Single inheritance
    - Method overriding with DVD-specific details
    """

    def __init__(self, item_id, title, year, director, duration_min):
        super().__init__(item_id, title, year)
        self.__director = director
        self.__duration_min = duration_min

    @property
    def director(self):
        return self.__director

    @property
    def duration_min(self):
        return self.__duration_min

    def get_type(self):
        return "DVD"

    def get_details(self):
        return (f"Title: {self.title}\n"
                f"  Director: {self.__director}\n"
                f"  Duration: {self.__duration_min} min\n"
                f"  Year: {self.year}")

    def get_late_fee_per_day(self):
        return 2.0  # $2 per day (most expensive)


class DigitalBook(Book):
    """
    DigitalBook inheriting from Book (multi-level inheritance).
    Represents an e-book that can be borrowed by multiple users simultaneously.

    Demonstrates:
    - Multi-level inheritance (LibraryItem -> Book -> DigitalBook)
    - Method overriding at a deeper level
    """

    def __init__(self, item_id, title, year, author, isbn, pages, file_format, file_size_mb):
        super().__init__(item_id, title, year, author, isbn, pages)
        self.__file_format = file_format    # e.g., "PDF", "EPUB"
        self.__file_size_mb = file_size_mb
        self.__max_concurrent = 3           # Up to 3 users can borrow at once
        self.__current_borrowers = 0

    @property
    def file_format(self):
        return self.__file_format

    @property
    def file_size_mb(self):
        return self.__file_size_mb

    def get_type(self):
        return "Digital Book"

    def get_details(self):
        base = super().get_details()
        return (f"{base}\n"
                f"  Format: {self.__file_format}\n"
                f"  Size: {self.__file_size_mb} MB\n"
                f"  Available copies: {self.__max_concurrent - self.__current_borrowers}/{self.__max_concurrent}")

    def borrow(self):
        """Override: digital books can be borrowed by multiple users."""
        if self.__current_borrowers >= self.__max_concurrent:
            return False
        self.__current_borrowers += 1
        return True

    def return_item(self):
        """Override: reduce concurrent borrower count."""
        if self.__current_borrowers > 0:
            self.__current_borrowers -= 1

    @property
    def is_available(self):
        """Override: available if under max concurrent borrowers."""
        return self.__current_borrowers < self.__max_concurrent

    def get_late_fee_per_day(self):
        return 0.0  # No late fee for digital books
