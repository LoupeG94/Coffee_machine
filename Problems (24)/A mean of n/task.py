def mean(a, n):
    # Find sum of array element
    sum = 0
    for i in range(n):
        sum += a[i]

    return sum/n


# Driver code
number = [int(x) for x in input().split()]
n = len(number)
print(mean(number, n))