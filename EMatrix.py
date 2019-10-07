from Matrix import Matrix


class EMatrix(Matrix):
    def __init__(self, n=6,m=8):
        super().__init__(n, m)
        values = [32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1]

        valueIter = iter(values)
        for x in range(0,n):
            for y in range(0,m):
                self.value[x][y] = next(valueIter)

