#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(0, list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            result.append(0)
            print("wrong type")
            continue
        except ZeroDivisionError:
            result.append(0)
            print("division by zero")
            continue
        except IndexError:
            result.append(0)
            print("out of range")
            continue
        finally:
            pass
    return result
