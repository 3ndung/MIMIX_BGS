# this is sample you can add your owd dictionary

my_dict = {
    "AB": ["A", "B", "C"],
    "BE": ["E", "F", "Z"],
    "CD": ["X", "Y"]
}

def transform_list(check_list, key, my_dict):
    if key in my_dict:
        elements = my_dict[key]
        replacement = key
        if all(element in check_list for element in elements):
            for element in elements:
                check_list.remove(element)
            check_list.append(replacement)
            return True
    return False

# Example usage
check_list = ["A", "C", "E", "F", "Z", "X", "Y","TT"]


for ZZ in my_dict.keys():
    transform_list(check_list,ZZ, my_dict)


print(check_list)
