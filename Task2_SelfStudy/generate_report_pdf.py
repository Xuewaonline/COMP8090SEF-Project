"""
Generate Task 2 Self-Study Report PDF using ReportLab.
COMP8090SEF - Data Structures And Algorithms
Student: HE Xue (SID: 13927408)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Preformatted, KeepTogether
)
from reportlab.lib import colors

# ============================================================
# Page setup
# ============================================================
PAGE_WIDTH, PAGE_HEIGHT = A4  # 595.27, 841.89 points
MARGIN = 2.54 * cm  # ~72 points

OUTPUT_PATH = "/Users/tomzhang/Documents/xuewaonline/COMP8090SEF_DSA_Project/Task2_SelfStudy/Task2_Report.pdf"

# ============================================================
# Styles
# ============================================================
FONT = "Times-Roman"
FONT_BOLD = "Times-Bold"
FONT_ITALIC = "Times-Italic"
FONT_SIZE = 12
LEADING = FONT_SIZE * 1.2  # single-line spacing (~14.4pt)

style_normal = ParagraphStyle(
    "Normal",
    fontName=FONT,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_JUSTIFY,
    spaceAfter=6,
)

style_center = ParagraphStyle(
    "Center",
    fontName=FONT,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_CENTER,
    spaceAfter=6,
)

style_center_bold = ParagraphStyle(
    "CenterBold",
    fontName=FONT_BOLD,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_CENTER,
    spaceAfter=6,
)

style_heading1 = ParagraphStyle(
    "Heading1",
    fontName=FONT_BOLD,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_LEFT,
    spaceBefore=12,
    spaceAfter=6,
)

style_heading2 = ParagraphStyle(
    "Heading2",
    fontName=FONT_BOLD,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_LEFT,
    spaceBefore=8,
    spaceAfter=4,
)

style_declaration = ParagraphStyle(
    "Declaration",
    fontName=FONT,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_JUSTIFY,
    spaceAfter=4,
    leftIndent=0,
)

style_declaration_item = ParagraphStyle(
    "DeclarationItem",
    fontName=FONT,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_JUSTIFY,
    spaceAfter=2,
    leftIndent=18,
    firstLineIndent=-18,
)

style_code = ParagraphStyle(
    "Code",
    fontName="Courier",
    fontSize=9,
    leading=11,
    alignment=TA_LEFT,
    spaceAfter=2,
    leftIndent=12,
)

style_bullet = ParagraphStyle(
    "Bullet",
    fontName=FONT,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_LEFT,
    spaceAfter=2,
    leftIndent=24,
    bulletIndent=12,
)

style_appendix_title = ParagraphStyle(
    "AppendixTitle",
    fontName=FONT_BOLD,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_CENTER,
    spaceBefore=12,
    spaceAfter=8,
)

style_figure_caption = ParagraphStyle(
    "FigureCaption",
    fontName=FONT_BOLD,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_LEFT,
    spaceBefore=10,
    spaceAfter=4,
)

style_placeholder = ParagraphStyle(
    "Placeholder",
    fontName=FONT_ITALIC,
    fontSize=FONT_SIZE,
    leading=LEADING,
    alignment=TA_CENTER,
    spaceAfter=6,
    textColor=colors.grey,
)


def escape(text):
    """Escape XML special characters for ReportLab Paragraph."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def build_cover_page():
    """Build the cover page elements."""
    elements = []
    sp = lambda pts: Spacer(1, pts)

    elements.append(sp(60))
    elements.append(Paragraph("Hong Kong Metropolitan University", style_center))
    elements.append(sp(40))
    elements.append(Paragraph("COMP 8090SEF", style_center_bold))
    elements.append(Paragraph("Data Structures And Algorithms", style_center_bold))
    elements.append(sp(40))
    elements.append(Paragraph("Self-study Report", style_center_bold))
    elements.append(Paragraph("Submission date: 9 April 2026", style_center))
    elements.append(sp(30))

    # Declaration
    elements.append(Paragraph("I declare that:", style_declaration))

    declarations = [
        "(i) I have read and checked that all parts of the project (including proposal, code programs, and reports), they are contributed by me, here submitted is original except for source material explicitly acknowledged;",
        "(ii) the project, in parts or in whole, has not been submitted for more than one purpose without declaration;",
        "(iii) I am aware of the University's policy and regulations on honesty in academic work and understand the possible consequence when breaching such policy and regulations;",
        "(iv) I confirm that I have declared in the report about the usage of AI and other generative models, including but not limited to ChatGPT, LLaMA, Gemini, Mistral, and Stable Diffusion, and complied with the instructions provided by HKMU; and",
        "(v) I am aware that I should be held responsible and liable to disciplinary actions, irrespective of whether I have signed the declaration and whether I have contributed, directly or indirectly, to the problematic contents.",
    ]
    for decl in declarations:
        elements.append(Paragraph(escape(decl), style_declaration_item))

    elements.append(sp(12))
    elements.append(Paragraph(
        "I confirm that I have read through and understood the project requirements. "
        "I understand that failure to comply with the project requirements will result in score deduction.",
        style_declaration,
    ))
    elements.append(sp(24))
    elements.append(Paragraph(
        "NAME: HE Xue&nbsp;&nbsp;&nbsp;&nbsp;SID: 13927408",
        style_center_bold,
    ))

    elements.append(PageBreak())
    return elements


