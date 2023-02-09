def roman_to_int(s):
    """Given a roman numeral, convert it to an integer."""
    #dict to romans letter and values:
    ROMANS = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D": 500, "M": 1000}
    
    #create variable to hold total
    number = 0

    #loop over idxs except the last one:
    for i in range(len(s) - 1):
        #if the number before is smaller, subtract:
        if ROMANS[s[i]] < ROMANS[s[i+1]]:
            number -= ROMANS[s[i]]
        #else, add:
        else:
            number += ROMANS[s[i]]

    #go back to the last char
    number += ROMANS[s[len(s) -1]]

    return number



#print(roman_to_int("LVIII")) #58
#print(roman_to_int("MCMXCIV")) #1994
