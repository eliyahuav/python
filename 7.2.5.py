def sequence_del(my_str):
    
    word = my_str[0]
    tmp = my_str[0]
    
    for letter in my_str:
        if letter != tmp:
            tmp = letter
            word += tmp
    
    return word



def main():

    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print(sequence_del("SSSSsssshhhh"))
    print(sequence_del("Heeyyy   yyouuuu!!!"))

if __name__ == "__main__":
    main()