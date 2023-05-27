#Inline functions

#add
add=lambda x,y:x+y
print(add(10,20))


#even
even=lambda x:x%2==0
print(even(11))


#list
list1=[
    lambda x:x*2,
    lambda x,y=10:x==y,
    lambda x:x<4
    ]
for i in range(len(list1)):
    print(list1[i](10))
    

#sub
sub=lambda x,y:x-y
print(sub(-50,30))


#mul
mul=lambda x,y:x*y
print(mul(10,5))


#div
div=lambda x,y:x/y
print(div(15,-2))


#mod
mod=lambda x,y:x%y
print(mod(7,3))


#lower
lower=(lambda x,y:x if x<y else y)
print(lower(10,20))


#list_map
list1=(10,20,30,40)
list_map=list(map(lambda x:x/2,list1))
print(list_map)


#list_filter

list2=[10,21,30,41,50]
list_filter=list(filter(lambda x:x%2==0,list2))
print(list_filter)























