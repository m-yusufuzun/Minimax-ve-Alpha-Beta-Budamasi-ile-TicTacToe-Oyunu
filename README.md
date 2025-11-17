<b>X-O (Tic Tac Toe) oyununun ve uygulanan Minimax ve Alfa-Beta Budaması algoritmalarının teknik detayları, görsel çıktıları ve performans testlerinin sonuçları sunulmuştur.</b>

<h2>Minimax Algoritması</h2>

  Minimax, X-O gibi iki oyunculu, sıfır toplamlı (bir oyuncunun kazancı diğerinin kaybına eşit olan) ve tam bilgili (her iki oyuncunun da oyunun tüm durumunu bildiği) oyunlar için kullanılan bir karar verme algoritmasıdır. Algoritmanın temel amacı, bir sonraki hamlenin en optimal (en iyi) hamle olmasını sağlamaktır.
    
<h2>Alfa-Beta Budaması (Alpha-Beta Pruning)</h2>

  Alfa-Beta Budaması, Minimax algoritmasının bir optimizasyonudur. Minimax'ın en büyük problemi, özellikle karmaşık oyunlarda (X-O basit olsa da, satranç gibi) oyun ağacının çok hızlı büyümesi ve hesaplama maliyetinin aşırı artmasıdır.
  Alfa-Beta Budaması, Minimax ağacının tamamını keşfetmek yerine, "gereksiz" veya "sonucu değiştirmeyecek" dalları budayarak arama işlemini hızlandırır. Bunu yaparken Alfa (α) ve Beta (β) adında iki değer tutar.

  Alfa (α): MAX oyuncusunun (bizim) şu ana kadar garantilediği en yüksek skordur. Başlangıçta -∞ (eksi sonsuz) olarak ayarlanır.
  Beta (β): MIN oyuncusunun (rakibin) şu ana kadar garantilediği en düşük skordur. Başlangıçta +∞ (artı sonsuz) olarak ayarlanır.

<h2>Ekran Çıktıları & Test Sonuçları</h2>

<img width="452" height="837" alt="Ekran görüntüsü 2025-11-16 192852" src="https://github.com/user-attachments/assets/d6b7c68a-8d58-443d-a1bb-f68aaf72735b" />

Durum: Bu, oyunun başlangıç anıdır. Tahta tamamen boştur.

Açıklama: "Sıra sizde (X)" yazısı, programın ilk hamleyi oyuncudan beklediğini gösterir.

Performans: "Minimax" ve "Alfa-Beta" için Düğüm ve Süre değerleri 0'dır, çünkü yapay zeka henüz bir hamle hesaplaması yapmamıştır.


<img width="452" height="837" alt="Ekran görüntüsü 2025-11-16 192936" src="https://github.com/user-attachments/assets/0d78d8a9-50ec-467c-9828-dedb64b82a18" />

Durum: Oyuncu 'X' ilk hamlesini sol üst köşeye (7) oynamıştır. Yapay zeka 'O' ise bu hamleye karşılık olarak merkezi (5) seçmiştir.

Açıklama: Bu, yapay zekanın oyundaki ilk ve en karmaşık hamlesidir. AI'ın 8 olası hamlesi vardı.

Performans:
Minimax: 59,704 Düğüm | 75.32 ms
Alfa-Beta: 7,500 Düğüm | 10.55 ms

Analiz: Projenizin ana tezini kanıtlayan en net görüntü budur. Alfa-Beta budaması, Minimax'ın gezdiği düğüm sayısının sadece %12'sini gezerek (59,704 yerine 7,500) ve yaklaşık 7 kat daha hızlı (75ms yerine 10ms) bir sürede aynı optimal hamleyi (merkezi) bulmuştur.


<img width="452" height="837" alt="Ekran görüntüsü 2025-11-16 192957" src="https://github.com/user-attachments/assets/9192fe60-8e30-44ba-9ee2-fd4798afd12c" />

Durum: Oyuncu 'X' ikinci hamlesini sağ alt köşeye (3) oynamıştır. Yapay zeka 'O' ise buna karşılık olarak alt ortaya (2) oynamıştır.

Açıklama: Tahtadaki boş kare sayısı azaldıkça, algoritmaların hesaplaması gereken toplam olasılık da (düğüm sayısı) azalmıştır.

Performans:
Minimax: 1,052 Düğüm | 4.52 ms
Alfa-Beta: 524 Düğüm | 1.10 ms

Analiz: Alfa-Beta, budama yaparak hala Minimax'ın yaklaşık yarısı kadar düğümü gezmektedir ve 4 kat daha hızlıdır


<img width="452" height="837" alt="Ekran görüntüsü 2025-11-16 193018" src="https://github.com/user-attachments/assets/4b319e04-c0ab-49bf-a01e-077ebc02b253" />

Durum: Oyuncu 'X' üst ortaya (8) oynamıştır. AI 'O' ise sağ üste (9) oynamıştır (oyuncunun kazanmasını engellemek için).

Açıklama: Oyun sonuna yaklaşıldı. Tahtada sadece 3 boş kare kaldı.

Performans:
Minimax: 46 Düğüm | 0.08 ms
Alfa-Beta: 42 Düğüm | 0.06 ms

Analiz: Olası hamle sayısı çok azaldığı için (arama ağacı çok küçüldüğü için), Alfa-Beta'nın "budayabileceği" çok az dal kalmıştır. Bu nedenle iki algoritmanın performansı neredeyse eşitlenmiştir.


<img width="452" height="837" alt="Ekran görüntüsü 2025-11-16 193035" src="https://github.com/user-attachments/assets/572f7ec9-216b-4286-8407-fc10a36f8f86" />

Durum: Oyuncu 'X' sol alta (1) oynamıştır. AI 'O' ise orta sola (4) oynamıştır.

Açıklama: AI'ın yapabil-eceği sadece iki hamle kalmıştı.

Performans:
Minimax: 4 Düğüm | 0.03 ms
Alfa-Beta: 4 Düğüm | 0.01 ms

Analiz: Arama ağacı o kadar küçülmüştür ki, budama yapmanın hiçbir avantajı kalmamıştır. İki algoritma da aynı 4 olasılığı kontrol etmiştir.


<img width="452" height="837" alt="Ekran görüntüsü 2025-11-16 193051" src="https://github.com/user-attachments/assets/006d2e2c-d8c8-4771-8d75-0364f4f1f41e" />

Durum: Tahtada kalan son boş kareye (orta sağ - 6) oyuncu 'X' oynamış ve tahta dolmuştur.

Açıklama: "Oyun Be-rabere!" yazısı, check_ga-me_over fonksiyonunun çalıştığını ve kazanan olmadığını tespit ettiğini gösterir.

Performans: Performans sayıları (Minimax: 4, Alfa-Beta: 4) bir önceki adımdaki (AI'ın son hamlesi) sayıların aynısıdır. Oyuncunun son hamlesi bir AI hesaplamasını tetiklemediği için bu değerler değişmemiştir

