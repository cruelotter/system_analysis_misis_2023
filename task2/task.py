
def task(data: str):
    
    data = [row.split(',') for row in data.split('\n')]
    graph = [list(map(int, el)) for el in data]
    
    vertex_set = set()
    for row in data:
        vertex_set.update(row)
    
    matrix = [[0]*len(vertex_set) for i in range(len(vertex_set))]
    for row in graph:
        matrix[row[0]-1][row[1]-1] = 1
        matrix[row[1]-1][row[0]-1] = -1
    
    # непосредственное управление
    r1 = []
    for i in range(len(matrix)):
        for v in matrix[i]:
            if v == 1: 
                r1.append(i+1)
                break

    # непосредственное подчинение
    r2 = []
    for i in range(len(matrix)):
        for v in matrix[i]:
            if v == -1: 
                r2.append(i+1)
                break
            
    # опосредственное управление
    r3 = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                for el in matrix[j]:
                    if el == 1:
                        r3.append(i+1)
                        break
    
    # опосредственное подчинение
    r4 = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == -1:
                for el in matrix[j]:
                    if el == -1:
                        r4.append(i+1)
                        break
            
    # соподчинение
    r5 = []
    for i in range(len(matrix)):
        if matrix[i].count(1) > 1:
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    r5.append(j+1)
                    
    return [r1, r2, r3, r4, r5]


with open('task2/graph.csv', 'r') as file:
    raw_data = file.read()

    
print(task(raw_data))