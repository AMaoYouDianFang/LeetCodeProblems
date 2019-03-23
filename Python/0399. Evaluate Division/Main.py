class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}
        def build_graph(equations, values):
            def add_edge(f, t, val):
                if f in graph:
                    graph[f].append((t, val))
                else:
                    graph[f] = [(t, val)]
            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1/value) #把变都存入到dic a : c 10
                                         #             c : a 1/10

        def find_path(query):
            b, e = query
            if b not in graph or e not in graph:
                return -1.0
