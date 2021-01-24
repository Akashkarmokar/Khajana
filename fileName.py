

# This function check problem name. sometimes problem name is not supported in operating system.
def check_filename(filename):
    name_list = list(filename)
    for i in range(0, len(name_list)):
        if (ord(name_list[i]) > 31 and ord(name_list[i]) < 48) or (
                ord(name_list[i]) > 57 and ord(name_list[i]) < 65) or (
                ord(name_list[i]) > 90 and ord(name_list[i]) < 97) or (
                ord(name_list[i]) > 122 and ord(name_list[i]) < 127):
            name_list[i] = '_'
    final_name = "".join(name_list)
    return final_name


