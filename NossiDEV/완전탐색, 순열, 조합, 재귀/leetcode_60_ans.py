def getPermutation(n, k)  :
    orders = [0 for _ in range(n)]

    def get_factorial(n):
        if n == 0 or n == 1:
            return 1

        return n * get_factorial(n - 1)

    factorial = [get_factorial(n) for n in range(n + 1)]

    k -= 1
    tmp = [i for i in range(n + 1)]

    for i in range(n):
        count = k // factorial[n - 1 - i] + 1
        k = k % factorial[n - 1 - i]
        orders[i] = str(tmp[count])
        tmp.pop(count)

    return "".join(orders)

getPermutation(4, 14)