def calculate_discount(price,discount_percent):
    price=float(price)
    discount_percent=float(discount_percent)
    if discount_percent>=20:
        discount=(price*discount_percent/100)
        final_price=(price-discount)
        print('Final price after discount was applied: ',final_price)
    else:
        print('Final price after no discount was applied: ',price) 

user_input1=input('Enter the original price:')
user_input2=input('Enter the discount percentage:')  

calculate_discount(user_input1,user_input2)         