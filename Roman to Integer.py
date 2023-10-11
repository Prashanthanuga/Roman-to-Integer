def roman_to_integer(s):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    prev_value = 0

    for numeral in s[::-1]:
        if roman_numerals[numeral] < prev_value:
            integer_value -= roman_numerals[numeral]
        else:
            integer_value += roman_numerals[numeral]
        prev_value = roman_numerals[numeral]

    return integer_value

# Example usage:
roman_numeral = input("Enter a Roman numeral: ")
integer_value = roman_to_integer(roman_numeral)
print("Integer value:", integer_value)