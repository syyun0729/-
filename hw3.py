def get_fixed_price(discount_rate, discounted_price):
    original_price = discounted_price / (1 - discount_rate / 100) 
    return original_price


discount_rate = float(input('할인율은? '))

discounted_price_a = float(input('A상품의 할인된 가격은? '))
discounted_price_b= float(input('B상품의 할인된 가격은? '))

original_price_a = get_fixed_price (discount_rate, discounted_price_a)
original_price_b = get_fixed_price (discount_rate, discounted_price_b)

print ('A상품의 정가는 ', original_price_a, '원')
print('B상품의 정가는', original_price_b, '원')
