def display_multiplication_range(start, end):
    for i in range(1, 10):  
        for dan in range(start, end + 1):
            print(f'{dan} * {i} = {dan * i:2}', end='\t')
        print()  


display_multiplication_range(2, 5)
print()  

display_multiplication_range(6, 9)
