"""
generate_report.py - Generate Task 1 PDF Report
COMP8090SEF - Task 1 OOP Application: Library Management System
Student: HE Xue (SID: 13927408)

This script generates a professional PDF report using reportlab.
Run: python generate_report.py
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import black, HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Preformatted
)
from reportlab.lib import colors

# ─── Configuration ───────────────────────────────────────────────────────────

OUTPUT_PATH = "/Users/tomzhang/Documents/xuewaonline/COMP8090SEF_DSA_Project/Task1_OOP/Task1_Report.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4  # 595.27 x 841.89 points
MARGIN = 2.54 * cm  # Normal margin: 2.54 cm all round
FONT_NAME = "Times-Roman"
FONT_NAME_BOLD = "Times-Bold"
FONT_NAME_ITALIC = "Times-Italic"
FONT_NAME_BOLD_ITALIC = "Times-BoldItalic"
FONT_SIZE = 12
LEADING = FONT_SIZE * 1.2  # Single-line spacing (1.0x leading = font_size * 1.2)


# ─── Styles ──────────────────────────────────────────────────────────────────

def create_styles():
    """Create all paragraph styles used in the report."""
    styles = getSampleStyleSheet()

    # Cover page - university name
    styles.add(ParagraphStyle(
        name='CoverUniversity',
        fontName=FONT_NAME_BOLD,
        fontSize=16,
        leading=16 * 1.4,
        alignment=TA_CENTER,
        spaceAfter=20,
    ))

    # Cover page - course code
    styles.add(ParagraphStyle(
        name='CoverCourse',
        fontName=FONT_NAME_BOLD,
        fontSize=14,
        leading=14 * 1.4,
        alignment=TA_CENTER,
        spaceAfter=6,
    ))

    # Cover page - course title lines
    styles.add(ParagraphStyle(
        name='CoverTitle',
        fontName=FONT_NAME,
        fontSize=14,
        leading=14 * 1.4,
        alignment=TA_CENTER,
        spaceAfter=6,
    ))

    # Cover page - "Self-study Report"
    styles.add(ParagraphStyle(
        name='CoverReportTitle',
        fontName=FONT_NAME_BOLD,
        fontSize=16,
        leading=16 * 1.5,
        alignment=TA_CENTER,
        spaceAfter=20,
    ))

    # Cover page - submission date
    styles.add(ParagraphStyle(
        name='CoverDate',
        fontName=FONT_NAME,
        fontSize=FONT_SIZE,
        leading=LEADING,
        alignment=TA_CENTER,
        spaceAfter=20,
    ))

    # Cover page - declaration text
    styles.add(ParagraphStyle(
        name='CoverDeclaration',
        fontName=FONT_NAME,
        fontSize=11,
        leading=11 * 1.3,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
    ))

    # Cover page - declaration item (indented)
    styles.add(ParagraphStyle(
        name='CoverDeclarationItem',
        fontName=FONT_NAME,
        fontSize=11,
        leading=11 * 1.3,
        alignment=TA_JUSTIFY,
        leftIndent=20,
        spaceAfter=4,
    ))

    # Cover page - confirmation text
    styles.add(ParagraphStyle(
        name='CoverConfirm',
        fontName=FONT_NAME,
        fontSize=11,
        leading=11 * 1.3,
        alignment=TA_JUSTIFY,
        spaceBefore=8,
        spaceAfter=16,
    ))

    # Cover page - name/SID line
    styles.add(ParagraphStyle(
        name='CoverNameSID',
        fontName=FONT_NAME_BOLD,
        fontSize=FONT_SIZE,
        leading=LEADING,
        alignment=TA_LEFT,
        spaceBefore=10,
    ))

    # Section heading (numbered, e.g. "1. Description of Core Functions")
    styles.add(ParagraphStyle(
        name='SectionHeading',
        fontName=FONT_NAME_BOLD,
        fontSize=13,
        leading=13 * 1.4,
        alignment=TA_LEFT,
        spaceBefore=14,
        spaceAfter=6,
    ))

    # Body text
    styles.add(ParagraphStyle(
        name='BodyText12',
        fontName=FONT_NAME,
        fontSize=FONT_SIZE,
        leading=LEADING,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
    ))

    # Body text with indent (for sub-items)
    styles.add(ParagraphStyle(
        name='BodyIndent',
        fontName=FONT_NAME,
        fontSize=FONT_SIZE,
        leading=LEADING,
        alignment=TA_JUSTIFY,
        leftIndent=18,
        spaceAfter=3,
    ))

    # Bullet point style
    styles.add(ParagraphStyle(
        name='BulletItem',
        fontName=FONT_NAME,
        fontSize=FONT_SIZE,
        leading=LEADING,
        alignment=TA_JUSTIFY,
        leftIndent=18,
        bulletIndent=6,
        spaceAfter=3,
    ))

    # Sub-bullet style (deeper indent)
    styles.add(ParagraphStyle(
        name='SubBullet',
        fontName=FONT_NAME,
        fontSize=FONT_SIZE,
        leading=LEADING,
        alignment=TA_JUSTIFY,
        leftIndent=36,
        bulletIndent=24,
        spaceAfter=2,
    ))

    # Code/monospace style for sample output
    styles.add(ParagraphStyle(
        name='CodeBlock',
        fontName='Courier',
        fontSize=7.5,
        leading=7.5 * 1.3,
        alignment=TA_LEFT,
        leftIndent=6,
        spaceAfter=2,
    ))

    # Appendix heading
    styles.add(ParagraphStyle(
        name='AppendixHeading',
        fontName=FONT_NAME_BOLD,
        fontSize=14,
        leading=14 * 1.4,
        alignment=TA_LEFT,
        spaceBefore=16,
        spaceAfter=8,
    ))

    # Figure caption
    styles.add(ParagraphStyle(
        name='FigureCaption',
        fontName=FONT_NAME_BOLD_ITALIC,
        fontSize=11,
        leading=11 * 1.3,
        alignment=TA_CENTER,
        spaceBefore=6,
        spaceAfter=10,
    ))

    # Reference style
    styles.add(ParagraphStyle(
        name='Reference',
        fontName=FONT_NAME,
        fontSize=FONT_SIZE,
        leading=LEADING,
        alignment=TA_LEFT,
        leftIndent=18,
        spaceAfter=3,
    ))

    return styles


# ─── Cover Page ──────────────────────────────────────────────────────────────

def build_cover_page(styles):
    """Build the cover page elements."""
    elements = []

    elements.append(Spacer(1, 40))

    # University name
    elements.append(Paragraph("Hong Kong Metropolitan University", styles['CoverUniversity']))

    elements.append(Spacer(1, 30))

    # Course code
    elements.append(Paragraph("COMP S209W/8090SEF", styles['CoverCourse']))
    elements.append(Paragraph("Data Structures, Algorithms And Problem Solving", styles['CoverTitle']))
    elements.append(Paragraph("Data Structures, Algorithms", styles['CoverTitle']))

    elements.append(Spacer(1, 40))

    # Report title
    elements.append(Paragraph("Self-study Report", styles['CoverReportTitle']))

    elements.append(Spacer(1, 20))

    # Submission date
    elements.append(Paragraph("Submission date: 9 April 2026", styles['CoverDate']))

    elements.append(Spacer(1, 20))

    # Declaration
    elements.append(Paragraph("I declare that:", styles['CoverDeclaration']))

    declaration_items = [
        "(i) I have read and checked that all parts of the project (including proposal, code programs, "
        "and reports), they are contributed by me, here submitted is original except for source material "
        "explicitly acknowledged;",

        "(ii) the project, in parts or in whole, has not been submitted for more than one purpose "
        "without declaration;",

        "(iii) I am aware of the University's policy and regulations on honesty in academic work and "
        "understand the possible consequence when breaching such policy and regulations;",

        "(iv) I confirm that I have declared in the report about the usage of AI and other generative "
        "models, including but not limited to ChatGPT, LLaMA, Gemini, Mistral, and Stable Diffusion, "
        "and complied with the instructions provided by HKMU; and",

        "(v) I am aware that I should be held responsible and liable to disciplinary actions, "
        "irrespective of whether I have signed the declaration and whether I have contributed, "
        "directly or indirectly, to the problematic contents.",
    ]

    for item_text in declaration_items:
        elements.append(Paragraph(item_text, styles['CoverDeclarationItem']))

    elements.append(Paragraph(
        "I confirm that I have read through and understood the project requirements. "
        "I understand that failure to comply with the project requirements will result in score deduction.",
        styles['CoverConfirm']
    ))

    elements.append(Spacer(1, 20))

    # Name and SID
    elements.append(Paragraph(
        "NAME: HE Xue&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SID: 13927408",
        styles['CoverNameSID']
    ))

    elements.append(PageBreak())
    return elements


# ─── Main Content (Pages 2-4) ───────────────────────────────────────────────

def build_main_content(styles):
    """Build the main content pages (text only, max 3 pages)."""
    elements = []

    # ── Section 1: Description of Core Functions ──
    elements.append(Paragraph(
        "1. Description of Core Functions and Summary of Techniques",
        styles['SectionHeading']
    ))

    elements.append(Paragraph(
        "The Library Management System is a Python-based application that manages a library's "
        "collection of books, magazines, DVDs, and digital books. It supports member registration "
        "(standard and premium memberships), item borrowing and returning with due dates and late "
        "fees, waitlist management using a queue, search functionality by title keyword, borrow "
        "history tracking, and undo operations for reversible actions.",
        styles['BodyText12']
    ))

    elements.append(Spacer(1, 4))

    elements.append(Paragraph(
        "The system is organised into four Python modules:",
        styles['BodyText12']
    ))

    modules = [
        ("<b>models.py</b>: Defines abstract base classes and the item hierarchy, including "
         "Book, Magazine, DVD, and DigitalBook. Uses the <i>abc</i> module for abstraction."),
        ("<b>data_structures.py</b>: Implements custom LinkedList, Stack, and Queue data structures "
         "with full encapsulation and magic method support."),
        ("<b>library.py</b>: Contains the core system logic, including the Library, Member, "
         "PremiumMember, BorrowRecord, and Printable mixin classes."),
        ("<b>main.py</b>: Provides an interactive menu-driven interface with 17 options and a "
         "built-in demo scenario that exercises all system features."),
    ]
    for mod in modules:
        elements.append(Paragraph(
            f"\u2022 {mod}",
            styles['BulletItem']
        ))

    elements.append(Spacer(1, 4))

    elements.append(Paragraph(
        "The following data structures are employed:",
        styles['BodyText12']
    ))

    ds_items = [
        "<b>LinkedList</b>: Stores borrow history records, enabling sequential traversal of all "
        "past transactions.",
        "<b>Stack (LIFO)</b>: Supports undo operations; each action (add, remove, borrow, return) "
        "is pushed onto the stack and can be reversed.",
        "<b>Queue (FIFO)</b>: Manages reservation waitlists for borrowed items; members are served "
        "in first-come-first-served order.",
        "<b>Dictionary</b>: Provides O(1) lookup for items and members by their unique identifiers.",
    ]
    for ds in ds_items:
        elements.append(Paragraph(f"\u2022 {ds}", styles['BulletItem']))

    # ── Section 2: Usage of OOP Concepts ──
    elements.append(Paragraph(
        "2. Usage of OOP Concepts",
        styles['SectionHeading']
    ))

    elements.append(Paragraph(
        "The system demonstrates the following OOP concepts (refer to Appendix Figure 1 for the "
        "full OOP Concepts Usage Table and Figure 2 for sample outputs):",
        styles['BodyText12']
    ))

    oop_concepts = [
        ("<b>Abstraction</b>: <i>LibraryItem</i> is an abstract base class (ABC) with three abstract "
         "methods: <i>get_type()</i>, <i>get_details()</i>, and <i>get_late_fee_per_day()</i>. It cannot "
         "be instantiated directly and forces all subclasses to provide concrete implementations."),

        ("<b>Encapsulation</b>: All classes use Python name mangling (double-underscore prefix) for private "
         "attributes, with <i>@property</i> decorators providing controlled read/write access. For example, "
         "<i>LibraryItem.__title</i> is accessed through a <i>title</i> property with a setter that validates "
         "the input is a non-empty string."),

        ("<b>Single Inheritance</b>: <i>Book</i>, <i>Magazine</i>, and <i>DVD</i> each inherit from "
         "<i>LibraryItem</i>, gaining its common attributes and methods while overriding abstract methods. "
         "<i>PremiumMember</i> inherits from <i>Member</i>."),

        ("<b>Multi-level Inheritance</b>: <i>DigitalBook</i> inherits from <i>Book</i>, which in turn "
         "inherits from <i>LibraryItem</i>, forming a three-level deep inheritance chain. "
         "<i>DigitalBook</i> adds file format, file size, and concurrent borrowing capabilities."),

        ("<b>Multiple Inheritance (Mixin)</b>: <i>Member</i> inherits from the <i>Printable</i> mixin "
         "class, gaining the <i>display_info()</i> method for formatted console output. This demonstrates "
         "the mixin pattern where a class inherits additional behaviour without being part of the main "
         "class hierarchy."),

        ("<b>Polymorphism</b>: Each subclass of <i>LibraryItem</i> overrides <i>get_type()</i>, "
         "<i>get_details()</i>, and <i>get_late_fee_per_day()</i> differently. <i>DigitalBook</i> also "
         "overrides <i>borrow()</i> to allow concurrent borrowing. The built-in <i>sorted()</i> function "
         "uses the <i>__lt__</i> magic method for custom ordering of items by title."),

        ("<b>Composition</b>: The <i>Library</i> class contains instances of <i>LinkedList</i>, "
         "<i>Stack</i>, <i>Queue</i>, and dictionaries of <i>Member</i> and <i>LibraryItem</i> objects. "
         "These components work together to provide the system's full functionality."),

        ("<b>Magic Methods</b>: Extensively used throughout the codebase. <i>models.py</i> implements "
         "<i>__str__</i>, <i>__repr__</i>, <i>__eq__</i>, <i>__lt__</i>, <i>__hash__</i>. "
         "<i>data_structures.py</i> implements <i>__len__</i>, <i>__contains__</i>, <i>__getitem__</i>, "
         "<i>__iter__</i>, and <i>__bool__</i>."),

        ("<b>Class Methods</b>: <i>LibraryItem.get_total_items_created()</i> and "
         "<i>Member.get_member_count()</i> use the <i>@classmethod</i> decorator to track the total "
         "number of instances created across all subclasses."),

        ("<b>Static Methods</b>: <i>LibraryItem.validate_year()</i> and <i>Member.validate_email()</i> "
         "use <i>@staticmethod</i> for utility validation functions that do not depend on instance "
         "or class state."),

        ("<b>Properties</b>: The <i>@property</i> decorator is used throughout all classes to provide "
         "getter and setter methods for encapsulated attributes, enabling controlled access with "
         "input validation."),
    ]

    for concept in oop_concepts:
        elements.append(Paragraph(f"\u2022 {concept}", styles['BulletItem']))

    # ── Section 3: Declaration of External Resources ──
    elements.append(Paragraph(
        "3. Declaration of External Resources",
        styles['SectionHeading']
    ))

    elements.append(Paragraph(
        "No external third-party packages are required. The system uses only Python standard library "
        "modules: <i>abc</i> (for abstract base classes), <i>datetime</i> (for date handling and "
        "due date calculation), and <i>collections</i> (deque, used in certain data structure operations). "
        "All custom data structures (LinkedList, Stack, Queue) are implemented from scratch.",
        styles['BodyText12']
    ))

    # ── Section 4: Self-reflection on Weaknesses and Future Improvements ──
    elements.append(Paragraph(
        "4. Self-reflection on Weaknesses and Future Improvements",
        styles['SectionHeading']
    ))

    elements.append(Paragraph("<b>Weaknesses:</b>", styles['BodyText12']))

    weaknesses = [
        "Data is not persisted to disk; all data is lost when the program exits. A future version "
        "could add file-based or database storage using JSON, CSV, or SQLite.",
        "The search function only matches by title keyword. It could be extended to search by "
        "author, ISBN, genre, or other metadata fields.",
        "Late fee calculation is simplified; real libraries have more complex policies with "
        "grace periods, maximum caps, and tiered rates.",
        "The Queue-based waitlist does not handle priority levels or reservation expiration. "
        "A priority queue could improve fairness for premium members.",
    ]
    for w in weaknesses:
        elements.append(Paragraph(f"\u2022 {w}", styles['BulletItem']))

    elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Future Improvements:</b>", styles['BodyText12']))

    improvements = [
        "Add file I/O or SQLite database for persistent storage across sessions.",
        "Implement a graphical user interface (GUI) using tkinter or PyQt for better user experience.",
        "Add more search filters and sorting options (by author, year, type, popularity).",
        "Implement a recommendation system based on borrow history and member preferences.",
        "Add comprehensive unit tests using the <i>unittest</i> or <i>pytest</i> framework for "
        "automated testing and regression prevention.",
    ]
    for imp in improvements:
        elements.append(Paragraph(f"\u2022 {imp}", styles['BulletItem']))

    # ── Section 5: GitHub Repository Link ──
    elements.append(Paragraph(
        "5. GitHub Repository Link",
        styles['SectionHeading']
    ))

    elements.append(Paragraph(
        "https://github.com/Xuewaonline/COMP8090SEF-Project/tree/main/Task1_OOP",
        styles['BodyText12']
    ))

    # ── Section 6: Video Link ──
    elements.append(Paragraph(
        "6. Video Link",
        styles['SectionHeading']
    ))

    elements.append(Paragraph(
        "[Your YouTube/Bilibili Link]",
        styles['BodyText12']
    ))

    # ── Section 7: References ──
    elements.append(Paragraph(
        "7. References",
        styles['SectionHeading']
    ))

    references = [
        'Python Documentation. <i>The Python Standard Library</i>. Available at: '
        'https://docs.python.org/3/',
        'Python Documentation. <i>abc -- Abstract Base Classes</i>. Available at: '
        'https://docs.python.org/3/library/abc.html',
        'Python Documentation. <i>datetime -- Basic date and time types</i>. Available at: '
        'https://docs.python.org/3/library/datetime.html',
    ]
    for i, ref in enumerate(references, 1):
        elements.append(Paragraph(f"[{i}] {ref}", styles['Reference']))

    elements.append(PageBreak())
    return elements


# ─── Appendix ────────────────────────────────────────────────────────────────

def build_appendix(styles):
    """Build the appendix pages."""
    elements = []

    elements.append(Paragraph("Appendix", styles['AppendixHeading']))

    # ── Figure 1: OOP Concepts Usage Table ──
    elements.append(Paragraph(
        "Figure 1: OOP Concepts Usage Table",
        styles['FigureCaption']
    ))

    # Table data
    table_data = [
        ["OOP Concept", "Module", "Example"],
        ["Abstraction", "models.py", "LibraryItem(ABC) with abstract methods\nget_type(), get_details(), get_late_fee_per_day()"],
        ["Encapsulation", "all modules", "Private attrs (__attr) + @property decorators\nwith getter/setter validation"],
        ["Single Inheritance", "models.py", "Book(LibraryItem), Magazine(LibraryItem),\nDVD(LibraryItem)"],
        ["Multi-level\nInheritance", "models.py", "DigitalBook(Book(LibraryItem))\nThree levels deep"],
        ["Multiple Inheritance\n(Mixin)", "library.py", "Member(Printable) mixin pattern\ndisplay_info() method"],
        ["Polymorphism", "models.py", "get_type(), get_details() overridden differently\nin each subclass; __lt__ for sorting"],
        ["Composition", "library.py", "Library contains LinkedList, Stack, Queue,\nand dictionaries of Members and Items"],
        ["Magic Methods", "all modules", "__str__, __repr__, __eq__, __lt__, __hash__\n__len__, __contains__, __getitem__, __iter__, __bool__"],
        ["Class Methods", "models.py,\nlibrary.py", "get_total_items_created(),\nget_member_count()"],
        ["Static Methods", "models.py,\nlibrary.py", "validate_year(), validate_email()"],
    ]

    # Calculate column widths
    avail_width = PAGE_WIDTH - 2 * MARGIN
    col_widths = [avail_width * 0.22, avail_width * 0.16, avail_width * 0.62]

    table = Table(table_data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        # Header row
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), FONT_NAME_BOLD),
        ('FONTSIZE', (0, 0), (-1, 0), 10),

        # Body rows
        ('FONTNAME', (0, 1), (-1, -1), FONT_NAME),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('LEADING', (0, 0), (-1, -1), 12),

        # Alternating row colours
        *[('BACKGROUND', (0, i), (-1, i), HexColor('#D6E4F0'))
          for i in range(1, len(table_data), 2)],
        *[('BACKGROUND', (0, i), (-1, i), colors.white)
          for i in range(2, len(table_data), 2)],

        # Grid
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#8DB4E2')),

        # Alignment
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (0, 1), (0, -1), 'LEFT'),
        ('ALIGN', (1, 1), (1, -1), 'CENTER'),
        ('ALIGN', (2, 1), (2, -1), 'LEFT'),

        # Padding
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))

    elements.append(table)

    elements.append(Spacer(1, 30))

    # ── Figure 2: Sample Running Output ──
    elements.append(Paragraph(
        "Figure 2: Sample Running Output",
        styles['FigureCaption']
    ))

    sample_output = """\
