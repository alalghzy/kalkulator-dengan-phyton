#membuat class untuk kalkulator agar lebih mudah untuk dikembangkan dan diedit
class kalkulator():
      def __init__(self,x,y):
        self.x = x
        self.y = y
      def tambah(x,y):
        hasilT = x + y
        print('Hasil penjumlahan         =', hasilT)
        return hasilT
      def kurang(x,y):
        hasilM = x - y
        print('Hasil pengurangan         =', hasilM)
        return hasilM
      def kali(x,y):
        hasilK = x * y
        print('Hasil perkalian           =', hasilK)
        return hasilK
      def bagi(x,y):
        hasilB = x / y
        print('Hasil penjumlahan         =', hasilB)
        return hasilB
#menginput 2 bilangan, yang nantinya akan dijumlahkan
def mTambah():
    print('''
=================================
Kalkulator Penjumlahan 2 Bilangan
=================================
  ''')
    x = int(input('Masukkan bilangan pertama = '))
    y = int(input('Masukkan bilangan kedua   = '))
    tHasil = kalkulator.tambah(x,y)    
#menginput 2 bilangan, yang nantinya akan dikurang
def mKurang():
    print('''
=================================
Kalkulator Pengurangan 2 Bilangan
=================================
  ''')
    x = int(input('Masukkan bilangan pertama = '))
    y = int(input('Masukkan bilangan kedua   = '))
    mHasil = kalkulator.kurang(x,y)     
#menginput 2 bilangan, yang nantinya akan dikalikan
def mKali():
    print('''
===============================
Kalkulator Perkalian 2 Bilangan
===============================
  ''')
    x = int(input('Masukkan bilangan pertama = '))
    y = int(input('Masukkan bilangan kedua   = '))
    kHasil = kalkulator.kali(x,y)
#menginput 2 bilangan, yang nantinya akan dibagi 
def mBagi():
    print('''
===============================
Kalkulator Pembagian 2 Bilangan
===============================
  ''')
    x = int(input('Masukkan bilangan pertama = '))
    y = int(input('Masukkan bilangan kedua   = '))
    bHasil = kalkulator.bagi(x,y) 
#menu pilihan yang bisa dipilih/diinput oleh user
def menu():
  print('''
Pilih Menu
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
''')
  pilih = int(input('Masukkan pilihan = '))
  if pilih == 1:
    mTambah()
  elif pilih == 2:
    mKurang()
  elif pilih == 3:
    mKali()
  elif pilih == 4:
    mBagi()
#main code
def main():
  print('''
====================
Kalkulator Sederhana
====================
Nama : Rafif Alghazy
NPM  : G1A021097
====================  
  ''')
  menu()
if __name__ == '__main__':
  main()
