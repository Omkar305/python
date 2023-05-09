#Formatting Method

temp1='{0},{1},{2}'.format('Omkar','Makrand','Rashi')
print(temp1)

temp2='{1},{2},{0}'.format('Omkar','Makrand','Rashi')
print(temp2)

temp3='Name:{Name},Age:{Age},Salary:{Salary}'.format(Name='Omkar',Age=23,Salary=15000)
print(temp3)

temp4='Age:{Age},Salary:{Salary},Name:{Name}'.format(Name='Omkar',Age=24,Salary=20000)
print(temp4)

temp5='{Motto},{0},{Food}'.format('Jam',Motto='Kissan',Food='Baklava')
print(temp5)

temp6='{},{},{Name}'.format('Kissan','Jam',Name='Baklava')
print(temp6)

temp7='{Name},{0[Age]},{1[2]}'.format({'Name':'Omkar','Age':23,'Salary':15000},[56,79,22],Name='Jam')
print(temp7)
