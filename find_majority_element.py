"""
Given a list of integer numbers, find the element with the highest number of occurrences
"""

def find_majority_element(target_list):
    data = {}

    for i in target_list:
        data[i] = 0

    for i in target_list:
        data[i] += 1

    solution = max(data, key=lambda x:data[x])


    print(f"The integer with the highest number of occurrences is {solution}")




if __name__ == "__main__":
    target_list = [3, 2, 3]
    find_majority_element(target_list)