# Salam Hər vaxtınız xeyir , Task bank sistemilə bağlıdı. 
# # İlk classımızda bizim hesab nömrəsi (int) və balans argumentlərimiz olacaq.
# # Metod olaraq 3 fərqli metoddan istifadə edəcəyik Balansı artırmaq,  
# Pul çıxarmaq  və balansı göstərmək üçün metodlar.
# # # İkinci classımız isə kreditlə bağlıdır. İlk classımızı bu classa inheritance eliyəcəyik və  
# super initdən  istifadə edəcəyik.   Bu classda bizim 2 metodumuz olacaq. Kredit vermək və kredit ödənişi. 
# Bu səbəbdən classımızın əlavə kimi 1 argumenti olacaq.
# Kredit götürüləcək məbləğ. Kredit sadəcə 1 il müddəti üçündür
# və faiz yoxdur (kreditinməbləği / 12=aylıq ödəniş).

class Info ():
    def __init__(self, hesabNo,balans,*args):
        self.hesabNo=hesabNo
        self.balans=balans
    
    def artir(self,mebleg):
        self.mebleg=mebleg
        self.balans+=self.mebleg
        print(f"Balansiniz {self.mebleg} azn artirildi.\nBalansiniz {self.balans} azn teskil edir")
    
    def cixar(self,mebleg):
        self.mebleg=mebleg
        if self.mebleg<=self.balans:
            self.balans-=self.mebleg
            print(f"Balansinizdan {self.mebleg} azn cixildi.\nBalansiniz {self.balans} azn teskil edir")
        else:
            print("Balansinizda kifayet qeder vesait yoxdur")
        
    def goster(self):
        print(f"Balansiniz {self.balans} azn teskil edir")

class Kredit (Info):
    def __init__(self,*args):
        super().__init__(*args)

    def kreditGotur(self,kreditMebleg):
        self.kreditMebleg=kreditMebleg
        self.balans+=self.kreditMebleg
        print(f"Hormetli musteri siz {kreditMebleg} azn kredit goturdunuz.\nIndi sizin balansiniz {self.balans} azn teskil edir")

    def kreditOde(self):
        if self.kreditMebleg:
            self.odenen=(self.kreditMebleg/12)
            if self.odenen<=self.balans:
                self.kreditMebleg-=self.odenen
                self.balans-=self.odenen   
                print(f"Hormetli musteri sizin {self.odenen} azn kredit borcunuz odenildi.\nCari kredit borcunuz{self.kreditMebleg} azn teskil edir")
            else:
                print("Hormetli musteri sizin kredit odemek ucun balnsinizda kifayet qeder vesait yoxdur")         
        else:
            print("Siz kredit goturmemisiniz")


kredit=Kredit(500,3000,1000)
# print(kredit.artir(2332))
