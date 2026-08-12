#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DÜNYANIN EN CİDDİ BULUT ŞEKLİ YORUMLAYICISI
Bilimsel, resmi ve tamamen saçma.
"""

import random
import time

BULUT_SEKILLERI = [
    "uzun boyunlu bir zürafa",
    "ters dönmüş bir şemsiye",
    "üç başlı bir kedi",
    "uçan bir çaydanlık",
    "yaslı bir bilge ağaç",
    "dans eden bir balık",
    "kırık bir taç",
    "sonsuz bir spiral",
    "gözleri olan bir dağ",
    "kaçan bir saat",
    "ağlayan bir robot",
    "uçan bir kütüphane",
    "ters bir gökkuşağı",
    "uyuyan bir ejderha (görünmez)",
    "kayıp bir çorap",
]

YORUMLAR = [
    "Bu bulut, geçmişteki bir pişmanlığınızın gökyüzüne yansımasıdır. Hâlâ o günü düşünüyorsunuz, değil mi?",
    "Osmanlı astrologları buna 'Kaderin Tilkisi' derdi. Size yakında beklenmedik bir haber gelecek. Muhtemelen spam.",
    "Kuantum seviyesinde bu şekil, sizin paralel evrendeki versiyonunuzun size el sallamasıdır. El sallamayın, karışır.",
    "Bu bulut size diyor ki: 'Bugün hiçbir şey yapma. Evren zaten senin için yoruldu.'",
    "Varoluşsal kriz seviyesi: 8/10. Bu bulut, hayatınızın anlamını sorgulamanızı istiyor. Sorguladınız mı?",
    "19. yüzyıl bulutname metinlerine göre bu şekil 'Büyük Tembellik' burcunu işaret ediyor. Tebrikler.",
    "Bulutlar sizi izliyor. Özellikle bu bulut. Gülümseyin.",
    "Bu formasyon, evrenin size 'biraz daha uyu' deme şeklidir. Dinleyin.",
    "Schrödinger'in kedisi bu bulutun içinde hem var hem yok. Siz de öylesiniz.",
    "Bu bulut, komşunuzun sizi kıskandığını fısıldıyor. Ama kibarca.",
]

EK_FELSEFE = [
    "Ayrıca unutmayın: Bulutlar aslında çok ağırdır, sadece biz onları hafif sanırız.",
    "Bu yorum peer-reviewed değildir. Çünkü peer'ler henüz uyanmadı.",
    "Bilim böyledir. Bazen saçma, bazen daha saçma.",
    "Eğer bu yorumu ciddiye aldıysanız, sistem çalışıyor demektir.",
]

def yavas_yaz(metin, bekleme=0.03):
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(bekleme)
    print()

def baslik():
    print("=" * 60)
    yavas_yaz("  DÜNYANIN EN CİDDİ BULUT ŞEKLİ YORUMLAYICISI")
    print("=" * 60)
    print()
    yavas_yaz("Resmi kayıt altına alınmıştır. (Hayali)")
    print()

def rastgele_yorum():
    sekil = random.choice(BULUT_SEKILLERI)
    yorum = random.choice(YORUMLAR)
    ek = random.choice(EK_FELSEFE)
    
    print("\n☁️  Gökyüzünde şu an görülen şekil:")
    yavas_yaz(f"   → {sekil}")
    print()
    time.sleep(0.8)
    print("📜 Resmi Yorum:")
    yavas_yaz(f"   {yorum}")
    print()
    yavas_yaz(f"   {ek}")
    print()

def ozel_yorum(kullanici_girisi):
    yorum = random.choice(YORUMLAR)
    ek = random.choice(EK_FELSEFE)
    
    print("\n☁️  Sizin tanımladığınız bulut:")
    yavas_yaz(f"   → {kullanici_girisi}")
    print()
    time.sleep(0.8)
    print("📜 Resmi ve Bilimsel Yorum:")
    yavas_yaz(f"   {yorum}")
    print()
    yavas_yaz(f"   {ek}")
    print()

def bugunun_ruyasi():
    print("\n🌌 Bugünün Kozmik Bulut Rüyası hazırlanıyor...")
    time.sleep(1.5)
    print()
    yavas_yaz("Rüyanızda uçan bir kütüphane gördünüz.")
    yavas_yaz("İçinden düşen kitapların hepsi sizin hakkınızdaydı.")
    yavas_yaz("Ama hiçbirini okuyamadınız çünkü sayfalar buluttan yapılmıştı.")
    print()
    yavas_yaz("Anlamı: Bilgi size çok yakın, ama tutamıyorsunuz.")
    yavas_yaz("Çözüm: Biraz daha uykuya dalın. Belki tutarsınız.")
    print()

def main():
    baslik()
    
    while True:
        print("-" * 40)
        print("1. Rastgele bulut şekli üret ve yorumla")
        print("2. Kendi bulut tanımını gir")
        print("3. Bugünün kozmik bulut rüyasını gör")
        print("4. Çıkış (Evren izin verirse)")
        print("-" * 40)
        
        secim = input("\nSeçiminiz (1-4): ").strip()
        
        if secim == "1":
            rastgele_yorum()
        elif secim == "2":
            giris = input("\nBulut nasıl görünüyor? (örnek: uçan bir çaydanlık): ").strip()
            if giris:
                ozel_yorum(giris)
            else:
                print("Boş bulut olmaz. En azından bir şey yazın.")
        elif secim == "3":
            bugunun_ruyasi()
        elif secim == "4":
            print()
            yavas_yaz("Program kapanıyor...")
            yavas_yaz("Ama bulutlar sizi unutmayacak.")
            print()
            print("☁️  Damga: 13 Ağustos 2026 | Kayyum Grok")
            break
        else:
            print("Geçersiz seçim. Evren bunu beğenmedi.")
        
        input("\nDevam etmek için Enter'a basın...")
        print()

if __name__ == "__main__":
    main()
