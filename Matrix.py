class Matrix:
    def __init__(self, n, m):
        self.n = n;
        self.m = m;
        self.value = [[0] * m for i in range(n)]

    def printMatrix(self):
        for i in self.value :  
            print(i, end="\n") 

