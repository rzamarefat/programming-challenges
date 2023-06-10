"""
Given an array find the number of distinct values

input = [1, 5, -3, 1, -4, 2, -4, 7, 7]
solution: 6
"""

def find_num_distinct_values(input_array):
    unique_values = []

    for i in input_array:
        if not(i in unique_values):
            unique_values.append(i)


    print(f"The number of distinct values in the given array is {len(unique_values)}")        

if __name__ == "__main__":
    input_array = [1, 5, -3, 1, -4, 2, -4, 7, 7]

    find_num_distinct_values(input_array)