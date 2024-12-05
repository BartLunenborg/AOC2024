from collections import defaultdict

class Graph:
    def __init__(self, nums, rules):
        self.nodes = nums
        self.edges = defaultdict(list)
        for num in nums:
            for rule in rules[num]:
                if rule in nums:
                    self.edges[num].append(rule)

    def __topo_sort(self, node, visited, stack):
        visited[node] = True
        for neighbour in self.edges[node]:
            if not visited[neighbour]:
                self.__topo_sort(neighbour, visited, stack)
        stack.append(node)

    def topo_sort(self):
        visited = {node: False for node in self.nodes}
        stack = []
        for node in self.nodes:
            if not visited[node]:
                self.__topo_sort(node, visited, stack)
        return stack[::-1]


file = open("./input/05.in").read().strip()
lines = [line for line in file.split("\n")]
split = lines.index("")

rules = defaultdict(list)
for line in lines[:split]:
    a, b = map(int, line.split("|"))
    rules[a].append(b)

one, two = 0, 0
good_ordering = lambda before, rules: all(rule not in before for rule in rules)
for line in lines[split+1:]:
    nums = list(map(int, line.split(",")))
    mid = len(nums) // 2
    if all(good_ordering(nums[:i], rules[num]) for i, num in enumerate(nums) if num in rules):
        one += nums[mid]
    else:
        g = Graph(nums, rules)
        two += g.topo_sort()[mid]

print(f"Part one: {one}")
print(f"Part two: {two}")
