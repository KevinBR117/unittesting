def square(x):
    return x * x


def triple(x):
    return 3 * x


def minNum(arr):
    min = arr[0]
    for ele in arr:
        if ele < min:  # la condición deber ser "<"
            min = ele
    return min


def sumArray(arr):
    total = 0  # se inicializa en "0" porque al comenzar en una posición del array en el for se sumaria otra vez esa posición
    for ele in arr:
        total += ele
    return total


def bubbleSort(arr):
    n = len(arr)  # a la dimension del array no se le resta "-1"
    for i in range(n):
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  # falto retornar el array

# a = [5,9,3]
# n =3
# ciclo 0 al 2
#     ciclo 0 al 2
#       5 > 9 = no
#     cilco 1 al 2
#       9 > 3 = si
#       arr[1], arr[2] = arr[2], arr[1]
#       9, 3 = 3, 9

# ciclo 1 al 2
#     ciclo 0 al 1
#       5 > 3 = si
#     ciclo 1 al 1
#       


# for i in range(5):
#     print(i)

if __name__ == "__main__":
    print(bubbleSort([5,9,3]))
