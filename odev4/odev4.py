import sqlite3

# SQLite veritabanı bağlantısını oluştur
conn = sqlite3.connect('metinler.db')
c = conn.cursor()

# Metinleri SQLite'a ekleme
def metin_ekle(metin1, metin2):
    c.execute("CREATE TABLE IF NOT EXISTS metinler (id INTEGER PRIMARY KEY, metin TEXT)")
    c.execute("INSERT INTO metinler (metin) VALUES (?)", (metin1,))
    c.execute("INSERT INTO metinler (metin) VALUES (?)", (metin2,))
    conn.commit()

# Benzerlik algoritması
def benzerlik_hesapla(metin1, metin2):
    # Metinleri kelimelere ayırın
    kelimeler_metin1 = set(metin1.split())
    kelimeler_metin2 = set(metin2.split())
    
    # İki metin arasındaki ortak kelimelerin sayısını bulun
    ortak_kelimeler = len(kelimeler_metin1.intersection(kelimeler_metin2))
    
    # Jaccard benzerlik katsayısını hesaplayın
    jaccard_benzerlik = ortak_kelimeler / len(kelimeler_metin1.union(kelimeler_metin2))
    
    return jaccard_benzerlik

# Benzerlik durumu dosyasına yazma
def benzerlik_durumu_yaz(benzerlik_orani):
    with open('benzerlik_durumu.txt', 'w', encoding='utf-8') as file:
        file.write(f"Benzerlik Oranı: {benzerlik_orani}")
        file.write("\n")
        if benzerlik_orani == 1.0:
            file.write("Metinler tamamen aynıdır.")
        elif benzerlik_orani > 0.5:
            file.write("Metinler benzerdir.")
        else:
            file.write("Metinler benzer değildir.")
        file.write("\n")

# Ana işlem
def main():
    metin1 = input("İlk metni girin: ")
    metin2 = input("İkinci metni girin: ")
    
    metin_ekle(metin1, metin2)
    
    benzerlik_orani = benzerlik_hesapla(metin1, metin2)
    
    print("Benzerlik Oranı:", benzerlik_orani)
    
    benzerlik_durumu_yaz(benzerlik_orani)
    
    conn.close()

if __name__ == "__main__":
   main()