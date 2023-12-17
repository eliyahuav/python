def mult_tuple(tuple1, tuple2):
    new_tuple = ()
    for i in tuple1:
        for j in tuple2:
            new_tuple += ((i, j),(j, i)) 

    return new_tuple


# ----------main----------------------------------------
def main():

    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))

if __name__ == "__main__":
    main()