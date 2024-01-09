n, k = 5, 3
a = [1, 2, 3, 4, 5]

b = []

def combi(start, b) :
    if len(b) == k :
        print(b)
        return

    for i in range(start + 1, n) :
        b.append(i)
        combi(i, b)
        b.pop()

    return

combi(-1, b)