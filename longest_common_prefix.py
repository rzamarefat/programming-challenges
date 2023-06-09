def longest_common_prefix(string_one, string_two):
    common_prefix = ""

    for index, char in enumerate(string_one):
        try:
            if char == string_two[index]:
                common_prefix += string_two[index]
            else:
                break
        except:
            continue

    if common_prefix == "":
        common_prefix = "None"
        
    print(f"The common prefix in {string_one} and {string_two} is {common_prefix}")


if __name__ == "__main__":
    string_one = "lgo"
    string_two = "Algorithm"
    longest_common_prefix(string_one, string_two)
