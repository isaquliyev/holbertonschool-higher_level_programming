#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]
            result = 0
            try:
                if isinstance(value_1, str) or isinstance(value_1, str):
                    new_list.append(0)
                    raise Exception
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
        while len(new_list) != list_length:
            new_list.append(0)
            if len(new_list) == list_length:
                print("out of range")
    finally:
        return new_list
