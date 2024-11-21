import statistics

with open('example.txt', 'r') as f:

    FID = []
    mem_strength = []

    for line in f:
        if 'FID' in line:
            number = ''
            for char in line:
                if char.isdigit() or char == '.':
                    number += char
                else:
                    if number:
                        FID.append(float(number))
                        break

        if 'memorization_strength' in line:
            number1 = ""
            for char in line:
                for char in line:
                if char.isdigit() or char == '.':
                    number += char
                else:
                    if number:
                        mem_strength.append(float(number))
                        break
                