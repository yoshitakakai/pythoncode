text = list('PYTHON PROGRAMMING')
pattern = list('PRO')

for i in range(len(text)):
    match = True
    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
            break
    if match:
        print(i)
        break