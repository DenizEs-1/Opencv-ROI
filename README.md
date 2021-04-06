Yapılan projenin amacı: bir resimde kareye aldığımız alanın koordinatlarını otomatik olarak elde etmektir.
Bunun için opencv kütüphanesindeki ROI methodunu kullandık.

Projenin işleyişi şu şekildedir:
Öncelikle kullancağımız resmi imread komutuyla çekiyoruz. (Burada resmin adresini yazmamız lazım, fakat python kodumuzla aynı yerdeyse sadece adını yazmak yeterlidir.)
Kullanıcıdan kaç adet kareleme yapcağı bilgisini alıyoruz.
Ardından neyi kareleceğini sorup, açılan resimde alanı seçip entera tıklayınca koordinatlarını kaydediyor.
Bu isimler ve koordinatlarını bir dictionaryde saklıyoruz. Böyle ismini girdiğimizde bize onun koordinatlarını verecektir.

Burada elde edilen koordinat 4 değere sahiptir. İlk ikisi: oluşan dörtgenin sol üst köşesindeki x ve y noktasını verir. 
Diğer ikisi ise sol üst köşe ile sağ alt köşe arasındaki x ve y uzaklıklarını verir.
Kısaca koordinat (a,b,c,d) değerleriyse. Sol üst köşe koordinatı(a,b), sağ alt köşe koordinatı (a+c,b+d) dir.

KURULMASI GEREKENLER
-python 3.6
-opencv
-opencv_contrib 