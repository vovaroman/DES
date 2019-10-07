from Matrix import Matrix


class PIMatrix(Matrix):
    def __init__(self, n=8,m=8):
        super().__init__(n, m)
        evenList = [x for x in range(1,65) if x % 2 == 0]
        oddList = [x for x in range(1,65) if x % 2 == 1]
        oddIterator = iter(oddList)
        evenIterator = iter(evenList)
        for x in range(7,-1, -1):
           for y in range(0,4):
               self.value[y][x] = next(evenIterator)
        for x in range(7,-1, -1):
           for y in range(4,8):
               self.value[y][x] = next(oddIterator)

        
