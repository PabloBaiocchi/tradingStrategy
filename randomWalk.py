import random

class RandomWalk:

    def __init__(self,startValue,maxVariation,varMean,varStdDev):
        self.maxVariation=maxVariation
        self.varMean=varMean
        self.varStdDev=varStdDev
        self.history=[startValue]

    def next(self):
        delta=random.gauss(self.varMean,self.varStdDev)*self.maxVariation
        self.history.append(self.history[-1]+delta)
        return self.history[-1]
        
    def currentValue(self):
        return self.history[-1]
