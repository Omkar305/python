#Non-local

a=23
b=45
c=91
def f1():
    h=34
    def f2():
        nonlocal h
        h=97
        print('h:',h)
        def f3():
            global a
            a=67
            print('a:',a)
            def f4():
                global b
                b=57
                print('b:',b)
                def f5():
                    global c
                    c=84
                    print('c:',c)
                f5()
            f4()
        f3()
    f2()
f1()
            
