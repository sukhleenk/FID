import statistics

with open('example.txt', 'r') as f:

    FID = []

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