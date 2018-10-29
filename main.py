class Graph:
    def __init__(self):
        self.parts = []
        self.edges = {}


class Part:
    def __init__(self):
        self.elements = []

    def add(self, node):
        self.elements.append(node)


def build_graph(content, letters):
    global graph
    graph = Graph()
    part_family = Part()
    part_elements = Part()
    for i in range(len(content)):
        part_family.add(i)
        edges = []
        for j in content[i]:
            index = letters.index(j)
            if index not in part_elements.elements:
                part_elements.add(index)
            edges.append(index)
        graph.edges[i] = edges
    graph.parts.append(part_elements)
    graph.parts.append(part_family)


def get_family(content):
    size = int(content[0])
    arr = []
    lines = content.split('\n')
    for i in range(1, size + 1):
        line = lines[i].split()
        multiplicity = []
        for j in range(len(line) - 1):
            multiplicity.append(line[j])
        arr.append(multiplicity)
    return arr


def get_number_nodes(arr):
    letters = set()
    for el in arr:
        for node in el:
            letters.add(node)
    letters = list(letters)
    letters.sort()
    numbers = []
    for i in range(len(letters)):
        numbers.append(i)
    return letters


def build_matrix(families, letters):
    matrix = [[0 for j in range(len(families) + len(letters))] for i in range(len(families) + len(letters))]
    for i in range(len(families)):
        for j in range(len(families[i])):
            index = letters.index(families[i][j]) + len(families[i])
            matrix[index][i] = 1
            matrix[i][index] = 1
    return matrix


def dfs(v):
    if used[v]:
        return False
    used[v] = True
    for num in range(len(matrix[v])):
        if matrix[v][num] == 1:
            if matching[num] == -1 or dfs(matching[num]):
                matching[num] = v
                return True
    return False


def main():
    global graph
    global matching
    global used
    global matrix
    used = []
    matching = dict()
    with open("in.txt") as file:
        data = file.read()
        family = get_family(data)
        letters = get_number_nodes(family)
    matrix = build_matrix(family, letters)
    for q in range(len(family) + len(letters)):
        used.append(False)
    for i in range(len(family) + len(letters)):
        matching[i] = -1
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            used[j] = False
        dfs(i)
    for i in range(len(matrix[0])):
        if matching[i] != -1:
            print(i, " ", matching[i])
    print(matching)


if __name__ == '__main__':
    main()
