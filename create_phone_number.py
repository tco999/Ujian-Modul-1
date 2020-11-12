def create_phone_number(x): # fungsi def ini untuk membuat fungsi dengan nama create_phone_number()
    return (f'({x[0]}{x[1]}{x[2]}) {x[3]}{x[4]}{x[5]}-{x[6]}{x[7]}{x[8]}{x[9]}') # menggunakan return f string. Memanggil masing-masing index satu per satu. Ketika fungsi ini di print, maka akan keluar output seperti yang diharapkan pada soal.

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))