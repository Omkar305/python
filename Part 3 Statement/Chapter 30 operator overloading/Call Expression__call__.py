class Employee:

    def __call__(self,*pargs,**kargs):
        print('Caller:',pargs,kargs)

omkar=Employee()
omkar(19,29,name='Omkar Savardekar',job='CEO',pay=250000000)

rashi=Employee()
rashi(name='Rashi Shelar',job='CEO',pay=250000000)
