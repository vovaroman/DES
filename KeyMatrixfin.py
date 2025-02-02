from Matrix import Matrix


class KeyMatrixfin(Matrix):
    def __init__(self, n=6,m=8):
        super().__init__(n, m)
        values = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

        valueIter = iter(values)
        for x in range(0,n):
            for y in range(0,m):
                self.value[x][y] = next(valueIter)
