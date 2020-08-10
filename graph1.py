class Graph:
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Non-Existent Vertex!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, start_index):
        queue_front = [start_index]
        visited = set()

        while len(queue_front) > 0:
            current = queue_front[0]
            queue_front.remove(current)
            if current in visited:
                continue
            else:
                visited.add(current)
                queue_front.extend(self.vertices[current])

        return visited


"""
Breadth-first traversal:
    pick a start node:
"""


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)

g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(4, 3)
g.add_edge(3, 6)
g.add_edge(6, 5)
g.add_edge(5, 4)

# print(g)

print(g.bft(1))