************************************************************
  COMP8090SEF - Library Management System
  Student: HE Xue (SID: 13927408)
  An OOP-based Python Application
************************************************************

  Loading sample data...
  ----------------------------------------
  Added: [Book] Python Crash Course (2023) - Available
  Added: [Book] Clean Code (2008) - Available
  Added: [Book] Data Structures Using Python (2021) - Available
  Added: [Book] Introduction to Algorithms (2009) - Available
  Added: [Magazine] National Geographic (2024) - Available
  Added: [Magazine] Scientific American (2024) - Available
  Added: [DVD] The Matrix (1999) - Available
  Added: [DVD] Inception (2010) - Available
  Added: [Digital Book] Learning Python (2024) - Available
  Registered: Member(STU001: Alice Wong)
  Registered: Member(STU002: Bob Chen)
  Registered: PremiumMember(STU003: Charlie Li)
  ----------------------------------------
  Sample data loaded successfully!

############################################################
  RUNNING DEMO SCENARIO
############################################################

--- Step 1: View all library items ---

  ID         Type            Title                          Status
  -------------------------------------------------------------------
  B002       Book            Clean Code                     Available
  B003       Book            Data Structures Using Python   Available
  D002       DVD             Inception                      Available
  B004       Book            Introduction to Algorithms     Available
  E001       Digital Book    Learning Python                Available
  M001       Magazine        National Geographic            Available
  B001       Book            Python Crash Course            Available
  M002       Magazine        Scientific American            Available
  D001       DVD             The Matrix                     Available

