rom = input("Enter a roman numeral:")
rom = str(rom)
rom = rom.lower()
i = 1
v = 5
x = 10
l = 50
c = 100
d = 500
m = 1000
total = 0
for n in range (len(rom)):
    if rom[n] == 'i' and not(rom[len(rom)-1] == rom[n]):
        if rom[n+1] == 'v' or 'x' or 'l' or 'c' or 'd' or 'm':
            total -= 1
        else:
            total += 1
    elif rom[n] == 'i' and (rom[len(rom)-1] == rom[n]):
        total += 1
        
    elif rom[n] == 'v' and not(rom[len(rom)-1] == rom[n]):
        if rom[n+1] == ('x' or 'l' or 'c' or 'd' or 'm'):
            total -= 5
        else:
            total += 5
    elif rom[n] == 'v' and (rom[len(rom)-1] == rom[n]):
        total += 5

    elif rom[n] == 'x' and not(rom[len(rom)-1] == rom[n]):
        if rom[n+1] == ('l' or 'c' or 'd' or 'm'):
            total -= 10
        else:
            total += 10
    elif rom[n] == 'x' and (rom[len(rom)-1] == 'x'):
        total += 10

    elif rom[n] == 'l' and not(rom[len(rom)-1] == rom[n]):
        if rom[n+1] == ('c' or 'd' or 'm'):
            total -= 50
        else:
            total += 50
    elif rom[n] == 'l' and (rom[len(rom)-1] == rom[n]):
        total += 50

    elif rom[n] == 'c' and not(rom[len(rom)-1] == rom[n]):
        if rom[n+1] == ('d' or 'm'):
            total -= 100
        else:
            total += 100
    elif rom[n] == 'c' and (rom[len(rom)-1] == rom[n]):
        total += 100

    elif rom[n] == 'd' and not(rom[len(rom)-1] == rom[n]):
        if rom[n+1] == ('m'):
            total -= 500
        else:
            total += 500
    elif rom[n] == 'd' and (rom[len(rom)-1] == rom[n]):
        total += 500

    elif rom[n] == 'm':
        total += 1000
print(rom.upper() + " = " + str(total))
