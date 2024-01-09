a = [1, 2, 3]
n, r = 3, 3
def printAll() :
    for i in range(r) :
        print(a[i], end = " ")

    print()
# n 3
# depth0 i 0 1v 2
# depth1 i 1v 2
# depth2 i 2v
#
def makePermutation(n, r, depth) :
    if r == depth :
        printAll()
        return

    for i in range(depth, n) :
        print(i, " : ", depth, "를 바꾼다!")
        a[i], a[depth] = a[depth], a[i]
        makePermutation(n, r, depth + 1)
        print(i, " : ", depth, "를 다시 바꾼다!")
        a[i], a[depth] = a[depth], a[i]

    return

makePermutation(n, r, 0)

