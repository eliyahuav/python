def numbers_letters_count(my_str):

    num = 0
    characters = 0

    for letter in my_str:
        if letter.isdigit():
            num += 1
        else:
            characters += 1
    return [num, characters]

def main():

    print(numbers_letters_count("Python 3.6.3"))

if __name__ == "__main__":
    main()