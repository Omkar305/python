#Non-local

w=87
x=19
def f1():
    y=99
    def f2():
        nonlocal y
        y=12
        z=65
        def f3():
            nonlocal z
            z=43
            print('z:',z)
            print('y:',y)
            def f4():
                global w
                w=29
                print('w:',w)
            f4()
        f3()
    f2()
f1()
