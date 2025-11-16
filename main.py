import math


# print(round(pi)) #pembulatan
# print(math.ceil(pi)) #pembulatan ke atas
# print(math.floor(pi)) #pembulatan ke bawah
# print(abs(pi)) #angka positif / absolut
# print(pow(x , 2)) #pangkat pow (variabel, pangkat)
# print(math.sqrt(10)) #akar kuadrat
# print(max(x,y,z)) #mencari nilai terbesar
# print(min(x,y,z)) #mencari data terkecil
# print(round(math.pi , 2)) #nilai pi
# print(round(math.e, 2)) #nilai eulier

# keliling dan luas lingkaran
# r = float(input("masukkan nilai jari jari lingkaran:"))
# kel = 2 * math.pi * r
# luas = math.pi * pow(r, 2)
# print("keliiling lingkaran adalah:" , round(kel,2))
# print ("luas lingkaran adalah:", round(luas,2))

# menghitung derajat sudut dalam lingkaran
# r = float(input("masukan nila jari jari lingkaran:"))
# s = float(input("masukan nilai panjang busur lingkaran:"))
# d = (s / (2 * math.pi * r)) * 360
# print("nilai derajat sudut dalam lingkaran adalah:" , round(d,2))

# menghitung keliling dan luas lingkaran, menghitung derajat sudut, juring , luas segitiga lingkaran dan luas dan keliling tembereng lingkaran 
r = float(input("masukan nilai jari jari lingkaran:"))#inputan jari jari
s = float(input("masukan nilai sudut pusat lingkaran:")) #inputan sudut pusat
j = ( s / 360 * math.pi * pow(r ,2)) #juring ligkaran
ls = (0.5 * pow(r,2) * math.sin(math.radians(s))) #luas segitiga lingkaran
t = j - ls #luas temberereng lingkaran
pb = (s / 360) *2 * math.pi * r #panjang busur
tb = 2 * r * math.sin(math.radians(s/2)) #tali busur
kt = pb + tb #keliiling tembereng lingkaran
kel = 2 * math.pi * r #keliling lingkaran
luas = math.pi * pow(r, 2) #luas lingkaran
d = (pb / (2 * math.pi * r)) * 360 #derajat sudut dalam lingkaran
dm = 2 * r #diameter lingkaran
print("nilai diameter lingkaran adalah:" , round(dm,2) , "cm")
print("keliiling lingkaran adalah:" , round(kel,2) , "cm")
print ("luas lingkaran adalah:", round(luas,2) , "cm\u00B2")
print("nilai derajat sudut dalam lingkaran adalah:" , round(d,2), "derajat")
print("nilai luas juring lingkaran adalah:" , round(j,2) , "cm\u00B2")
print("nilai luas segitiga adalah:" , round(ls,2) , "cm\u00B2")
print("niai luas tmbereng adalah:" , round(t,2) , "cm\u00B2")
print("niai panjang busur adalah:" , round(pb,2) , "cm")
print("niai tali busur adalah:" , round(tb,2), "cm")
print("niai keliling tembereng adalah:" , round(kt,2) , "cm")




# menghitung segitiga pitagoras sisi miring / (c)
# a = float(input("masukan nilai sisi a:"))
# b = float(input("masukan nilai sisi b:"))
# c = math.sqrt(pow(a,2) + pow(b,2))
# print("nilai sisi miring segitiga pitagoras sisi c adalah:" , round(c,2))



