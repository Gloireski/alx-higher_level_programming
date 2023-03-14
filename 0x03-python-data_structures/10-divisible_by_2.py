def divisible_by_2(my<F5>_list=[]):
    new_list = []
    for i in range(0, len(my_list)):
        if (my_list[i] % 2) == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list        