def build_main_content():
    """Build pages 2-4: main report content (text only)."""
    elements = []
    sp = lambda pts: Spacer(1, pts)

    # Title
    elements.append(Paragraph("<b>Self-study Report</b>", style_center_bold))
    elements.append(Paragraph(
        "<b>Graph data structure and Cocktail Sort algorithm</b>",
        style_center_bold,
    ))
    elements.append(sp(8))

    # ----- Section 1: Introduction -----
    elements.append(Paragraph("<b>1. Introduction</b>", style_heading1))

    elements.append(Paragraph(
        "For Task 2 of the COMP8090SEF course study project, I selected the Graph data structure "
        "and the Cocktail Sort algorithm as my self-study topics.",
        style_normal,
    ))
    elements.append(Paragraph(
        "Graphs are a versatile data structure that represents entities and their connections, "
        "much like a map of cities and roads. They are easy to conceptualize yet powerful for "
        "complex problems.",
        style_normal,
    ))
    elements.append(Paragraph(
        "Cocktail sort, also known as shaker sort or bidirectional bubble sort, improves upon "
        "bubble sort by sorting in both directions, reducing passes and making it more efficient "
        "for nearly sorted data.",
        style_normal,
    ))
    elements.append(Paragraph(
        "The report will introduce the abstract data type (ADT) for graphs, detail its main methods "
        "and applications, analyze the time complexity of cocktail sort with examples, and cover their "
        "development through Python implementations. This self-study has enhanced my knowledge of "
        "non-linear data structures and sorting optimizations.",
        style_normal,
    ))
    elements.append(Paragraph(
        "The repository link is: https://github.com/Xuewaonline/COMP8090SEF-Project/tree/main/Task2_SelfStudy",
        style_normal,
    ))
    elements.append(Paragraph(
        "The video link is: [Your YouTube/Bilibili Link]",
        style_normal,
    ))

    # ----- Section 2: Data Structure: Graph -----
    elements.append(Paragraph("<b>2. Data Structure: Graph</b>", style_heading1))

    elements.append(Paragraph(
        "A graph is an abstract data type (ADT) that represents a set of objects called vertices "
        "and the relationships between them called edges. The ADT for a graph includes operations "
        "to add vertices and edges, remove them, and check for connections. In simple terms, the "
        "graph ADT is like a map of points and lines, where points are vertices and lines are edges. "
        "Vertices can be anything, like people or places, and edges show how they are linked, like "
        "friendships or roads.",
        style_normal,
    ))
    elements.append(Paragraph(
        "<i>(Appendix &amp; References: Figure 0 Comparison Table of Graph)</i>",
        style_normal,
    ))

    # --- 2.1 Undirected Graph ---
    elements.append(Paragraph("<b>2.1 Undirected Graph</b>", style_heading2))
    elements.append(Paragraph(
        "An undirected graph is a graph where edges have no direction. This means if there is an "
        "edge between node A and node B, you can traverse it in both directions (from A to B and "
        "B to A). Edges represent symmetric relationships, like mutual friendships. There are no "
        "arrows on edges; they are just lines connecting nodes.",
        style_normal,
    ))
    elements.append(Paragraph(
        "<i>(Appendix &amp; References: Figure 1 Data Structure (Undirected Graph))</i>",
        style_normal,
    ))
    elements.append(Paragraph("Key Characteristics:", style_normal))
    for item in [
        "Edges are bidirectional.",
        "No self-loops or multiple edges between the same pair unless specified as a multigraph.",
        "Represented using adjacency lists or adjacency matrices.",
    ]:
        elements.append(Paragraph(
            f"<bullet>&bull;</bullet>{escape(item)}", style_bullet
        ))
    elements.append(Paragraph(
        "<b>Possible Applications:</b> Road maps, friendship networks, or undirected connections "
        "in computer networks.",
        style_normal,
    ))
    elements.append(Paragraph(
        "<b>Comments:</b> Undirected Graph is simple for symmetric data, but it can't model "
        "one-way relationships.",
        style_normal,
    ))

    # --- 2.2 Directed Graph ---
    elements.append(Paragraph("<b>2.2 Directed Graph</b>", style_heading2))
    elements.append(Paragraph(
        "A directed graph is a graph where edges have a direction, indicated by arrows. An edge "
        "from A to B means you can go from A to B, but not necessarily B to A unless there's a "
        "separate edge. Edges represent asymmetric relationships, like one-way streets.",
        style_normal,
    ))
    elements.append(Paragraph(
        "<i>(Appendix &amp; References: Figure 2 Data Structure (Directed Graph))</i>",
        style_normal,
    ))
    elements.append(Paragraph("Key Characteristics:", style_normal))
    for item in [
        "Edges are unidirectional (arrows point from source to destination).",
        "Can have cycles (loops back to start).",
    ]:
        elements.append(Paragraph(
            f"<bullet>&bull;</bullet>{escape(item)}", style_bullet
        ))
    elements.append(Paragraph(
        "<b>Possible Applications:</b> Web links (hyperlinks are one-way), task scheduling, "
        "or traffic flow with one-way streets.",
        style_normal,
    ))
    elements.append(Paragraph(
        "<b>Comments:</b> Models real-world asymmetries; but more complex to traverse.",
        style_normal,
    ))

    # --- 2.3 Weighted Graph ---
    elements.append(Paragraph("<b>2.3 Weighted Graph</b>", style_heading2))
    elements.append(Paragraph(
        "A weighted graph is a graph (can be undirected or directed) where each edge has a weight "
        "or cost associated with it, representing a value like distance, time, or price. Weights "
        "are numbers (integers or floats) on edges.",
        style_normal,
    ))
    elements.append(Paragraph(
        "<i>(Appendix &amp; References: Figure 3 Data Structure (Weighted Graph))</i>",
        style_normal,
    ))
    elements.append(Paragraph("Key Characteristics:", style_normal))
    for item in [
        "Builds on undirected or directed graphs but adds numerical values to edges.",
        "No weights mean it's unweighted (all edges equal, like weight=1).",
    ]:
        elements.append(Paragraph(
            f"<bullet>&bull;</bullet>{escape(item)}", style_bullet
        ))
    elements.append(Paragraph(
        "<b>Possible Applications:</b> GPS navigation (shortest path with distances), network "
        "routing (bandwidth as weights), or social graphs with friendship strength.",
        style_normal,
    ))
    elements.append(Paragraph(
        "<b>Comments:</b> Handles real costs; but algorithms like shortest path are needed, "
        "adding complexity.",
        style_normal,
    ))

    # ----- Section 3: Algorithm: Cocktail Sort -----
    elements.append(Paragraph("<b>3. Algorithm: Cocktail Sort</b>", style_heading1))
    elements.append(Paragraph(
        "Cocktail sort is a sorting algorithm that is a variation of bubble sort. It sorts a list "
        "by repeatedly going through it from left to right and then from right to left, swapping "
        "adjacent items if they are in the wrong order. The definition is that it bubbles the "
        "largest items to the end in one direction and the smallest to the beginning in the other "
        'direction. The name "cocktail" comes from the way it mixes or shakes the elements back '
        "and forth, similar to shaking a cocktail shaker.",
        style_normal,
    ))
    elements.append(Paragraph(
        "<i>(Appendix &amp; References: Figure 4 Algorithm (Cocktail Sort))</i>",
        style_normal,
    ))

    elements.append(Paragraph("Key Characteristics:", style_normal))
    for item in [
        "Bidirectional Passes: Unlike Bubble Sort, which only passes in one direction, Cocktail Sort alternates between forward and backward passes.",
        "Optimization Flag: It uses a flag to track if any swaps occurred. If no swaps happen, the array is sorted, allowing early termination.",
    ]:
        elements.append(Paragraph(
            f"<bullet>&bull;</bullet>{escape(item)}", style_bullet
        ))

    elements.append(Paragraph("Time Complexity:", style_normal))
    for item in [
        "Worst-case: O(n<super>2</super>) - when the array is reverse-sorted",
        "Average-case: O(n<super>2</super>) - but performs better than Bubble Sort",
        "Best-case: O(n) - for already sorted arrays",
    ]:
        elements.append(Paragraph(
            f"<bullet>&bull;</bullet>{item}", style_bullet
        ))

    elements.append(Paragraph("<b>Possible Applications:</b>", style_normal))
    for item in [
        "Data Processing: Updating leaderboards in games or priority lists",
        "File Sorting Utilities: Sorting short text files or logs",
        "Educational Purposes: Used for test result sorting",
    ]:
        elements.append(Paragraph(
            f"<bullet>&bull;</bullet>{escape(item)}", style_bullet
        ))

    elements.append(Paragraph(
        "<b>Comments:</b> Cocktail Sort is a straightforward improvement over Bubble Sort. Its "
        "main strength is early termination in best/average cases, but it remains inefficient for "
        "large datasets compared to divide-and-conquer sorts. It's stable and in-place, which is "
        "advantageous for memory-constrained environments.",
        style_normal,
    ))

    # ----- Section 4: Code Demonstration -----
    elements.append(Paragraph("<b>4. Code Demonstration</b>", style_heading1))
    elements.append(Paragraph(
        "The cocktail_sort function takes an array arr. It uses a while loop to repeat passes "
        "until no swaps. The forward loop (range(start, end)) swaps larger elements right. After, "
        "shrink end. The backward loop (range(end-1, start-1, -1)) swaps smaller left. Shrink "
        "start. The flag optimizes by exiting early if sorted. Test with [8,7,4,8,1]: After calls, "
        "returns [1,4,7,8,8].",
        style_normal,
    ))
    elements.append(Paragraph(
        "<i>(See Appendix for code snippets and running results.)</i>",
        style_normal,
    ))

    # ----- Section 5: References -----
    elements.append(Paragraph("<b>5. References</b>", style_heading1))
    elements.append(Paragraph(
        '<bullet>&bull;</bullet>Graph Representation: '
        'https://studyglance.in/ds/display.php?tno=33&amp;topic=Graph-Representation',
        style_bullet,
    ))
    elements.append(Paragraph(
        '<bullet>&bull;</bullet>Cocktail Sort Steps: '
        'https://www.educba.com/cocktail-sort/',
        style_bullet,
    ))

    elements.append(PageBreak())
    return elements


