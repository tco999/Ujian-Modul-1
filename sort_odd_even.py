def sort_odd_even(x): # fungsi def ini untuk membuat fungsi dengan nama sort_odd_even()
    ganjil = [] # membuat list kosong dengan nama ganjil yang digunakan untuk menampung angka ganjil
    indexganjil = [] # membuat list kosong dengan nama indexganjil yang digunakan untuk menampung index dari angka ganjil
    genap = [] # membuat list kosong dengan nama genap yang digunakan untuk menampung angka genap
    indexgenap = [] # membuat list kosong dengan nama indexgenap yang digunakan untuk menampung index dari angka genap
    for i in range(len(x)): # looping for loop dengan range berdasarkan panjang dari list x atau input
        if x[i] % 2 == 1: # fungsi conditional untuk mengecek apakah elemen x[i] merupakan bilangan ganjil
            ganjil.append(x[i]) # ketika elemen x[i] merupakan bilangan ganjil, maka elemen tersebut akan masuk ke list ganjil
            indexganjil.append(i) # dan index dari elemen tersebut akan masuk ke list indexganjil
    ganjil.sort() # fungsi ganjil.sort() digunakan untuk mengurutkan angka di list ganjil dari angka terkecil ke terbesar
    for i in range(len(x)): # looping for loop dengan range berdasarkan panjang dari list x atau input
        if x[i] % 2 == 0: # fungsi conditional untuk mengecek apakah elemen x[i] merupakan bilangan genap
            genap.append(x[i]) # ketika elemen x[i] merupakan bilangan genap, maka elemen tersebut akan masuk ke list genap
            indexgenap.append(i) # dan index dari elemen tersebut akan masuk ke list indexgenap
    genap.sort(reverse=True) # fungsi genap.sort(reverse=True) digunakan untuk mengurutkan angka di list genap dari angka terbesar ke terkecil
    for i in range(len(indexganjil)): # looping for loop dengan range berdasarkan panjang dari list indexganjil
        x[indexganjil[i]] = ganjil[i] # fungsi ini digunakan untuk mengubah nilai angka pada list indexganjil sesuai dengan urutan yang diinginkan; x[0]=1, x[1]=3, x[4]=5
    for i in range(len(indexgenap)): # looping for loop dengan range berdasarkan panjang dari list indexgenap
        x[indexgenap[i]] = genap[i] # fungsi ini digunakan untuk mengubah nilai angka pada list indexgenap sesuai dengan urutan yang diinginkan; x[2]=8, x[3]=4, x[5]=2
    return x # ketika semua rangkaian for loop di atas selesai, maka akan me-return x

print(sort_odd_even([5, 3, 2, 8, 1, 4]))
