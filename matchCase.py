a = int(input("enter your favourite number : "))

match a:
    case 1:
        print("case is 1")
    case 2:
        print("case is 2")
    case 3:
        print("case is 3")
    case 4:
        print("case is 4")
    case 5:
        print("congratulations! you are lucky man!!")
    case _:
        print("no match found")
