from Matrix import Matrix
from PIMatrix import PIMatrix

class KeyMatrix(Matrix):
    def __init__(self, n=8,m=7):
        super().__init__(n, m)
        piMatrix = PIMatrix().value
        steps = {
            -1:8,
            -2:8,
            -3:8,
            -4:4,
        }
        belowSteps = {
            0 : 8,
            1 : 8,
            2 : 8,

        }
        count, minus = 0, 0
        stepsIterator = iter(steps.items())
        belowStepsIterator = iter(belowSteps.items())
        output = []
        iterator = stepsIterator
        try:
            for x in piMatrix:
                for y in x:
                    if count == 0:
                        minus = next(stepsIterator)[0]
                        count = steps[minus]
                    output.append(y+minus)
                    count -= 1
        except StopIteration:
            count, minus = 0, 0
            pass
        try:
            piMatrix.reverse()
            for x in piMatrix:
                for y in x:
                    if count == 0:
                        minus = next(belowStepsIterator)[0]
                        count = belowSteps[minus]
                    output.append(y+minus)
                    count -= 1
        except StopIteration:
            pass
        output.extend([28,20,12,4])
        outputIterator = iter(output)
        try:
            for x in range(0,n):
                for y in range(0,m):
                    self.value[x][y] = next(outputIterator)
        except StopIteration:
            pass
