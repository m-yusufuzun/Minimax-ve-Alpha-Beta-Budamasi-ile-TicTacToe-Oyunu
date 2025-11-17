X-O (Tic Tac Toe) oyununun ve uygulanan Minimax ve Alfa-Beta Budaması algoritmalarının teknik detayları, görsel çıktıları ve performans testlerinin sonuçları sunulmuştur.

Minimax Algoritması

  Minimax, X-O gibi iki oyunculu, sıfır toplamlı (bir oyuncunun kazancı diğerinin kaybına eşit olan) ve tam bilgili (her iki oyuncunun da oyunun tüm durumunu bildiği) oyunlar için kullanılan bir karar verme algoritmasıdır. Algoritmanın temel amacı, bir sonraki hamlenin en optimal (en iyi) hamle olmasını sağlamaktır.
    
Alfa-Beta Budaması (Alpha-Beta Pruning)

  Alfa-Beta Budaması, Minimax algoritmasının bir optimizasyonudur. Minimax'ın en büyük problemi, özellikle karmaşık oyunlarda (X-O basit olsa da, satranç gibi) oyun ağacının çok hızlı büyümesi ve hesaplama maliyetinin aşırı artmasıdır.
  Alfa-Beta Budaması, Minimax ağacının tamamını keşfetmek yerine, "gereksiz" veya "sonucu değiştirmeyecek" dalları budayarak arama işlemini hızlandırır. Bunu yaparken Alfa (α) ve Beta (β) adında iki değer tutar.

  Alfa (α): MAX oyuncusunun (bizim) şu ana kadar garantilediği en yüksek skordur. Başlangıçta -∞ (eksi sonsuz) olarak ayarlanır.
  Beta (β): MIN oyuncusunun (rakibin) şu ana kadar garantilediği en düşük skordur. Başlangıçta +∞ (artı sonsuz) olarak ayarlanır.

Ekran Çıktıları & Test Sonuçları

Durum: Bu, oyunun başlangıç anıdır. Tahta tamamen boştur.

Açıklama: "Sıra sizde (X)" yazısı, programın ilk hamleyi oyuncudan beklediğini gösterir.

Performans: "Minimax" ve "Alfa-Beta" için Düğüm ve Süre değerleri 0'dır, çünkü yapay zeka henüz bir hamle hesaplaması yapmamıştır.
