vstup = str('OOOXOXOOOOOO');
vstup =  [vstup[i:i+3] for i in range(0, len(vstup), 3)]

# Základní hodnota pro vstup 
print('START: ' , vstup)

finish = []

for lamp_t in vstup:
    vastup_3 = list(lamp_t)
    if 'X' in vastup_3:
        print('X > ', vastup_3)
        finish.append(vastup_3) 
    else:
            print(vastup_3)
            vastup_3[1] = '-'
            print('Y > ', vastup_3)
            finish.append(vastup_3)

print("FINISH")
finish = str(finish).replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace(' ', '')
finish =  [finish[i:i+2] for i in range(0, len(finish), 2)]
string = ''.join(finish)
print(string)
print(finish)
for lamp_t in finish:

    print(vastup_3)
    if '[O, O]' in vastup_3:
        vastup_3[1] = ''
        print('X > ', vastup_3)
        finish.append('O')

finish = str(finish).replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace(' ', '')


print(finish)

    
            

