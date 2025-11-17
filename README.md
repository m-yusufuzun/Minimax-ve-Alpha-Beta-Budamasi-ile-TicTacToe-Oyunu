# X-O (Tic-Tac-Toe) için Minimax ve Alfa-Beta Budaması Karşılaştırması

Bu proje, klasik X-O (Tic-Tac-Toe) oyunu üzerinde iki farklı yapay zeka karar verme algoritmasını uygular ve karşılaştırır: **Minimax** ve **Alfa-Beta Budaması (Alpha-Beta Pruning)**.

Projenin temel amacı, Alfa-Beta Budaması optimizasyonunun, standart Minimax algoritmasına kıyasla arama ağacındaki düğüm sayısını ve hesaplama süresini nasıl önemli ölçüde azalttığını göstermektir.

![GitHub lisanı](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Sürümü](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![Kullanılan Algoritmalar](https://img.shields.io/badge/AI-Minimax%20%26%20Alpha--Beta-orange.svg)

---

## 🧠 Uygulanan Algoritmalar

### 1. Minimax Algoritması
Minimax, X-O gibi iki oyunculu, sıfır toplamlı ve tam bilgili oyunlar için kullanılan bir karar verme algoritmasıdır. Temel amacı, bir sonraki hamlenin en optimal (en iyi) hamle olmasını sağlamaktır.

### 2. Alfa-Beta Budaması (Alpha-Beta Pruning)
Alfa-Beta Budaması, Minimax algoritmasının bir optimizasyonudur. Minimax'ın tüm oyun ağacını keşfetmesi yerine, "gereksiz" veya "sonucu değiştirmeyecek" dalları budayarak arama işlemini hızlandırır.

Bunu yaparken iki değer tutar:
* **Alfa ($\alpha$):** `MAX` oyuncusunun (bizim) şu ana kadar garantilediği **en yüksek** skordur. (Başlangıç: $-\infty$)
* **Beta ($\beta$):** `MIN` oyuncusunun (rakibin) şu ana kadar garantilediği **en düşük** skordur. (Başlangıç: $+\infty$)

---

## 📊 Performans Analizi ve Test Sonuçları

Aşağıdaki testler, oyuncunun (X) her hamlesine karşılık yapay zekanın (O) optimal hamleyi bulmak için ne kadar hesaplama yaptığını göstermektedir.

### Performans Özeti
| Hamle (AI) | Algoritma | Gezilen Düğüm Sayısı | Süre (ms) | Analiz |
| :--- | :--- | :--- | :--- | :--- |
| **1. Hamle** | Minimax | 59,704 | 75.32 | Tam arama |
| (8 boş kare) | **Alfa-Beta** | **7,500** | **10.55** | **~7 kat daha hızlı, %87 daha az düğüm** |
| **2. Hamle** | Minimax | 1,052 | 4.52 | - |
| (6 boş kare) | **Alfa-Beta** | **524** | **1.10** | **~4 kat daha hızlı, %50 daha az düğüm** |
| **3. Hamle** | Minimax | 46 | 0.08 | - |
| (4 boş kare) | **Alfa-Beta** | **42** | **0.06** | Performanslar yakınsıyor |
| **4. Hamle** | Minimax | 4 | 0.03 | - |
| (2 boş kare) | **Alfa-Beta** | **4** | **0.01** | Budanacak dal kalmadı, performans eşit |

<br>

### Test Adımları (Görsel Çıktılar)

#### 1. Oyun Başlangıcı (Hamle Yok)
* **Durum:** Tahta boş. "Sıra sizde (X)" mesajı görüntüleniyor.
* **Performans:** AI henüz hesaplama yapmadı (Düğüm: 0, Süre: 0).

<img src="https://github.com/user-attachments/assets/d6b7c68a-8d58-443d-a1bb-f68aaf72735b" width="400" />

---

#### 2. AI'ın İlk Hamlesi (Merkezi Seçim)
* **Durum:** Oyuncu (X) sol üste (7) oynadı. AI (O) merkeze (5) karşılık verdi.
* **Minimax:** 59,704 Düğüm | 75.32 ms
* **Alfa-Beta:** 7,500 Düğüm | 10.55 ms
> **Analiz:** Projenin ana tezini kanıtlayan en net görüntü budur. Alfa-Beta budaması, Minimax'ın gezdiği düğüm sayısının sadece **%12'sini** gezerek ve yaklaşık **7 kat daha hızlı** bir sürede aynı optimal hamleyi bulmuştur.

<img src="https://github.com/user-attachments/assets/0d78d8a9-50ec-467c-9828-dedb64b82a18" width="400" />

---

#### 3. Oyun Ortası
* **Durum:** Oyuncu (X) sağ alta (3) oynadı. AI (O) alt ortaya (2) karşılık verdi.
* **Minimax:** 1,052 Düğüm | 4.52 ms
* **Alfa-Beta:** 524 Düğüm | 1.10 ms
> **Analiz:** Olasılıklar azaldıkça arama ağacı küçüldü. Alfa-Beta hala Minimax'ın yaklaşık yarısı kadar düğümü gezerek **4 kat daha hızlı** çalışmaktadır.

<img src="https://github.com/user-attachments/assets/9192fe60-8e30-44ba-9ee2-fd4798afd12c" width="400" />

---

#### 4. Oyun Sonu (AI 3. Hamle)
* **Durum:** Oyuncu (X) üst ortaya (8) oynadı. AI (O) sağ üste (9) oynayarak kazanmayı engelledi.
* **Minimax:** 46 Düğüm | 0.08 ms
* **Alfa-Beta:** 42 Düğüm | 0.06 ms
> **Analiz:** Olası hamle sayısı çok azaldığı için (arama ağacı çok küçüldüğü için), Alfa-Beta'nın "budayabileceği" çok az dal kalmıştır. Bu nedenle iki algoritmanın performansı neredeyse eşitlenmiştir.

<img src="https://github.com/user-attachments/assets/4b319e04-c0ab-49bf-a01e-077ebc02b253" width="400" />

---

#### 5. AI'ın Son Hamlesi
* **Durum:** Oyuncu (X) sol alta (1) oynadı. AI (O) kalan iki seçenekten birini (orta sol - 4) oynadı.
* **Minimax:** 4 Düğüm | 0.03 ms
* **Alfa-Beta:** 4 Düğüm | 0.01 ms
> **Analiz:** Arama ağacı o kadar küçülmüştür ki, budama yapmanın hiçbir avantajı kalmamıştır.

<img src="https://github.com/user-attachments/assets/572f7ec9-216b-4286-8407-fc10a36f8f86" width="400" />

---

#### 6. Sonuç: Berabere
* **Durum:** Oyuncu (X) son kareye (6) oynadı ve tahta doldu.
* **Sonuç:** "Oyun Berabere!"
* **Performans:** AI yeni bir hesaplama yapmadığı için önceki adımın değerleri (4 Düğüm) geçerlidir.

<img src="https://github.com/user-attachments/assets/006d2e2c-d8c8-4771-8d75-0364f4f1f41e" width="400" />

---

## 🚀 Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için:

1.  Depoyu klonlayın:
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git](https://github.com/KULLANICI_ADINIZ/PROJE_ADINIZ.git)
    cd PROJE_ADINIZ
    ```
2.  (Varsa) Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
3.  Uygulamayı çalıştırın:
    ```bash
    python main.py
    ```

## 📄 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.
