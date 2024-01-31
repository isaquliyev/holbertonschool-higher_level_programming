#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]
            result = 0
            try:
                value_1 = float(value_1)
                value_2 = float(value_2)
                try:
                    result = my_list_1[i] / my_list_2[i]
                except Exception:
                    print("division by 0")
            except Exception:
                print("wrong type")
            finally:
                new_list.append(result)
    except Exception:
        print("out of range")
    finally:
        return new_list
