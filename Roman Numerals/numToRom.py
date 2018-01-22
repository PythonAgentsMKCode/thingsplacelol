#numToRoman.py

def main():
    roman = ""
    num = eval(input("Enter a number to convert to Roman Numerals: "))
    while num >= 1000:
        roman += "M"
        num -= 1000
    while num >= 500:
        roman += "D"
        num -= 500
    while num >= 100:
        roman += "C"
        num -= 100
    while num >= 50:
        roman += "L"
        num -= 50
    while num >= 10:
        roman += "X"
        num -= 10
    while num >= 5:
        roman += "V"
        num -= 5
    while num >= 1:
        roman += "I"
        num -= 1

    roman2 = ""
    for i in range(len(roman)-3):
        if roman[i] == roman[i+1] == roman[i+2] == roman[i+3] == "M":
            roman2 += "MMMM"
        if roman[i] == roman[i+1] == roman[i+2] == roman[i+3] == "D":
            roman2 += "DM"
        if roman[i] == roman[i+1] == roman[i+2] == roman[i+3] == "C":
            roman2 += "CD"
        if roman[i] == roman[i+1] == roman[i+2] == roman[i+3] == "L":
            roman2 += "LC"
        if roman[i] == roman[i+1] == roman[i+2] == roman[i+3] == "X":
            roman2 += "XL"
        if roman[i] == roman[i+1] == roman[i+2] == roman[i+3] == "V":
            roman2 += "VX"
        if roman[i] == roman[i+1] == roman[i+2] == roman[i+3] == "I":
            roman2 += "IV"

        
    print()
    print()
    print(roman2)

main()
