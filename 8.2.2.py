def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x:(float)(x[1]))
    # lambda x:(float)(x[1]) = <get x, return (float)(x[1]>)



products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))