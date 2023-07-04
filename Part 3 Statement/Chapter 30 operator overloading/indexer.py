class Indexer:
    def __init__(self,list1):
        self.list1=list1

    def __getitem__(self,index):
        print('getitem',index)
        print(self.list1[index])

x=Indexer([1,5,3,6,5,4,8,9,10])
x[2:6]
x[2]
