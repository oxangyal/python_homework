try:
    diary = open("diary.txt", "a")
    str = input("What happened today?")
    diary.write(str + "\n")
    while str != "done for now":
        str = input("What else?")
        diary.write(str + "\n")
    diary.close()
except:
    print("\nAn exception occurred.")
