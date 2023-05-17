def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
        discount = float (discount) 
        max_discount = int (max_discount)
    except (ValueError, TypeError):
        return 'некорректные аргументы'    
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

    
    
print(discounted('fghfgh',20,2))    