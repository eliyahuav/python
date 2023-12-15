def seven_boom(end_number):
    arr = []
    i = 0
    while i <= end_number:
        if(( i % 7 == 0) or ('7' in str(i))):
            arr.append("boom")
        else:
            arr.append(i)

        i += 1

    return arr


def main():

    print(seven_boom(17))

if __name__ == "__main__":
    main()