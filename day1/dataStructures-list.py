# list

buah = ['apel','mangga','melon'] 
# menambah 1 element baru 
buah.append('jeruk')
# menambah banyak element
buah.extend(['semangka','pisang'])
# menambah element pada index tertentu
buah.insert(0,'nangka')
# menghapus element
buah.remove('apel')
# menghapus element di posisi yang diberikan
buah.pop(1) # mangga dihapus

buahcopy = buah.copy()
# menghapus semua element
buahcopy.clear()
# mengembalikan nilai index pada element yang sama dengan argumen yang dimasukan. 
# (akan mengembalikan error jika element tidak ada)
print(buah.index('jeruk'))
# mereverse element
buah_r = buah.copy()
buah_r.reverse()
print(buah_r)
# menghitung ada berapa element yang sama dengan argument
print(buah.count('melon'))
# mengsortir list (terkecil -> terbesar)
s = [5,2,1,3,4]
s_r = s.copy()
s.sort()
print(s)
# mengsortir list (terbesar -> terkecil)
s_r.sort(reverse=True)
print(s_r)
print(buah)
# del statement

del buah[0] # menghapus element dengan index ke 0 (nangka)

# slicing

new_buah = buah.copy()
print(new_buah[2:4])
del new_buah[2:4]
print(new_buah)
del new_buah
# print(new_buah) -> ERROR
print(buah)
print(buahcopy)