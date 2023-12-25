x = int(input("Masukan angka : "))
if x == 1:
    print("adalah benar") # di python menggunakan indentation tidak menggunakan bracket {} seperti js, c++, dll
elif x == 2:
    print("yes bener")
else:
    print("gatau.")
    
match x:
    case 1:
        print("adalah benar coy")
    case 2: 
        print("yes bener coy")
    case _:
        print("gatau jir.")

while x<=2:
    x += 1

a = 0
while True:
    if(a == 10):
        break
    a += 1
print("->", x)

orang = ("udin","samsul")
print("List nama orang")

for indexNama in range(len(orang)):
    print(indexNama,orang[indexNama])

print("==============")

players_status = {
    'udin': 'online',
    'samsul': 'offline',
    'samsudin': 'online'
}

for nama, status in players_status.copy().items():
    if status == "offline":
        del players_status[nama]

print(players_status)

print("===============")


for i in range (5):
    print(i)

def fungsiIniGakNgapainNgapain():
    pass # ini kode gak ngapa ngapain

fungsiIniGakNgapainNgapain()

def fungsiTambah(argumen1, argumen2):
    return argumen1 + argumen2

print(fungsiTambah(1,2))

def makanan(arg="ayam"):
    match arg:
        case "ayam": print("UMMM, ENAK!")
        case "bubur": print("ENAK JIR")
        case "mie": print("MANTAP!")
        case _: print("apaan tuh!")

makanan()
makanan("bubur")

# PERINGATAN: Nilai default yang dapat diubah (misalnya, daftar) dievaluasi hanya sekali.
# Ini mempengaruhi fungsi yang mengakumulasi argumen, seperti contoh di bawah ini.

def accumulate_args(arg, acc=[]):
    acc.append(arg)
    return acc

# Example usage:
# Penggunaan contoh:
print(accumulate_args(1))  # Output: [1]
print(accumulate_args(2))  # Output: [1, 2]
print(accumulate_args(3))  # Output: [1, 2, 3]

# solusi

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))

# argument

def test(a, *b, **c): 
    print(a) # mengambil argumen pada posisi pertama
    print(b) # mengambil argumen positional (selain argumen yang pertama)
    print(c) # mengambil argumen keyword

test("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# positional-only & keyword-only args

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
    
standard_arg(1)
standard_arg(arg=1)
pos_only_arg(2)
# pos_only_arg(arg=2) -> ERROR!
kwd_only_arg(arg=3)
# kwd_only_arg(3) -> ERROR!

# combined_example(1, 2, 3) -> ERROR!
# combined_example(pos_only=1, standard=2, kwd_only=3) -> ERROR!

combined_example(1,2,kwd_only=3)
combined_example(1,standard=2,kwd_only=3)

# cara lain menulis keyword
combined_example(1,**{'standard': 2, 'kwd_only': 3})

# lambda function

lf = lambda x: x+1
def makeLambdaFunction():
    return lambda x: x+1
lff = makeLambdaFunction()
print(lf(1))
print(lff(2))

# Documentation Strings

def fungsiku():
    """
    fungsi ini gak ngapa ngapain :D
    """
    pass
fungsiku()


# anotasi fungsi

# fungsi(argument: tipe-data) -> tipe-data
# tipe data: 
# str,float,int,str,dict,tuple,list,set,frozenset, dan lain lain

def fungsiKurang(nilai1: int, nilai2: int) -> int:
    """
    fungsi ini melakukan operasi kurang. (nilai1-nilai2)
    """
    return nilai1 - nilai2

print(fungsiKurang(12,3))