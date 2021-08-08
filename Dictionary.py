
from difflib import get_close_matches
import json
# json file is similar to the dictionary in python..:)
data=json.load(open("/home/karuna/Downloads/data.json"))
print("\nLets begin the searching journey...:) ")


def Output(output): #when searched element conveys more than one meaning..!          
    if type(output) ==list:
        print("\nMeaning for the searched element in the dictionary :\n")
        for meanings in output:
            print(meanings)
    else:
        print("\nMeaning for the searched element in the dictionary :\n")
        print(output)


def translate(): 
    while True:
        choice=input("\nPress 'Y'/'y' to begin serach...\nPress 'N'/'n' if you are bored with the searching work..:(( : ")
        
        if choice=='Y' or choice== 'y':
            search=input("\nEnter search element: ")
            search=search.lower()
            
            if search in data:
                output=data[search]
                Output(output)
            
            elif search.title() in data:  #if word in format Tamil
                output=data[search.title()]
                Output(output)
            
            elif search.upper() in data:  #if word in format TAMIL
                output=data[search.upper()]
                Output(output)
            
            elif len(get_close_matches(search,data.keys())) >0:
                print("Did you mean %s instead "%get_close_matches(search,data.keys())[0]) #This is when user types wrong search element by mistake 
                decide=input("Press 'y' for yes and 'n' for  no...")                       #this is another way of string formatting
                if decide == 'y':
                    Output(data[get_close_matches(search,data.keys())[0]])
                elif decide == 'n':
                    print("Word doesn't exists in dictionary..!")
                else:
                    print("Enter valid input : ")

            else:
                print("This word doesn't exists in the dictionary..:(")
        
        elif choice=='N'or choice=='n':
            print("\nHave a good day ahead..dictionary will miss you...:)))\n")
            break
        
        else:
            print("\nEnter valid choice :..><")

if __name__=='__main__':
    translate()