def build_appendix():
    """Build the Appendix pages (page 5+)."""
    elements = []
    sp = lambda pts: Spacer(1, pts)

    elements.append(Paragraph("<b>APPENDIX</b>", style_appendix_title))
    elements.append(sp(8))

    # --- Figure 0: Comparison Table ---
    elements.append(Paragraph(
        "<b>Figure 0: Comparison Table of Graph</b>", style_figure_caption
    ))

    table_data = [
        ["Aspect", "Undirected Graph", "Directed Graph", "Weighted Graph"],
        ["Direction", "No direction\n(bidirectional)", "Has direction\n(unidirectional)", "Can be either,\nwith weights"],
        ["Edge\nRepresentation", "Simple line\n(A--B)", "Arrow\n(A->B)", "Line/arrow with\nnumber (A--50--B)"],
        ["Example", "Mutual\nfriendship", "X(Twitter)\nfollows", "Distance\nbetween cities"],
        ["Traversal", "Symmetric\n(both ways)", "Follow arrows\nonly", "Consider weights\nfor costs"],
        ["Common Use", "Social\nnetworks", "Web links,\nworkflows", "Maps"],
        ["Complexity", "Simple", "Handles\nasymmetries", "Adds numerical\nanalysis"],
    ]

    col_widths = [70, 110, 110, 110]
    table = Table(table_data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), FONT_BOLD),
        ("FONTNAME", (0, 1), (-1, -1), FONT),
        ("FONTNAME", (0, 0), (0, -1), FONT_BOLD),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("LEADING", (0, 0), (-1, -1), 11),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.9, 0.9, 0.9)),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    elements.append(table)
    elements.append(sp(12))

    # --- Figures 1-4: Placeholders ---
    for fig_num, caption in [
        (1, "Data Structure (Undirected Graph)"),
        (2, "Data Structure (Directed Graph)"),
        (3, "Data Structure (Weighted Graph)"),
        (4, "Algorithm (Cocktail Sort)"),
    ]:
        elements.append(Paragraph(
            f"<b>Figure {fig_num}: {caption}</b>", style_figure_caption
        ))
        elements.append(Paragraph(
            "[See original report for diagram]", style_placeholder
        ))
        elements.append(sp(6))

    # --- Figure 5: Code Snippet ---
    elements.append(Paragraph(
        "<b>Figure 5: Code Snippet - Cocktail Sort Function</b>",
        style_figure_caption,
    ))

    code_text = """\
def cocktail_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    start = 0
    end = n - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        end -= 1
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1
    return arr"""

    code_style = ParagraphStyle(
        "CodeBlock",
        fontName="Courier",
        fontSize=9,
        leading=11,
        alignment=TA_LEFT,
        leftIndent=12,
        rightIndent=12,
        spaceBefore=4,
        spaceAfter=4,
        backColor=colors.Color(0.95, 0.95, 0.95),
    )
    elements.append(Preformatted(code_text, code_style))
    elements.append(sp(12))

    # --- Figure 6: Sample Output ---
    elements.append(Paragraph(
        "<b>Figure 6: Sample Output - Sorting [8, 7, 4, 8, 1] Step by Step</b>",
        style_figure_caption,
    ))

    output_text = """\
Initial array: [8, 7, 4, 8, 1]

Pass 1 - Forward (left to right, index 0 to 4):
  Swap arr[0]=8 and arr[1]=7 -> [7, 8, 4, 8, 1]
  Swap arr[1]=8 and arr[2]=4 -> [7, 4, 8, 8, 1]
  Swap arr[3]=8 and arr[4]=1 -> [7, 4, 8, 1, 8]
  After forward pass: [7, 4, 8, 1, 8] (right boundary now 3)

Pass 1 - Backward (right to left, index 2 to 0):
  Swap arr[2]=8 and arr[3]=1 -> [7, 4, 1, 8, 8]
  Swap arr[1]=4 and arr[2]=1 -> [7, 1, 4, 8, 8]
  Swap arr[0]=7 and arr[1]=1 -> [1, 7, 4, 8, 8]
  After backward pass: [1, 7, 4, 8, 8] (left boundary now 1)

Pass 2 - Forward (left to right, index 1 to 3):
  Swap arr[1]=7 and arr[2]=4 -> [1, 4, 7, 8, 8]
  After forward pass: [1, 4, 7, 8, 8] (right boundary now 2)

Pass 2 - Backward (right to left, index 1 to 1):
  No swaps -> Array is sorted!

Sorted array: [1, 4, 7, 8, 8]"""

    output_style = ParagraphStyle(
        "OutputBlock",
        fontName="Courier",
        fontSize=8.5,
        leading=10.5,
        alignment=TA_LEFT,
        leftIndent=12,
        rightIndent=12,
        spaceBefore=4,
        spaceAfter=4,
        backColor=colors.Color(0.95, 0.95, 0.95),
    )
    elements.append(Preformatted(output_text, output_style))

    return elements


def build_pdf():
    """Assemble and generate the full PDF report."""
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        title="COMP8090SEF Self-study Report - Task 2",
        author="HE Xue (13927408)",
    )

    elements = []
    elements.extend(build_cover_page())
    elements.extend(build_main_content())
    elements.extend(build_appendix())

    doc.build(elements)
    print(f"PDF generated successfully: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
