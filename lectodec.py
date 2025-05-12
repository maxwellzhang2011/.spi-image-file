digit_set = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*-+="

def lectodec(input_str):
    decimal_value = 0
    length = len(input_str)

    for i, char in enumerate(input_str):
        value = digit_set.index(char)
        decimal_value += value * (47 ** (length - i - 1))

    return decimal_value