def Hashtag(x): # fungsi def ini untuk membuat fungsi dengan nama Hashtag()
    if x == '' or len(x) > 140: # fungsi ini untuk memberi batasan pada x; Dalam hal ini, jika x diisi dengan string kosong atau panjang x adalah lebih dari 140 karakter, maka fungsi ini akan bernilai True
        return False # jika function if di atas terpenuhi atau bernilai True, maka akan me-return False
    else: # fungsi ini adalah fungsi yang akan dijalankan ketika fungsi if di atas bernilai False
        y = x.title() # fungsi x.title() berfungsi untuk membuat string pertama di awal kata menjadi huruf besar
        z = y.replace(' ','') # fungsi y.replace() berfungsi untuk mengubah string spasi (' ') menjadi string kosong ('')
        return f'#{z}' # ketika fungsi else ini jalan, maka akan return f string ini

print(Hashtag("Hello there how are you doing"))
print(Hashtag("     Hello     World   "))
print(Hashtag(""))