def add(x,y):
    result=x+y
    print('add:',result)
    def sub():
        result=x-y
        print('sub:',result)
        def mul():
            result=x*y
            print('mul:',result)
            def div():
                result=x/y
                print('div:',result)
                def mod():
                    result=x%y
                    print('mod:',result)
                    def floor():
                        result=x//y
                        print('floor:',result)
                    floor()
                mod()
            div()
        mul()
    sub()
    
