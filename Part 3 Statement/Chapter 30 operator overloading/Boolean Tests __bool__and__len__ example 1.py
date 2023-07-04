class Test:
    def __bool__(self):
        return False

x=Test()
print(bool(x))

if x:
    print('true')
else:
    print('false')
