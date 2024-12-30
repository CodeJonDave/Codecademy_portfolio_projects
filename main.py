from title import title as TITLE

def main():
    print(TITLE)
    while(True):
        username = input("Welcome! please What is your fist and last name.").strip()
        if " " in username and len(username.split()) == 2:
            break
        print("Improper format: first and last name please: ")
    first_name, last_name = username.split(" ",1)
    print("We are ready for you.\nPlease take a moment and think about what you would like ask the fates today.")

if __name__ == "__main__":
    main()