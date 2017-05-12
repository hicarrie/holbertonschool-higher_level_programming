#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        length = sum(1 for x in my_list)
        if length < x:
            print(*my_list[:], sep="")
            return length
        else:
            print(*my_list[:x], sep="")
            return x
    except:
        print("An error occurred")
