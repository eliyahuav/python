# ---------func sort_str------------------------------------------
def sort_str(str_arr):
    word = ""
    arr = []
    for letter in str_arr:
        if letter == ',':
            arr.append(word)
            word = ""
        else:
            word += letter

    arr.append(word)
    
    return arr
# ---------func sort_str------------------------------------------
def print_derry(arr):
    for derry in arr:
        print(derry)
# ---------func check_amount_of_derrys------------------------------------------
def check_amount_of_derrys(arr):
    num = 0
    for derry in arr:
        num += 1
    print(num)
# ---------func print_if_exists------------------------------------------
def print_if_exists(arr, derry):
    if derry in arr:
        print(True)
    else:
        print(False)
# ---------func print_amount_derry------------------------------------------
def print_amount_derry(arr, wanted_derry):
    amount = 0
    for derry in arr:
        if derry == wanted_derry:
            amount += 1
    return amount
# ---------func delete_derry_from_arr------------------------------------------
def delete_derry_from_arr(arr, wanted_derry):
    amount = 0
    for derry in arr:
        if derry == wanted_derry:
            del arr[amount]
        amount += 1
# ---------func add_derry_to_arr------------------------------------------
def add_derry_to_arr(arr, new_derry):
    arr.append(new_derry)     
# ---------func print_eligal_derrys------------------------------------------
def print_eligal_derrys(arr):
    for derry in arr:
        if len(derry) <= 3 or not(derry.isalpha()):
            print(derry)
# ---------func delete_duplicate_deries------------------------------------------
def delete_duplicate_deries(arr):

    for derry in arr:
        if arr.count(derry) > 1:
           arr.remove(derry)
# ---------main------------------------------------------
def main():

    str_arr = "Milk,Cottage,Tomatoes" #Given
    number = (int)(input("plese enter number betwean 1 - 9")) #input

    arr = sort_str(str_arr) #sort Given str

    exit_ = True
    while(exit_):
        if(number == 1):
            print_derry(arr)
        elif(number == 2):
            check_amount_of_derrys(arr)
        elif(number == 3):
            derry = input("please enter name of derry")
            print_if_exists(arr, derry)
        elif(number == 4):
            derry = input("please enter name of derry")
            print(print_amount_derry(arr, derry))
        elif(number == 5):
            derry = input("please enter name of derry")
            delete_derry_from_arr(arr, derry)
        elif(number == 6):
            derry = input("please enter new derry to add")
            add_derry_to_arr(arr, derry)
            # just for check
            # print_derry(arr)
        elif(number == 7):
            print_eligal_derrys(arr)
        elif(number == 8):
            delete_duplicate_deries(arr)
            print_derry(arr)
        elif(number == 9):
            exit_ = False

if __name__ == "__main__":
    main()