class IndexSetter:
    def __init__(self,data):
        self.data=data

    def __setitem__(self,index,value):
        self.data[index]=value

x=IndexSetter([10,5,2,6,5,9,8,5])
x[2:5]=[55,66,77]
print(x.data)
