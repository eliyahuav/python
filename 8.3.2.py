
	
	
# ---------main------------------------------------------
def main():

    intel = {"first_name" : "Mariah",
            "last_name" :	"Carey",
            "birth_date" : "27.03.1970",
            "hobbies" : ["Sing", "Compose", "Act"]}
    
    number = (int)(input("plese enter number betwean 1 - 7")) #input


    if(number == 1):
        print(intel["last_name"])
    elif(number == 2):
        print(intel["birth_date"])
    elif(number == 3):
        print(len(intel["hobbies"]))
    elif(number == 4):
        print(intel["hobbies"][2])
    elif(number == 5):
        (intel["hobbies"].append("Cooking"))
        print((intel["hobbies"]))
    # elif(number == 6): #??????????????????????????????
    #     tappleBirthday =(" {day}'.'{month}'.'{year}").format()

    elif(number == 7):
        intel["age"] = 53 #add number
        print(dict(key for key in intel)) #?
              
if __name__ == "__main__":
    main()