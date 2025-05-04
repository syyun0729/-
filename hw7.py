d = {}  

while True:
    item = input('상품명? ')
    if item == '':
        break
    num = int(input('수량은? '))
    d[item] = num
    print(f'장바구니에 {item}가(이) {num}개 담겼습니다.')

print(f'\n>>> 장바구니 보기: {d}')

print('\n[검색]')
object = input('장바구니에서 확인하고자 하는 상품은? ')
if object in d:
    print(f'{object}은(는) {d[object]}개 담겨 있습니다.')
else:
    print(f'{object}은(는) 장바구니에 없습니다.')
    
