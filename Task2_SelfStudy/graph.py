"""
Graph Data Structure Implementation
COMP8090SEF - Task 2 Self Study
Student: HE Xue (SID: 13927408)

This module implements three types of graphs:
1. Undirected Graph
2. Directed Graph
3. Weighted Graph

Each graph supports common operations: add/remove vertices and edges,
check connections, BFS, DFS traversal, and display.
"""

from collections import deque


class UndirectedGraph:
    """
    Undirected Graph using adjacency list representation.
    Edges have no direction - if A connects to B, then B connects to A.

    Example use case: Social network friendships (mutual connections).
    """

    def __init__(self):
        # Adjacency list: {vertex: set of neighbors}
        self._adj_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph. If it already exists, do nothing."""
        if vertex not in self._adj_list:
            self._adj_list[vertex] = set()
            print(f"  Vertex '{vertex}' added.")
        else:
            print(f"  Vertex '{vertex}' already exists.")

    def remove_vertex(self, vertex):
        """Remove a vertex and all its edges from the graph."""
        if vertex in self._adj_list:
            # Remove this vertex from all neighbors' adjacency sets
            for neighbor in self._adj_list[vertex]:
                self._adj_list[neighbor].discard(vertex)
            del self._adj_list[vertex]
            print(f"  Vertex '{vertex}' removed.")
        else:
            print(f"  Vertex '{vertex}' not found.")

    def add_edge(self, v1, v2):
        """Add an undirected edge between v1 and v2."""
        if v1 not in self._adj_list:
            self.add_vertex(v1)
        if v2 not in self._adj_list:
            self.add_vertex(v2)
        self._adj_list[v1].add(v2)
        self._adj_list[v2].add(v1)
        print(f"  Edge added: {v1} -- {v2}")

    def remove_edge(self, v1, v2):
        """Remove the edge between v1 and v2."""
        if v1 in self._adj_list and v2 in self._adj_list[v1]:
            self._adj_list[v1].discard(v2)
            self._adj_list[v2].discard(v1)
            print(f"  Edge removed: {v1} -- {v2}")
        else:
            print(f"  Edge {v1} -- {v2} not found.")

    def has_edge(self, v1, v2):
        """Check if an edge exists between v1 and v2."""
        return v1 in self._adj_list and v2 in self._adj_list[v1]

    def get_neighbors(self, vertex):
        """Return the set of neighbors of a vertex."""
        return self._adj_list.get(vertex, set())

    def bfs(self, start):
        """
        Breadth-First Search starting from 'start'.
        Uses a queue to explore level by level.
        Returns the list of vertices in BFS order.
        """
        if start not in self._adj_list:
            print(f"  Vertex '{start}' not in graph.")
            return []
        visited = set()
        order = []
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in sorted(self._adj_list[vertex]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        """
        Depth-First Search starting from 'start'.
        Uses a stack (iterative) to explore as deep as possible first.
        Returns the list of vertices in DFS order.
        """
        if start not in self._adj_list:
            print(f"  Vertex '{start}' not in graph.")
            return []
        visited = set()
        order = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                # Push neighbors in reverse sorted order so smallest is popped first
                for neighbor in sorted(self._adj_list[vertex], reverse=True):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def display(self):
        """Print the adjacency list of the graph."""
        print("\n  Undirected Graph (Adjacency List):")
        for vertex in sorted(self._adj_list):
            neighbors = sorted(self._adj_list[vertex])
            print(f"    {vertex} -> {neighbors}")

    def __str__(self):
        lines = [f"  {v} -> {sorted(n)}" for v, n in sorted(self._adj_list.items())]
        return "Undirected Graph:\n" + "\n".join(lines)


class DirectedGraph:
    """
    Directed Graph using adjacency list representation.
    Edges have a direction - an edge from A to B does NOT imply B to A.

    Example use case: Web page hyperlinks, task dependencies.
    """

    def __init__(self):
        self._adj_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self._adj_list:
            self._adj_list[vertex] = set()
            print(f"  Vertex '{vertex}' added.")

    def remove_vertex(self, vertex):
        """Remove a vertex and all edges pointing to/from it."""
        if vertex in self._adj_list:
            del self._adj_list[vertex]
            # Remove all edges pointing to this vertex
            for v in self._adj_list:
                self._adj_list[v].discard(vertex)
            print(f"  Vertex '{vertex}' removed.")

    def add_edge(self, source, destination):
        """Add a directed edge from source to destination."""
        if source not in self._adj_list:
            self.add_vertex(source)
        if destination not in self._adj_list:
            self.add_vertex(destination)
        self._adj_list[source].add(destination)
        print(f"  Edge added: {source} -> {destination}")

    def remove_edge(self, source, destination):
        """Remove the directed edge from source to destination."""
        if source in self._adj_list and destination in self._adj_list[source]:
            self._adj_list[source].discard(destination)
            print(f"  Edge removed: {source} -> {destination}")
        else:
            print(f"  Edge {source} -> {destination} not found.")

    def has_edge(self, source, destination):
        """Check if a directed edge exists from source to destination."""
        return source in self._adj_list and destination in self._adj_list[source]

    def get_successors(self, vertex):
        """Return the set of vertices reachable from vertex in one step."""
        return self._adj_list.get(vertex, set())

    def get_predecessors(self, vertex):
        """Return the set of vertices that have an edge pointing to vertex."""
        return {v for v in self._adj_list if vertex in self._adj_list[v]}

    def in_degree(self, vertex):
        """Return the number of edges coming into vertex."""
        return sum(1 for v in self._adj_list if vertex in self._adj_list[v])

    def out_degree(self, vertex):
        """Return the number of edges going out from vertex."""
        return len(self._adj_list.get(vertex, set()))

    def has_cycle(self):
        """
        Detect if the directed graph contains a cycle using DFS coloring.
        WHITE=0 (unvisited), GRAY=1 (in progress), BLACK=2 (done).
        A cycle exists if we encounter a GRAY node during DFS.
        """
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {v: WHITE for v in self._adj_list}

        def dfs_visit(u):
            color[u] = GRAY
            for v in self._adj_list[u]:
                if color[v] == GRAY:
                    return True  # Back edge found -> cycle
                if color[v] == WHITE and dfs_visit(v):
                    return True
            color[u] = BLACK
            return False

        for vertex in self._adj_list:
            if color[vertex] == WHITE:
                if dfs_visit(vertex):
                    return True
        return False

    def topological_sort(self):
        """
        Return a topological ordering of the DAG (Directed Acyclic Graph).
        Uses Kahn's algorithm (BFS-based).
        Returns None if the graph has a cycle.
        """
        if self.has_cycle():
            print("  Graph has a cycle, topological sort not possible.")
            return None

        in_deg = {v: 0 for v in self._adj_list}
        for v in self._adj_list:
            for neighbor in self._adj_list[v]:
                in_deg[neighbor] += 1

        queue = deque([v for v in in_deg if in_deg[v] == 0])
        order = []
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in self._adj_list[vertex]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    queue.append(neighbor)
        return order

    def bfs(self, start):
        """Breadth-First Search from start vertex."""
        if start not in self._adj_list:
            return []
        visited = set()
        order = []
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in sorted(self._adj_list[vertex]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def display(self):
        """Print the adjacency list of the directed graph."""
        print("\n  Directed Graph (Adjacency List):")
        for vertex in sorted(self._adj_list):
            neighbors = sorted(self._adj_list[vertex])
            print(f"    {vertex} -> {neighbors}")

    def __str__(self):
        lines = [f"  {v} -> {sorted(n)}" for v, n in sorted(self._adj_list.items())]
        return "Directed Graph:\n" + "\n".join(lines)


class WeightedGraph:
    """
    Weighted Graph using adjacency list with weights.
    Each edge has a numerical weight (e.g., distance, cost, time).
    Can be configured as directed or undirected.

    Example use case: GPS navigation (shortest path between cities).
    """

    def __init__(self, directed=False):
        # {vertex: {neighbor: weight, ...}, ...}
        self._adj_list = {}
        self._directed = directed

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self._adj_list:
            self._adj_list[vertex] = {}
            print(f"  Vertex '{vertex}' added.")

    def remove_vertex(self, vertex):
        """Remove a vertex and all its edges."""
        if vertex in self._adj_list:
            del self._adj_list[vertex]
            for v in self._adj_list:
                self._adj_list[v].pop(vertex, None)
            print(f"  Vertex '{vertex}' removed.")

    def add_edge(self, v1, v2, weight):
        """Add a weighted edge. If undirected, adds both directions."""
        if v1 not in self._adj_list:
            self.add_vertex(v1)
        if v2 not in self._adj_list:
            self.add_vertex(v2)
        self._adj_list[v1][v2] = weight
        if not self._directed:
            self._adj_list[v2][v1] = weight
        direction = "->" if self._directed else "--"
        print(f"  Edge added: {v1} {direction} {v2} (weight={weight})")

    def remove_edge(self, v1, v2):
        """Remove a weighted edge."""
        if v1 in self._adj_list and v2 in self._adj_list[v1]:
            del self._adj_list[v1][v2]
            if not self._directed:
                self._adj_list[v2].pop(v1, None)
            print(f"  Edge removed: {v1} -- {v2}")

    def get_weight(self, v1, v2):
        """Get the weight of the edge between v1 and v2."""
        if v1 in self._adj_list and v2 in self._adj_list[v1]:
            return self._adj_list[v1][v2]
        return None

    def dijkstra(self, start):
        """
        Dijkstra's algorithm to find shortest paths from start to all vertices.
        Returns a dictionary of {vertex: shortest_distance}.

        How it works:
        1. Set distance to start = 0, all others = infinity
        2. Visit the unvisited vertex with smallest distance
        3. Update distances to its neighbors
        4. Repeat until all vertices visited
        """
        if start not in self._adj_list:
            print(f"  Vertex '{start}' not in graph.")
            return {}

        distances = {v: float('inf') for v in self._adj_list}
        distances[start] = 0
        visited = set()
        previous = {v: None for v in self._adj_list}

        while len(visited) < len(self._adj_list):
            # Find unvisited vertex with smallest distance
            current = None
            for v in self._adj_list:
                if v not in visited:
                    if current is None or distances[v] < distances[current]:
                        current = v
            if current is None or distances[current] == float('inf'):
                break

            visited.add(current)
            for neighbor, weight in self._adj_list[current].items():
                new_dist = distances[current] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current

        return distances

    def shortest_path(self, start, end):
        """
        Find the shortest path from start to end using Dijkstra.
        Returns (distance, path_list).
        """
        if start not in self._adj_list or end not in self._adj_list:
            return float('inf'), []

        distances = {v: float('inf') for v in self._adj_list}
        distances[start] = 0
        visited = set()
        previous = {v: None for v in self._adj_list}

        while len(visited) < len(self._adj_list):
            current = None
            for v in self._adj_list:
                if v not in visited:
                    if current is None or distances[v] < distances[current]:
                        current = v
            if current is None or distances[current] == float('inf'):
                break
            if current == end:
                break
            visited.add(current)
            for neighbor, weight in self._adj_list[current].items():
                new_dist = distances[current] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current

        # Reconstruct path
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = previous[node]
        path.reverse()

        if distances[end] == float('inf'):
            return float('inf'), []
        return distances[end], path

    def display(self):
        """Print the adjacency list with weights."""
        graph_type = "Directed" if self._directed else "Undirected"
        print(f"\n  Weighted {graph_type} Graph (Adjacency List):")
        for vertex in sorted(self._adj_list):
            edges = ", ".join(
                f"{n}(w={w})" for n, w in sorted(self._adj_list[vertex].items())
            )
            print(f"    {vertex} -> [{edges}]")

    def __str__(self):
        lines = []
        for v in sorted(self._adj_list):
            edges = ", ".join(
                f"{n}(w={w})" for n, w in sorted(self._adj_list[v].items())
            )
            lines.append(f"  {v} -> [{edges}]")
        return "Weighted Graph:\n" + "\n".join(lines)


# ============================================================
# Demonstration
# ============================================================

def demo_undirected_graph():
    """Demonstrate Undirected Graph with a friendship network example."""
    print("=" * 60)
    print("DEMO 1: Undirected Graph - Friendship Network")
    print("=" * 60)
    print("\nScenario: Model friendships between people.")
    print("If Alice is friends with Bob, Bob is also friends with Alice.\n")

    g = UndirectedGraph()

    # Add friendships
    print("Adding vertices and edges:")
    g.add_edge("Alice", "Bob")
    g.add_edge("Alice", "Charlie")
    g.add_edge("Bob", "Diana")
    g.add_edge("Charlie", "Diana")
    g.add_edge("Diana", "Eve")

    g.display()

    # Check connections
    print(f"\n  Alice and Bob are friends: {g.has_edge('Alice', 'Bob')}")
    print(f"  Alice and Eve are friends: {g.has_edge('Alice', 'Eve')}")
    print(f"  Alice's friends: {sorted(g.get_neighbors('Alice'))}")

    # Traversals
    print(f"\n  BFS from Alice: {g.bfs('Alice')}")
    print(f"  DFS from Alice: {g.dfs('Alice')}")

    # Remove edge
    print("\nRemoving edge Alice -- Charlie:")
    g.remove_edge("Alice", "Charlie")
    g.display()
    print()


def demo_directed_graph():
    """Demonstrate Directed Graph with a task dependency example."""
    print("=" * 60)
    print("DEMO 2: Directed Graph - Task Dependencies")
    print("=" * 60)
    print("\nScenario: Model task prerequisites in a project.")
    print("Task A -> Task B means A must be done before B.\n")

    g = DirectedGraph()

    # Task dependencies
    print("Adding task dependencies:")
    g.add_edge("Design", "Implement")
    g.add_edge("Design", "Test Plan")
    g.add_edge("Implement", "Test")
    g.add_edge("Test Plan", "Test")
    g.add_edge("Test", "Deploy")
    g.add_edge("Requirements", "Design")

    g.display()

    # Check dependencies
    print(f"\n  Design -> Implement exists: {g.has_edge('Design', 'Implement')}")
    print(f"  Implement -> Design exists: {g.has_edge('Implement', 'Design')}")
    print(f"  In-degree of Test: {g.in_degree('Test')} (prerequisites)")
    print(f"  Out-degree of Design: {g.out_degree('Design')} (enables)")

    # Cycle detection
    print(f"\n  Has cycle: {g.has_cycle()}")

    # Topological sort (execution order)
    order = g.topological_sort()
    print(f"  Topological order (execution sequence): {order}")

    # BFS from Requirements
    print(f"  BFS from Requirements: {g.bfs('Requirements')}")
    print()


def demo_weighted_graph():
    """Demonstrate Weighted Graph with a city distance/GPS example."""
    print("=" * 60)
    print("DEMO 3: Weighted Graph - City Distances (GPS)")
    print("=" * 60)
    print("\nScenario: Find shortest travel routes between cities.")
    print("Weights represent distances in kilometers.\n")

    g = WeightedGraph(directed=False)

    # City connections with distances
    print("Adding city connections:")
    g.add_edge("Hong Kong", "Shenzhen", 30)
    g.add_edge("Hong Kong", "Macau", 65)
    g.add_edge("Shenzhen", "Guangzhou", 140)
    g.add_edge("Macau", "Guangzhou", 145)
    g.add_edge("Guangzhou", "Changsha", 660)
    g.add_edge("Shenzhen", "Changsha", 780)

    g.display()

    # Dijkstra's shortest paths from Hong Kong
    print("\n  Shortest distances from Hong Kong (Dijkstra):")
    distances = g.dijkstra("Hong Kong")
    for city, dist in sorted(distances.items()):
        print(f"    Hong Kong -> {city}: {dist} km")

    # Shortest path from Hong Kong to Changsha
    dist, path = g.shortest_path("Hong Kong", "Changsha")
    print(f"\n  Shortest path Hong Kong -> Changsha:")
    print(f"    Path: {' -> '.join(path)}")
    print(f"    Total distance: {dist} km")

    # Show edge weight
    w = g.get_weight("Hong Kong", "Shenzhen")
    print(f"\n  Weight of Hong Kong -- Shenzhen: {w} km")
    print()


def main():
    """Run all graph demonstrations."""
    print("\n" + "#" * 60)
    print("  GRAPH DATA STRUCTURE - DEMONSTRATION")
    print("  COMP8090SEF Task 2 Self Study")
    print("#" * 60 + "\n")

    demo_undirected_graph()
    demo_directed_graph()
    demo_weighted_graph()

    print("=" * 60)
    print("All graph demonstrations completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