--- Step 3: Search for 'Python' ---
  Found: [Book] Data Structures Using Python (2021) - Available
  Found: [Digital Book] Learning Python (2024) - Available
  Found: [Book] Python Crash Course (2023) - Available

--- Step 4: View item details (Polymorphism Demo) ---

  [Book]
  Title: Python Crash Course
    Author: Eric Matthes
    ISBN: 978-1593279288
    Pages: 544
    Year: 2023
  Late fee per day: $1.00

  [Magazine]
  Title: National Geographic
    Issue: #256
    Publisher: National Geographic Society
    Year: 2024
  Late fee per day: $0.50

  [DVD]
  Title: The Matrix
    Director: Wachowskis
    Duration: 136 min
    Year: 1999
  Late fee per day: $2.00

--- Step 5: Member Info (Inheritance Demo) ---

  ----------------------------------------
  Member ID: STU001
  Name: Alice Wong
  Email: alice@hkmu.edu.hk
  Type: Standard
  Items borrowed: 0/5
  ----------------------------------------

  ----------------------------------------
  Member ID: STU003
  Name: Charlie Li
  Email: charlie@hkmu.edu.hk
  Type: Premium
  Items borrowed: 0/5
  Late fee discount: 50%
  ----------------------------------------

--- Step 6: Borrow Items ---
  Success: Alice Wong borrowed 'Python Crash Course'.
  Due date: 2026-04-19
  'Python Crash Course' is not available. Bob Chen added to waitlist (position: 1).
  Success: Bob Chen borrowed 'The Matrix'.
  Due date: 2026-04-19
  Success: Charlie Li borrowed 'Learning Python'.
  Due date: 2026-04-19
  Success: Alice Wong borrowed 'Learning Python'.
  Due date: 2026-04-19

