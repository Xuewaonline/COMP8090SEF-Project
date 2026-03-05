"""
Cocktail Sort Algorithm Implementation
COMP8090SEF - Task 2 Self Study
Student: HE Xue (SID: 13927408)

Cocktail Sort (also known as Bidirectional Bubble Sort or Shaker Sort)
is a variation of Bubble Sort that sorts in both directions on each pass.

Time Complexity:
  - Best case:    O(n)   - already sorted array, early termination
  - Average case: O(n^2) - better than bubble sort in practice
  - Worst case:   O(n^2) - reverse sorted array
Space Complexity: O(1)   - in-place sorting
Stability: Stable        - equal elements maintain relative order
"""


def cocktail_sort(arr):
    """
    Sort a list using the Cocktail Sort algorithm.

    The algorithm works by:
    1. Forward pass (left to right): bubble the largest unsorted element
       to the right end, like standard bubble sort.
    2. Backward pass (right to left): bubble the smallest unsorted element
       to the left end.
    3. Repeat until no swaps occur in a complete forward+backward pass.

    The 'swapped' flag allows early termination when the array is sorted.

    Parameters:
        arr: list of comparable elements
    Returns:
        The sorted list (sorts in-place and also returns it)
    """
    n = len(arr)
    if n <= 1:
        return arr

    start = 0       # Left boundary of unsorted region
    end = n - 1     # Right boundary of unsorted region
    swapped = True

    while swapped:
        swapped = False

        # Forward pass: left to right
        # Move the largest unsorted element to the right end
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If no swaps happened, the array is sorted
        if not swapped:
            break

        # Shrink the right boundary (largest element is now in place)
        end -= 1

        swapped = False

        # Backward pass: right to left
        # Move the smallest unsorted element to the left end
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Shrink the left boundary (smallest element is now in place)
        start += 1

    return arr


def cocktail_sort_verbose(arr):
    """
    Verbose version that prints each step for educational purposes.
    Shows the state of the array after each pass.
    """
    n = len(arr)
    if n <= 1:
        return arr

    start = 0
    end = n - 1
    swapped = True
    pass_num = 0

    print(f"  Initial array: {arr}")
    print()

    while swapped:
        swapped = False
        pass_num += 1

        # Forward pass
        print(f"  Pass {pass_num} - Forward (left to right, index {start} to {end}):")
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                print(f"    Swap arr[{i}]={arr[i+1]} and arr[{i+1}]={arr[i]} -> {arr}")

        if not swapped:
            print(f"    No swaps -> Array is sorted!")
            break

        end -= 1
        print(f"    After forward pass: {arr} (right boundary now {end})")
        print()

        swapped = False

        # Backward pass
        print(f"  Pass {pass_num} - Backward (right to left, index {end-1} to {start}):")
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                print(f"    Swap arr[{i}]={arr[i+1]} and arr[{i+1}]={arr[i]} -> {arr}")

        if not swapped:
            print(f"    No swaps -> Array is sorted!")
        else:
            start += 1
            print(f"    After backward pass: {arr} (left boundary now {start})")
        print()

    print(f"  Sorted array: {arr}")
    return arr


def compare_with_bubble_sort(arr):
    """
    Compare Cocktail Sort vs Bubble Sort by counting swap operations.
    Demonstrates that Cocktail Sort often needs fewer passes.
    """
    import copy

    # Bubble Sort with swap counter
    bubble_arr = copy.deepcopy(arr)
    bubble_swaps = 0
    bubble_passes = 0
    n = len(bubble_arr)
    for i in range(n):
        swapped = False
        bubble_passes += 1
        for j in range(0, n - i - 1):
            if bubble_arr[j] > bubble_arr[j + 1]:
                bubble_arr[j], bubble_arr[j + 1] = bubble_arr[j + 1], bubble_arr[j]
                bubble_swaps += 1
                swapped = True
        if not swapped:
            break

    # Cocktail Sort with swap counter
    cocktail_arr = copy.deepcopy(arr)
    cocktail_swaps = 0
    cocktail_passes = 0
    start_idx = 0
    end_idx = n - 1
    swapped = True
    while swapped:
        swapped = False
        cocktail_passes += 1
        for i in range(start_idx, end_idx):
            if cocktail_arr[i] > cocktail_arr[i + 1]:
                cocktail_arr[i], cocktail_arr[i + 1] = cocktail_arr[i + 1], cocktail_arr[i]
                cocktail_swaps += 1
                swapped = True
        if not swapped:
            break
        end_idx -= 1
        swapped = False
        for i in range(end_idx - 1, start_idx - 1, -1):
            if cocktail_arr[i] > cocktail_arr[i + 1]:
                cocktail_arr[i], cocktail_arr[i + 1] = cocktail_arr[i + 1], cocktail_arr[i]
                cocktail_swaps += 1
                swapped = True
        start_idx += 1

    print(f"  Input array: {arr}")
    print(f"  {'Algorithm':<20} {'Passes':<10} {'Swaps':<10} {'Result'}")
    print(f"  {'-'*60}")
    print(f"  {'Bubble Sort':<20} {bubble_passes:<10} {bubble_swaps:<10} {bubble_arr}")
    print(f"  {'Cocktail Sort':<20} {cocktail_passes:<10} {cocktail_swaps:<10} {cocktail_arr}")


