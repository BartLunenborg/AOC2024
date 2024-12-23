from collections import defaultdict

class Graph():
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(set)

    def add(self, connection):
        a, b = connection.split("-")
        self.nodes.add(a)
        self.nodes.add(b)
        self.edges[a].add(b)
        self.edges[b].add(a)

    def triples(self):
        triples = set()
        for a in self.nodes:
            for b in self.edges[a]:
                if b > a:
                    for c in self.edges[b]:
                        if c > b and a in self.edges[c]:
                            triples.add((a, b, c))
        return triples

    # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    def bron_kerbosch(self, R, P, X):
        if not P and not X:
            return R

        best = set()
        for v in P.copy():
            new = self.bron_kerbosch(R | {v}, P & self.edges[v], X & self.edges[v])
            P.remove(v)
            X.add(v)
            if len(new) > len(best):
                best = new

        return best

    def largest_clique(self):
        best = self.bron_kerbosch(set(), self.nodes.copy(), set())
        return sorted(best)

file, G = open("./input/23.in").read().strip(), Graph()
for line in file.split("\n"):
    G.add(line)

one = sum(any(s[0] == "t" for s in t) for t in G.triples())
two = ",".join(G.largest_clique())

print(f"Part one: {one}")
print(f"Part two: {two}")
