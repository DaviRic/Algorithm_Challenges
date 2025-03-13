def longestCommonPrefix(str_list):
    prefix = ''
    for string in str_list:
        for index in range(str_list):
            if string[index] == str_list[index+1][index]:
                prefix = string[index]
    return prefix