# ============================================================
# Demonstration
# ============================================================

def demo_basic():
    """Basic cocktail sort demonstration."""
    print("=" * 60)
    print("DEMO 1: Basic Cocktail Sort")
    print("=" * 60)
    print("\nSorting the array [8, 7, 4, 8, 1]:\n")

    arr = [8, 7, 4, 8, 1]
    cocktail_sort_verbose(arr)
    print()


def demo_already_sorted():
    """Demonstrate best-case O(n) performance on sorted array."""
    print("=" * 60)
    print("DEMO 2: Best Case - Already Sorted Array")
    print("=" * 60)
    print("\nSorting the array [1, 2, 3, 4, 5]:")
    print("Expected: Only one forward pass with no swaps -> O(n)\n")

    arr = [1, 2, 3, 4, 5]
    cocktail_sort_verbose(arr)
    print()


def demo_reverse_sorted():
    """Demonstrate worst-case on reverse-sorted array."""
    print("=" * 60)
    print("DEMO 3: Worst Case - Reverse Sorted Array")
    print("=" * 60)
    print("\nSorting the array [5, 4, 3, 2, 1]:")
    print("This is the worst case requiring the most swaps.\n")

    arr = [5, 4, 3, 2, 1]
    cocktail_sort_verbose(arr)
    print()


def demo_nearly_sorted():
    """Demonstrate cocktail sort advantage on nearly sorted data."""
    print("=" * 60)
    print("DEMO 4: Nearly Sorted Array (Cocktail Sort Advantage)")
    print("=" * 60)
    print("\nSorting [2, 3, 4, 5, 1] - only element '1' is misplaced.\n")

    arr = [2, 3, 4, 5, 1]
    cocktail_sort_verbose(arr)
    print()


def demo_comparison():
    """Compare Cocktail Sort vs Bubble Sort."""
    print("=" * 60)
    print("DEMO 5: Cocktail Sort vs Bubble Sort Comparison")
    print("=" * 60)

    print("\nTest 1: Nearly sorted array")
    compare_with_bubble_sort([2, 3, 4, 5, 1])

    print("\nTest 2: Reverse sorted array")
    compare_with_bubble_sort([5, 4, 3, 2, 1])

    print("\nTest 3: Random array")
    compare_with_bubble_sort([64, 34, 25, 12, 22, 11, 90])

    print("\nTest 4: Already sorted array")
    compare_with_bubble_sort([1, 2, 3, 4, 5])

    print()


def demo_string_sort():
    """Demonstrate sorting strings (stable sort property)."""
    print("=" * 60)
    print("DEMO 6: Sorting Strings (Stable Sort)")
    print("=" * 60)
    print("\nCocktail sort works with any comparable elements.")
    print("Sorting names alphabetically:\n")

    names = ["Eve", "Alice", "Diana", "Bob", "Charlie"]
    print(f"  Before: {names}")
    cocktail_sort(names)
    print(f"  After:  {names}")
    print()


def main():
    """Run all cocktail sort demonstrations."""
    print("\n" + "#" * 60)
    print("  COCKTAIL SORT ALGORITHM - DEMONSTRATION")
    print("  COMP8090SEF Task 2 Self Study")
    print("#" * 60 + "\n")

    demo_basic()
    demo_already_sorted()
    demo_reverse_sorted()
    demo_nearly_sorted()
    demo_comparison()
    demo_string_sort()

    print("=" * 60)
    print("All cocktail sort demonstrations completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
