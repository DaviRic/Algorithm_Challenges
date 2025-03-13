# Algoritmo que faz a conversão de número em algarismo romano para inteiro
def romanToInteger(s):
    values_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D':500, 'M': 1000
    }
    values_vector = []
    i = 0
    while i < len(s):
        if i < len(s) - 1 and values_dict[s[i]] < values_dict[s[i+1]]:
            values_vector.append(values_dict[s[i+1]] - values_dict[s[i]])
            i += 2
        else:
            values_vector.append(values_dict[s[i]])
            i+=1
    result = sum(values_vector)
    return result
    
romanToInteger("MCMXCIV")