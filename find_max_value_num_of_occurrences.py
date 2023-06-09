def find_max_value_num_of_occurrences(target_list):
    max_value = 0
    for i in target_list:
        if max_value < i:
            max_value = i

    num_occurrences = 0
    for i in target_list:
        if i == max_value:
            num_occurrences += 1


    print(f"The max value is {max_value} and the number of occurrences for it is {num_occurrences}")

        


if __name__ == "__main__":
    target_list = [11, 8, 3, 11, 4, 8, 11]
    find_max_value_num_of_occurrences(target_list)