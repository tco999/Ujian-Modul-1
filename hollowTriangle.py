def hollowTriangle(x): # fungsi def ini untuk membuat fungsi dengan nama hollowTriangle()
    for row in range(x): # menggunakan variable row untuk menentukan jumlah row nya (di simpan sebagai variable x)
        for col in range(2*x-1): # menggunakan variable col untuk menentukan jumlah column nya; Pada soal, ketika row nya 5, maka column nya adalah 9. Ketika row nya 6, maka column nya adalah 11; Maka dari itu tercipta formula 2*x-1
            if row == x-1 or row+col == x-1 or col-row == x-1: # fungsi ini adalah fungsi conditional yang digunakan untuk menentukan letak '#' pada posisi yang diinginkan; yaitu adalah ketika row == x-1, serta row+col == x-1, dan juga col-row == x-1, saya ingin ada '#' pada setiap posisi tersebut.
                print('#', end = '') # ketika fungsi if di atas bernilai true, maka fungsi ini akan memasukkan string '#' dan di akhiri dengan string kosong ('')
            else: # jika fungsi if di atas bernilai false, maka fungsi else ini akan jalan
                print(end='_') # jika fungsi else ini jalan, maka akan terprint underscore ('_')
        print() # setiap for loop col ini selesai, maka fungsi ini akan meminta untuk pindah baris

hollowTriangle(5)

