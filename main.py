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
    for k in range(len(families)):
        for n in range(len(families[k])):
            index = letters.index(families[k][n]) + len(families)
            matrix[index][k] = 1
            matrix[k][index] = 1
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


def print_result(letters, lenght):
    edges = []
    with open("out.txt", 'w') as file:
        for i in range(len(matrix[0])):
            if matching[i] != -1:
                edges.append((i, matching[i]))
        if len(edges) != 2 * lenght:
            file.write('N')
        else:
            file.write('Y\n')
            for j in range(lenght):
                file.write(letters[edges[j][1] - lenght] + ' ')


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
    print_result(letters, len(family))


if __name__ == '__main__':
    main()
