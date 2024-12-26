print('ini progam pilihan suara hati')
print('='*50)
print('apakah kamu suka aku? jawab dari hati ya')
print('='*50)

nama = input('!!!sebelum menjawab pertanyaan diatas, siapa nama mu:')
print(f'hello {nama}, namamu cukup indah seperti parasmu!!!')
print('sekarang jawab pertanyaan diatas')
 
user = input('yes?no :')

if user == 'yes':
    print('makasih ya, tapi apa kamu bener2 suka aku?')
    bener2 = input('ya/tidak :')
    if bener2== 'ya':
        print('kamu gak boong kan!!')
        option = input('lantas suka dari mana nya? :')
        print('aaahhh jadi hapy akuuu <3')
    elif bener2== 'tidak':
        print('"jadi selama ini kamu pura2 suka aku?')
        print('sejujurnya kamu gak papa lukain raga ku asal jangan hati ku, karna disitu ada kamu!!"')
        print('terimaksih telah menjawab,semoga harimu menyenang kan')
    else:
        print('jangan nyari yang gak ada ya, cukup perasaan mu ke aku aja yang gak ada')
elif user== 'no':
    for user in range(1,30,+1):
        print('TAI LU!!!!!')
        print('_'*5)
        print('BANGSATT')
        print('_'*5)
        print('ANJINGG ')
        print('_'*5)
    print(user)
    print('besok gw bunuh lu !!')

else:
    print('jangan nyari yang gak ada ya, cukup perasaan mu ke aku aja yang gak ada')

