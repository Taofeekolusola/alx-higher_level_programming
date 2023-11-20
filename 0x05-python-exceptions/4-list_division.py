#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            num1 = my_list_1[i] if i < len(my_list_1) else 0
            num2 = my_list_2[i] if i < len(my_list_2) else 0

            float_num1 = float(num1)
            float_num2 = float(num2)

            if float_num2 == 0:
                raise ZeroDivisionError("division by 0")

            result_list.append(float_num1 / float_num2)

        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        finally:
             pass

             return result_list
