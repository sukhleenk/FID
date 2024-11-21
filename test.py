import statistics

with open('example.txt', 'r') as f:

    FID = []
    mem_strength = []
    benign_count = 0
    malicious_count = 0

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
                
        if 'benign model' in line:
            benign_count += 1

        if 'malicious model' in line:
            malicious_count += 1

    print('Number of benign models: ', benign_count)
    print('Number of malicious models: ',malicious_count)

    

