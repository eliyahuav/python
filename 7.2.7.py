
# ----------arrow----------------------------------------
def arrow(my_char, max_length):
    
    arrow_string = ''

    for counter in range(1, max_length * 2):
        if counter <= max_length:
            arrow_string += f"{(my_char + ' ') * counter}\n"
        else:
            arrow_string += f"{(my_char + ' ') * (max_length * 2 - counter)}\n"

    return arrow_string
# ----------main----------------------------------------
def main():

    print(arrow('*', 5))

if __name__ == "__main__":
    main()