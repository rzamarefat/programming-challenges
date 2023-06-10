"""
Find the maximum lenght of consecutive occurrences of the number one
"""

def find_max_cons_ones(target_list):
    len = 0
    len_holder = []
    for i in target_list:
        if i == 1:
            len += 1
        else:
            len = 0

        len_holder.append(len)

    max_len = max(len_holder)

    print(f"The maximum lenght of occurrences of the number 1 is {max_len}")


if __name__ == "__main__":
    target_list = [1,1,0,1,1,1] #3
    target_list = [1,0,1,1,0,1] #2
    find_max_cons_ones(target_list)