#1. print a one line lambda expression that is going to proint for us a squared list 

lis = [1,2,3,5,4,6,8,7]

print(list(map(lambda lis: lis*lis,lis)))

#output : [1, 4, 9, 25, 16, 36, 64, 49]


#2. sort the list of tuples based on their second item using lambda expressions

another_list = [(0,2),(5,8),(7,3),(8,5),(2,-2),(5,0)]

another_list.sort(key=lambda x: x[1])

print(another_list)

'''
outputs :

[1, 4, 9, 25, 16, 36, 64, 49]
[(2, -2), (5, 0), (0, 2), (7, 3), (8, 5), (5, 8)]

'''