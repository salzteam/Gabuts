def isi():
    print(' halo selamat datang! ini siapa ya?')
    nama=input('coba masukin nama kamu disini : ')
    print('')

    print('haii', nama, '!')
    print('')
    jawab=input('apa kabar?')
    print('')
    jawaban='baik'

    if jawab==jawaban:
        print('alhamdulilah deh kalo baik')
        print(' ')
    else:
        hmm=input('kenapa?sini ceritaa: ')
        print('')
        op='gak ah','gak','dak'
        if hmm==op:
            hh=input('beneran nih ga mau?:')
            print('')
        else:
            aa=input('sini sini wa aja 082279014545 hehe : ')
            print('')
                        
    jumlah=int(input('btw kamu mau diucuapin brp kali?'))
    print('')
    text=input('mau di ucapin apa coba?')
    print('')

    while jumlah<=0:
        print('')

    for i in range (jumlah):
        print(text)

    print('')
    print('')
    print('udahhh yaaa babayyy')

isi()

want = input("Lanjutt? Y/N\n")
if want=="Y":
    isi()
if want=="N":
    sys.exit("OKAY THANKYOU")