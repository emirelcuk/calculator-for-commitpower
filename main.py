def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Hata: Sıfıra bölme hatası!"
    return a / b

print("Yapılacak işlemi seçin:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminizi yapın (1, 2, 3 veya 4): ")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))


else:
    print("Geçersiz seçim. Lütfen 1, 2, 3 veya 4 girin.")



