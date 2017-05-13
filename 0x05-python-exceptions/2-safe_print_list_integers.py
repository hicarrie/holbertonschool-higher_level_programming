#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    length = sum(1 for x in my_list)
    if length == x:
        x = x - 1
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except ValueError:
            count = count - 1
            pass
        except IndexError:
            count = count - 1
            pass
        finally:
            count = count + 1
    print()
    return count
