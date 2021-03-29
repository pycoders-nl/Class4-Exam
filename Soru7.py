# "Yazici Ciftligi" adını verdiğiniz milyon dolarlık bir is fikrine sahipsiniz.
# Pek çok insanın ofislerinde ve evlerinde yazıcı kullandığını biliyorsunuz ve bunun hiç mantıklı olmadigini dusunuyorsunuz.
# Neden tüm yazıcıları yazıcı çiftliğinizde birleştirip, kullanıcıların yazicilarinizi kullanarak dosyalar yazdirmasini saglayip,
# bu dosyaları postayla onlara göndermeyesiniz ki?
# Elbette bu harika bir fikir, bu yüzden hemen başlamaya karar veriyorsunuz.
# Ana sorun, sunucuza gelen binlerce yazdırma komutunu işlemek ve bunları sahip olduğunuz 64 yazıcıya tek tek göndermek.
# Amaç, herhangi bir baskı talebini aldıktan sonra 1 saat içinde baskiyi tamamlamak ve göndermek.
# Hizmetinizin kullanıcı sayısının hızla artacağını tahmin ediyorsunuz, bu nedenle işiniz büyüdükçe taleple başa çıkmak için
# yeni sunucular ve yazıcılar ekleyebilmeniz gerek.
# Kullanmanız gereken veri yapıları, bu veri yapilarinin nasil uygulamaya dokulecegi ve baskı hizmetini
# etkin bir şekilde çalıştırmak için gerekli olacak algoritmalar hakkında yaklasik 10 cümle ile kısa bir paragraf yazın.
# Seçimlerinizi çalışma süresi ve depolama boyutu açısından açıklayın. (Time & Space Complexity)


# Burada FIFO mantigiyla bir algoritam yazmamiz gerekli. Cunku dosyasini ilk gonderenin cikitisinin ilk alinmasi lazim.
# Bunu uygulamak icin bir stack uygulamasi gelistirmek lazim. Her ciktiya alinan dosyanin stackten silinmesi lazim.
# Time complexity 1 cunku ilk elimize gelen dosyayi cagiriyoruz burda. Ama space complexity si fazla. Gonderilen datalar kadar yerimizin olmasi lazim.
#
