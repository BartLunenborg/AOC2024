from collections import defaultdict

class Graph():
    def __init__(self, input):
        self.edges = defaultdict(set)
        for a, b in (line.split("-") for line in input):
            self.edges[a].add(b)
            self.edges[b].add(a)
        self.nodes = set(self.edges)

    def triples(self):
        return {(a, b, c) for a in self.nodes for b in self.edges[a] if b > a for c in self.edges[b] if c > b and a in self.edges[c]}

    # Finds the largest clique using Bron-Kerbosch: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
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

G = Graph([line for line in open("input/23.in").read().strip().split("\n")])
one = sum(any(t[0] == "t" for t in triple) for triple in G.triples())
two = ",".join(sorted(G.bron_kerbosch(set(), G.nodes.copy(), set())))

print(f"Part one: {one}")
print(f"Part two: {two}")
