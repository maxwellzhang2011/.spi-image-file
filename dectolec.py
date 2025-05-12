numbers = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*-+="

def detolecnovo(number):
    num1r = number % 47
    num1 = number / 47
    num2r = num1 % 47
    d1 = numbers[int(num1r)]
    d2 = numbers[int(num2r)]
    return d2 + d1