--- Step 9: Return Items ---
  Success: Alice Wong returned 'Python Crash Course'.
  Returned on time. No late fee.
  Notification: 'Python Crash Course' is now available for Bob Chen!

--- Step 11: Undo Last Action (Stack) ---
  Undo: Re-borrowed 'Python Crash Course' for Alice Wong.

--- Step 12: Library Statistics ---

  Library: HKMU Central Library
  ========================================
  Total items:      9
  Available:        5
  Borrowed:         4
  Total members:    3
  Borrow records:   5
  Undo stack size:  9

--- Step 14: Class & Static Methods ---
  Total items created (class method): 9
  Total members created (class method): 3
  Validate year 2024 (static method): True
  Validate year 3000 (static method): False
  Validate email (static method): True

--- Step 15: Custom Data Structures Demo ---
  Stack demo: Stack (top -> bottom): Action 3 | Action 2 | Action 1
    Pop: Action 3
    After pop: Stack (top -> bottom): Action 2 | Action 1

  Queue demo: Queue (front -> back): Person A <- Person B <- Person C
    Dequeue: Person A
    After dequeue: Queue (front -> back): Person B <- Person C

############################################################
  DEMO SCENARIO COMPLETED
############################################################"""

    # Split into lines and add as code block paragraphs
    for line in sample_output.split('\n'):
        # Escape XML special characters
        escaped = (line
                   .replace('&', '&amp;')
                   .replace('<', '&lt;')
                   .replace('>', '&gt;'))
        if not escaped.strip():
            escaped = " "  # Preserve blank lines
        elements.append(Paragraph(escaped, styles['CodeBlock']))

    return elements


# ─── Page Number Footer ─────────────────────────────────────────────────────

def add_page_number(canvas, doc):
    """Add page number to the bottom center of each page."""
    canvas.saveState()
    canvas.setFont(FONT_NAME, 10)
    page_num = canvas.getPageNumber()
    text = f"- {page_num} -"
    canvas.drawCentredString(PAGE_WIDTH / 2, 1.5 * cm, text)
    canvas.restoreState()


# ─── Main Build ─────────────────────────────────────────────────────────────

def build_report():
    """Build the complete PDF report."""
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title="COMP8090SEF Task 1 - Self-study Report",
        author="HE Xue",
    )

    styles = create_styles()
    elements = []

    # Page 1: Cover page
    elements.extend(build_cover_page(styles))

    # Pages 2-4: Main content
    elements.extend(build_main_content(styles))

    # Page 5+: Appendix
    elements.extend(build_appendix(styles))

    # Build PDF
    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"Report generated successfully: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_report()
