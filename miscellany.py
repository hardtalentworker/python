//декоратор
def deco(func):
    def decoInner():
        print('1')
        func()
        print('2')
    return decoInner

@deco
def BubbleSort(food="--food--"):
    print(food)

BubbleSort()
