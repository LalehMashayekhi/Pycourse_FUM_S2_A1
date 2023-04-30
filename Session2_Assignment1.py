side_1=int(input('Please Enter a number as triangle side: '))

side_2=int(input('Please Enter a number as triangle side: '))

side_3=int(input('Please Enter a number as triangle side: '))

if side_1<side_2+side_3 and side_2<side_1+ side_3 and side_3<side_1+ side_2:
    print('You can have a triangle')
    
else:
    print('The numbers you have entred can not form a triangle')