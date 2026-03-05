# Task 1: OOP-Based Application - Library Management System

**COMP8090SEF Data Structures and Algorithms**
**Student:** HE Xue (SID: 13927408)

## Description

A Library Management System built with Python that demonstrates all OOP concepts covered in the course. The system manages books, magazines, DVDs, and digital books, with member management, borrowing/returning, waitlists, and undo functionality.

## Files

| File | Description |
|------|-------------|
| `models.py` | Abstract base classes, Book/Magazine/DVD/DigitalBook classes |
| `data_structures.py` | Custom LinkedList, Stack, Queue implementations |
| `library.py` | Library system core: Member, PremiumMember, BorrowRecord, Library |
| `main.py` | Main entry point with interactive menu |

## OOP Concepts Used

| Concept | Where |
|---------|-------|
| **Abstraction** | `LibraryItem` (ABC with abstract methods) |
| **Encapsulation** | Private attributes (`__attr`) with `@property` getters/setters in all classes |
| **Inheritance** | `Book`, `Magazine`, `DVD` extend `LibraryItem`; `PremiumMember` extends `Member` |
| **Multi-level Inheritance** | `DigitalBook` extends `Book` extends `LibraryItem` |
| **Multiple Inheritance (Mixin)** | `Member` inherits from `Printable` mixin |
| **Polymorphism** | `get_type()`, `get_details()`, `get_late_fee_per_day()` overridden in each subclass |
| **Magic Methods** | `__str__`, `__repr__`, `__eq__`, `__lt__`, `__hash__`, `__len__`, `__contains__`, `__getitem__`, `__iter__`, `__bool__` |
| **Class Methods** | `LibraryItem.get_total_items_created()`, `Member.get_member_count()` |
| **Static Methods** | `LibraryItem.validate_year()`, `Member.validate_email()` |
| **Composition** | `Library` contains `LinkedList`, `Stack`, `Queue`, `Member`, `LibraryItem` objects |

## How to Run

### Prerequisites
- Python 3.7 or higher
- No external packages required

### Run the Application
```bash
cd Task1_OOP
python main.py
```

### Quick Demo
After launching, enter `17` to run the full demo scenario, which demonstrates all features automatically.

### Interactive Menu
The menu provides 17 options including:
- Browse and search library items
- Add/remove items
- Register members (Standard/Premium)
- Borrow and return items (with waitlist and late fees)
- View borrow history
- Undo operations
- Library statistics

## Video Link
[Your YouTube/Bilibili Link]
