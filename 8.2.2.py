
def return_float(one_taple):
    return (float)(one_taple[1])



def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=return_float)
    # lambda x:(float)(x[1]) = <get x, return (float)(x[1]>)
    # lambda x:(float)(x[1]) = return_float



products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))