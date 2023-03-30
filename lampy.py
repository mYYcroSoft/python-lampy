vstup = str('OOOxOxOOOOOO');
vstup =  [vstup[i:i+3] for i in range(0, len(vstup), 3)]

# Základní hodnota pro vstup 
print('START: ' , vstup)

finish = []

for lamp_t in vstup:
    vastup_3 = list(lamp_t)
    if 'x' in vastup_3:
        print(vastup_3)
        finish.append(vastup_3)
    else:
            vastup_3[1] = '-'
            print(vastup_3)
            finish.append(vastup_3)

print("FINISH")
finish = str(finish).replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace(' ', '')
print(finish)

    
            

