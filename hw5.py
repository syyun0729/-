def read_single_digit(n):
    if n == 1:
        return "일"
    if n == 2:
        return "이"
    if n == 3:
        return "삼"
    if n == 4:
        return "사"
    if n == 5:
        return "오"
    if n == 6:
        return "육"
    if n == 7:
        return "칠"
    if n == 8:
        return "팔"
    if n == 9:
        return "구"
    if n == 0:
        return "영"

def read_number(n):
    hundreds = n // 100
    tens = (n % 100) // 10
    ones = n % 10

    return f"{read_single_digit(hundreds)} {read_single_digit(tens)} {read_single_digit(ones)}"

num = int(input("세 자리 정수 입력: "))
print(read_number(num))















        
    
