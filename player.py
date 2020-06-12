import pandas as pd

class Player:

    def __init__(self,cashStack,shares,algorithm,randomWalk):
        self.cashStack=cashStack
        self.shares=shares
        self.algorithm=algorithm
        self.randomWalk=randomWalk
        self.stateHistory=[]
        self.transactionHistory=[]

    def marketTick(self):
        self.randomWalk.next()
        self.algorithm(self)
        self.stateHistory.append([self.cashStack,self.shares,self.randomWalk.currentValue()])

    def buyShares(self,amount):
        self.cashStack=self.cashStack-self.randomWalk.currentValue()*amount
        self.shares=self.shares+amount
        self.transactionHistory.append(['buy',amount,self.randomWalk.currentValue(),len(self.randomWalk.history)-1])

    def sellShares(self,amount):
        self.cashStack=self.cashStack+self.randomWalk.currentValue()*amount
        self.shares=self.shares-amount
        self.transactionHistory.append(['sell',amount,self.randomWalk.currentValue(),len(self.randomWalk.history)-1])

    def stateReport(self):
        if len(self.stateHistory)==0:
            return pd.DataFrame() 
        df=pd.DataFrame(self.stateHistory)
        df.columns=['cash','shares','share_price']
        return df

    def transactionReport(self):
        if len(self.transactionHistory)==0:
            return pd.DataFrame()
        df=pd.DataFrame(self.transactionHistory)
        df.columns=['transaction_type','share_quantity','share_price','time']
        return df
    

    
