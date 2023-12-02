a = []
a = [x for x in range(100, 0, -1)]
print(a)

def BubbleSort(a):
    lastElementIdx = len(a)-1
    for x in range(lastElementIdx, 0, -1):
        for y in range(x):
            if a[y] > a[y + 1]:
                a[y], a[y + 1] = a[y + 1], a[y]
