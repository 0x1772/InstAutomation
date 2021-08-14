from builtins import print

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
from datetime import datetime
import os
import urllib.request
import requests
import getpass
from termcolor import colored
from colorama import init
import threading
from random import randint
import json

class Instagram():
    def __init__(self):
        init(convert=True)
        self.config=None
        self.dil = None
        self.ayarlarYukle()
        self.dilYukle()
        self.script()
        self.tarayiciThreadOlustur()
        self.girisYapildimi = False
        self.tarayiciAcildimi = False
        self.aktifKullanici = ""
        self.index = 1
        self.BASE_URL = "https://www.instagram.com/"
        self.girisYap()

    def script(self):
        print("")
        self.uyariOlustur("   _____           _ _      ____        _   ", 1)
        self.uyariOlustur("  / ____|         (_) |    |  _ \      | |  ", 1)
        self.uyariOlustur("  | (___  _ __ ___ _| | __ | |_) | ___ | |_ ", 1)
        self.uyariOlustur("  \___ \| '_ ` _ \| | |/ _ \  _ < / _ \| __|", 1)
        self.uyariOlustur("  ____) | | | | | | | |  __/ |_) | (_) | |_ ", 1)
        self.uyariOlustur(" |_____/|_| |_| |_|_|_|\___|____/ \___/ \__|", 1)
        self.uyariOlustur("# ==============================================================================", 1)
        self.uyariOlustur("# author       :Inenarratus", 1)
        self.uyariOlustur("# telegram     :https://t.me/Inenarratus", 1)
        self.uyariOlustur("# github       :https://github.com/Inenarratus", 1)
        self.uyariOlustur("# uyarı        :Kullanıcı Adı Ve Şifrenizle Giriş Yapmanız Dahilinde Sorumluluğu Kabul Etmiş Olursunuz..", 2)
        self.uyariOlustur("# uyarı        :fakesmile.co sitesini ziyaret edebilirsiniz...", 2)
        self.uyariOlustur("# ==============================================================================", 1)
        print("")

    def menu(self):
        menu = self.configGetir("languages.{dil}.menu".format(dil=self.dil))
        for secenek in menu:
            self.uyariOlustur(secenek, 3)
        self.islemSec()

    def islemSec(self):
        base_warnings = self.BASE_UYARI(metod=self.islemSec, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.islemSec, inputs=True)
        secim = input(self.configGetir(base_inputs + "input1")).strip()
        if secim:
            try:
                secim = int(secim)
                if 0 < secim < 27:
                    self.secilenIslemiGoster(secim)
                    if secim in [1, 2, 3, 9, 12, 20, 21, 22, 23]:
                        self.profilSec(secim)
                    elif secim == 4:
                        self.topluTakiptenCik()
                    elif secim == 5:
                        self.topluYorumYapma()
                    elif secim == 6:
                        self.takipEtmeyenleriTakiptenCik()
                    elif secim == 7:
                        self.topluMesajSilme()
                    elif secim == 8:
                        self.oneCikanHikayeIndir()
                    elif secim in [10, 11]:
                        self.gonderiIndir()
                    elif secim == 13:
                        self.kullaniciListesiTakipEt(secim=secim)
                    elif secim == 14:
                        self.gonderiBegenenleriTakipEt()
                    elif secim == 15:
                        self.etiketeGoreTakipEtme()
                    elif secim == 16:
                        self.etiketeGoreBegenme()
                    elif secim == 17:
                        self.gonderiBegen()
                    elif secim == 18:
                        self.gonderiBegen(False)
                    elif secim == 19:
                        self.gonderiYorumYapma()
                    elif secim == 24:
                        self.ayarlar()
                    elif secim == 25:
                        self.oturumKapat()
                    elif secim == 26:
                        self.quit()
                else:
                    self.uyariOlustur(self.configGetir(base_warnings + "warning1"), 2)
                    self.islemSec()
            except Exception:
                self.uyariOlustur(self.configGetir(base_warnings + "warning2"), 2)
                self.islemSec()
        else:
            self.islemSec()

    def secilenIslemiGoster(self, secim):
        base_warnings = self.BASE_UYARI(metod=self.secilenIslemiGoster, warnings=True)
        secimler = self.configGetir("languages.{dil}.warnings.secilenIslemiGoster.secimler".format(dil=self.dil))
        print("")
        self.uyariOlustur(secimler.get(str(secim), self.configGetir(base_warnings + "warning1")), 1)
        if secim < 24:
            self.uyariOlustur(self.configGetir(base_warnings + "warning2"), 3)
        print("")

    def profilSec(self, secim):
        base_warnings = self.BASE_UYARI(metod=self.profilSec, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.profilSec, inputs=True)

        kullanici = input(self.configGetir(base_inputs + "input1")).strip()

        if not kullanici:
            self.profilSec(secim)

        self.anaMenuyeDonsunMu(kullanici)

        if self.kullaniciKontrol(kullanici):
            print(str(self.configGetir(base_warnings + "warning1")).format(kullanici=kullanici))
            if secim == 1:
                self.gonderileriIndir(kullanici, secim)
            elif secim == 2:
                self.gonderileriBegen(kullanici, secim)
            elif secim == 3:
                self.gonderileriBegen(kullanici, secim, False)
            elif secim == 9:
                self.hikayeIndir(kullanici, secim)
            elif secim == 12:
                self.kullaniciTakipcileriniTakipEt(kullanici, secim)
            elif secim == 20:
                self.kullaniciTakipEt(kullanici, secim)
            elif secim == 21:
                self.kullaniciTakipEt(kullanici, secim, False)
            elif secim == 22:
                self.kullaniciEngelle(kullanici, secim)
            elif secim == 23:
                self.kullaniciEngelle(kullanici, secim, False)
        else:
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning2")).format(kullanici=kullanici), 2)
            self.profilSec(secim)

    def ilkGonderiTikla(self):
        ilkGonderi = self.driver.find_elements_by_css_selector("article div.v1Nh3")[0]
        ilkGonderi.click()

    def gonderileriIndir(self, kullanici, secim):
        base_warnings = self.BASE_UYARI(metod=self.gonderileriIndir, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.gonderileriIndir)

        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                print(str(self.configGetir(base_warnings+"warning1")).format(
                    kullanici=kullanici))
                gonderiSayisi = self.gonderiSayisi()
                gonderiSayisi=int(self.metindenKarakterSil(gonderiSayisi,','))
                self.gonderiVarMi(kullanici, gonderiSayisi, secim)
                self.ilkGonderiTikla()
                sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
                self.klasorOlustur(kullanici)
                self.indexSifirla()
                for index in range(gonderiSayisi):
                    if self.gonderiAlbumMu():
                        self.klasorOlustur(str(self.index) + "_album")
                        tempIndex = self.index
                        self.indexSifirla()
                        self.albumUrlGetir()
                        self.klasorDegistir("../")
                        self.index = tempIndex + 1
                    else:
                        [url, veriTuru] = self.gonderiUrlGetir()
                        if url is not None:
                            self.dosyaIndir(url, veriTuru)
                        else:
                            continue
                    self.gonderiIlerlet()
                    sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
                self.klasorDegistir("../")
                print(str(self.configGetir(base_warnings+"warning2")).format(
                    kullanici=kullanici))
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(
                    kullanici=kullanici), 2)

            self.profilSec(secim)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(kullanici=kullanici, hata=error), 2)
            self.profilSec(secim)

    def gonderileriBegen(self, kullanici, secim, durum=True):
        base_warnings = self.BASE_UYARI(metod=self.gonderileriBegen, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.gonderileriBegen)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                print(str(self.configGetir(base_warnings+"warning1")).format(
                    kullanici=kullanici))
                gonderiSayisi = self.gonderiSayisi()
                gonderiSayisi = int(self.metindenKarakterSil(gonderiSayisi, ','))
                self.gonderiVarMi(kullanici, gonderiSayisi, secim)
                self.ilkGonderiTikla()
                sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
                self.indexSifirla()
                for index in range(gonderiSayisi):
                    btn_begen = self.begenButon()
                    begeniDurum = self.begenButonuDurumGetir(btn_begen)
                    if durum:
                        if begeniDurum == "like":
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(index=str(self.index),
                                                                                                     url=self.driver.current_url), 1)
                            self.gonderiBegenDurumDegistir(btn_begen)
                        else:
                            print(str(self.configGetir(base_warnings+"warning3")).format(url=self.driver.current_url))
                            self.gonderiIlerlet()
                            sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
                    else:
                        if begeniDurum == "unlike":
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(index=str(self.index),
                                                                                                     url=self.driver.current_url),
                                              1)
                            self.gonderiBegenDurumDegistir(btn_begen)
                        else:
                            print(str(self.configGetir(base_warnings+"warning5")).format(url=self.driver.current_url))
                            self.gonderiIlerlet()
                            sleep(self.configGetir("{base}sleep3".format(base=base_sleep)))
                print(str(self.configGetir(base_warnings+"warning6")).format(
                    kullanici=kullanici))
                self.profilSec(secim)
            else:
                if durum:
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning7")).format(
                        kullanici=kullanici), 2)
                else:
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning8")).format(
                        kullanici=kullanici), 2)
                self.profilSec(secim)
        except Exception as error:
            if durum:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning9")).format(
                    kullanici=kullanici, hata=error), 2)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning10")).format(
                    kullanici=kullanici, hata=error), 2)
            self.profilSec(secim)

    def topluTakiptenCik(self):
        base_warnings = self.BASE_UYARI(metod=self.topluTakiptenCik, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.topluTakiptenCik)
        try:
            print(self.configGetir(base_warnings+"warning1"))
            self.kullaniciProfilineYonlendir(self.aktifKullanici)
            btn_takipEdilenler = self.takipEdilenlerButon()
            takipEdilenSayisi = btn_takipEdilenler.find_element_by_css_selector("span.g47SY").text
            takipEdilenSayisi = int(self.metindenKarakterSil(takipEdilenSayisi, ','))
            btn_takipEdilenler.click()
            sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
            self.indexSifirla()
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takip in takipListe:
                    takipEdilenKullanıcıAdi = self.takipEdilenKullaniciAdiGetir(element=takip)
                    btn_takip = takip.find_element_by_css_selector('button.sqdOP')
                    if btn_takip.text == "Following":
                        btn_takip.click()
                        sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
                        try:
                            btn_onay = self.driver.find_element_by_css_selector("div.mt3GC > button.aOOlW")
                            btn_onay.click()
                        except Exception as error:
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(
                                kullanici=takipEdilenKullanıcıAdi, hata=str(error)), 2)
                            continue
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(
                            index=self.index, kullanici=takipEdilenKullanıcıAdi), 1)
                        self.indexArtir()
                        if (self.index - 1) >= takipEdilenSayisi:
                            devamEtsinMi = False
                            break
                        sleep3=self.configGetir("{base}sleep3".format(base=base_sleep))
                        sleep(self.beklemeSuresiGetir(sleep3[0],sleep3[1]))
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(
                            hata=str(error)), 2)
                        pass
                    sleep(self.configGetir("{base}sleep4".format(base=base_sleep)))
            print(self.configGetir(base_warnings + "warning5"))
            self.menu()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(hata=str(error)), 2)
            self.menu()

    def topluYorumYapma(self, url=None, yorumSayisi=None, secilenIslem=None):
        base_warnings = self.BASE_UYARI(metod=self.topluYorumYapma, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.topluYorumYapma, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.topluYorumYapma)
        sleep1 = self.configGetir(base_sleep + "sleep1")
        try:
            if url is None:
                url = input(self.configGetir(base_inputs + "input1")).strip()
                self.anaMenuyeDonsunMu(url)

                self.urlGirildiMi(url=url, metod=self.topluYorumYapma)
                self.urlGecerliMi(url=url, metod=self.topluYorumYapma)

                print(str(self.configGetir(base_warnings + "warning1")).format(url=url))
                self.urlYonlendir(url)

                if not self.sayfaMevcutMu():
                    self.uyariOlustur(str(self.configGetir(base_warnings + "warning2")).format(url=url), 2)
                    self.topluYorumYapma()

                if self.hesapGizliMi():
                    self.uyariOlustur(
                        str(self.configGetir(base_warnings + "warning3")).format(
                            url=url), 2)
                    self.topluYorumYapma()

            if not yorumSayisi:
                yorumSayisi = input(self.configGetir(base_inputs + "input2")).strip()
                self.anaMenuyeDonsunMu(yorumSayisi)
                if yorumSayisi.isnumeric() and int(yorumSayisi) > 0:
                    yorumSayisi = int(yorumSayisi)
                    if self.yorumLimitiAsildiMi(yorumSayisi):
                        yorumSayisi = 50
                        print(self.configGetir(base_warnings + "warning4"))
                else:
                    self.uyariOlustur(self.configGetir(base_warnings + "warning5"), 2)
                    self.topluYorumYapma(url=url, yorumSayisi=None, secilenIslem=None)

            if not secilenIslem:
                for secenek in self.configGetir(base_warnings + "warning6"):
                    self.uyariOlustur(secenek, 3)
                secilenIslem = str(input(self.configGetir(base_inputs + "input3")).strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                self.uyariOlustur(self.configGetir(base_warnings + "warning7"), 1)
                print(str(self.configGetir(base_warnings + "warning8")).format(url=url))
                for i in range(yorumSayisi):
                    yorum = self.rastgeleYorumGetir()
                    yorum = self.yorumUzunlukBelirle(yorum)
                    self.yorumYap(yorum)
                    self.uyariOlustur(str(self.configGetir(base_warnings + "warning9")).format(index=i + 1), 1)

                    sleep(self.beklemeSuresiGetir(sleep1[0], sleep1[1]))
            elif secilenIslem == "2":
                self.uyariOlustur(self.configGetir(base_warnings + "warning10"), 1)
                dosya = self.dosyaSec()
                yorumlar = self.dosyaIceriginiAl(dosya)
                if self.dosyaIcerigiAlindiMi(yorumlar):
                    print(str(self.configGetir(base_warnings + "warning11")).format(url=url))
                    for index, yorum in enumerate(yorumlar):
                        yorum = self.yorumUzunlukBelirle(yorum)
                        self.yorumYap(yorum)
                        self.uyariOlustur(str(self.configGetir(base_warnings + "warning12")).format(index=index + 1), 1)
                        if (index + 1) == yorumSayisi:
                            break
                        sleep(self.beklemeSuresiGetir(sleep1[0], sleep1[1]))
                else:
                    self.topluYorumYapma(url=url, yorumSayisi=yorumSayisi, secilenIslem=secilenIslem)
            else:
                self.uyariOlustur(self.configGetir(base_warnings + "warning13"), 2)
                print("")
                self.topluYorumYapma(url=url, yorumSayisi=yorumSayisi, secilenIslem=None)

            print(str(self.configGetir(base_warnings + "warning14")).format(url=url))
            self.topluYorumYapma()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning15")).format(url=url, hata=str(error)), 2)
            self.topluYorumYapma()

    def takipEtmeyenleriTakiptenCik(self):
        base_warnings = self.BASE_UYARI(metod=self.takipEtmeyenleriTakiptenCik, warnings=True)
        try:
            print(self.configGetir(base_warnings + "warning1"))
            takipciler = self.takipcileriGetir()
            print(self.configGetir(base_warnings + "warning2"))
            print(self.configGetir(base_warnings + "warning3"))
            self.takipEdilenleriGetir(takipciler=takipciler)
            print(self.configGetir(base_warnings + "warning4"))
            self.menu()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning5")).format(
                hata=str(error)), 2)
            self.menu()

    def topluMesajSilme(self):
        base_warnings = self.BASE_UYARI(metod=self.topluMesajSilme, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.topluMesajSilme)
        try:

            print(self.configGetir(base_warnings+"warning1"))
            self.kullaniciProfilineYonlendir('direct/inbox/')
            devamEtsinMi = True
            silinenMesajlar = set()
            self.indexSifirla()
            while devamEtsinMi:
                mesajListesi = self.driver.find_elements_by_css_selector("div.N9abW  a.rOtsg")
                if len(mesajListesi) == 0:
                    print(self.configGetir(base_warnings+"warning2"))
                    break
                for mesaj in mesajListesi:
                    if mesaj not in silinenMesajlar:
                        silinenMesajlar.add(mesaj)
                        kullaniciAdi = mesaj.find_element_by_css_selector("._7UhW9.xLCgt.MMzan.KV-D4.fDxYl").text
                        print(str(self.configGetir(base_warnings+"warning3")).format(index=self.index,kullanici=kullaniciAdi))
                        self.mesajSil(mesaj)
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(index=self.index, kullanici=kullaniciAdi), 1)
                        self.indexArtir()
                        sleep1 = self.configGetir(base_sleep + "sleep1")
                        sleep(self.beklemeSuresiGetir(sleep1[0], sleep1[1]))
                    break

            print(self.configGetir(base_warnings+"warning5"))
            self.menu()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(hata=str(error)),2)
            self.menu()

    def oneCikanHikayeIndir(self):
        base_warnings = self.BASE_UYARI(metod=self.oneCikanHikayeIndir, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.oneCikanHikayeIndir, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.oneCikanHikayeIndir)

        try:
            url = input(self.configGetir(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(url)
            self.urlGirildiMi(url=url,metod=self.oneCikanHikayeIndir)
            self.urlGecerliMi(url=url,metod=self.oneCikanHikayeIndir)

            print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
            self.urlYonlendir(url)

            if not self.sayfaMevcutMu():
                self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
                self.oneCikanHikayeIndir()

            print(str(self.configGetir(base_warnings+"warning3")).format(url=url))
            btn_oynat = self.driver.find_element_by_css_selector("button._42FBe")
            btn_oynat.click()
            sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
            kullanici = self.driver.find_element_by_css_selector("a.FPmhX").get_attribute("title")
            self.klasorOlustur(kullanici)
            self.indexSifirla()
            self.hikayeleriGetir()
            self.klasorDegistir("../")
            print(str(self.configGetir(base_warnings+"warning4")).format(url=url))
            self.oneCikanHikayeIndir()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.oneCikanHikayeIndir()

    def hikayeIndir(self, kullanici, secim):
        base_warnings = self.BASE_UYARI(metod=self.hikayeIndir, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.hikayeIndir)

        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                if self.hikayeVarMi():
                    self.driver.find_element_by_css_selector("div.RR-M-").click()
                    sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
                    print(str(self.configGetir(base_warnings + "warning1")).format(
                        kullanici=kullanici))
                    self.klasorOlustur(kullanici)
                    self.indexSifirla()
                    self.hikayeleriGetir()
                    self.klasorDegistir("../")
                    print(str(self.configGetir(base_warnings + "warning2")).format(
                        kullanici=kullanici))
                else:
                    self.uyariOlustur(self.configGetir(base_warnings + "warning3"), 2)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings + "warning4")).format(
                    kullanici=kullanici), 2)
            self.profilSec(secim)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning5")).format(hata=str(error)), 2)
            self.profilSec(secim)

    def gonderiKullaniciAdi(self):
        return self.driver.find_element_by_css_selector("a.sqdOP").text

    def gonderiIndir(self):
        base_warnings = self.BASE_UYARI(metod=self.gonderiIndir, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.gonderiIndir, inputs=True)
        try:
            url = input(self.configGetir(base_inputs + "input1")).strip()
            self.anaMenuyeDonsunMu(url)
            self.urlGirildiMi(url=url, metod=self.gonderiIndir)
            self.urlGecerliMi(url=url, metod=self.gonderiIndir)

            print(str(self.configGetir(base_warnings + "warning1")).format(url=url))
            self.urlYonlendir(url)
            if not self.hesapGizliMi():
                print(str(self.configGetir(base_warnings + "warning2")).format(url=url))
                kullanici = self.gonderiKullaniciAdi()
                self.klasorOlustur(kullanici)
                if self.gonderiAlbumMu():
                    self.indexSifirla()
                    self.klasorOlustur(str(self.index) + "_album")
                    self.albumUrlGetir()
                    self.klasorDegistir("../")
                else:
                    [url, veriTuru] = self.gonderiUrlGetir()
                    if url is not None:
                        self.dosyaIndir(url, veriTuru)
                print(str(self.configGetir(base_warnings + "warning3")).format(url=url))
                self.klasorDegistir("../")
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings + "warning4")).format(
                    url=url), 2)
            self.gonderiIndir()
        except Exception as error:
            print(
                self.uyariOlustur(str(self.configGetir(base_warnings + "warning5")).format(hata=error), 2))
            self.gonderiIndir()

    def kullaniciTakipcileriniTakipEt(self, kullanici, secim, secilenIslem=None):
        base_warnings = self.BASE_UYARI(metod=self.kullaniciTakipcileriniTakipEt, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.kullaniciTakipcileriniTakipEt, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.kullaniciTakipcileriniTakipEt)

        try:
            self.kullaniciProfilineYonlendir(kullanici)
            hedefTakipciSayisi = None

            if secilenIslem is None:
                for secenek in self.configGetir(base_warnings + "warning1"):
                    self.uyariOlustur(secenek, 3)
                secilenIslem = str(input(self.configGetir(base_inputs + "input1")).strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                self.uyariOlustur(self.configGetir(base_warnings + "warning2"), 1)
            elif secilenIslem == "2":
                self.uyariOlustur(self.configGetir(base_warnings + "warning3"), 1)
                hedefTakipciSayisi = input(self.configGetir(base_inputs + "input2")).strip()
                self.anaMenuyeDonsunMu(hedefTakipciSayisi)
                if hedefTakipciSayisi.isnumeric():
                    hedefTakipciSayisi = int(hedefTakipciSayisi)
                else:
                    self.uyariOlustur(self.configGetir(base_warnings + "warning4"), 2)
                    print("")
                    self.kullaniciTakipcileriniTakipEt(kullanici=kullanici,secim= secim, secilenIslem=secilenIslem)
            else:
                self.uyariOlustur(self.configGetir(base_warnings + "warning5"), 2)
                print("")
                self.kullaniciTakipcileriniTakipEt(kullanici=kullanici,secim= secim, secilenIslem=None)

            if not self.hesapGizliMi():
                print(str(self.configGetir(base_warnings + "warning6")).format(kullanici=kullanici))
                devamEtsinMi = True
                self.indexSifirla()

                if hedefTakipciSayisi is None:
                    takipciSayisi = self.driver.find_elements_by_css_selector("a.-nal3 > span.g47SY")[0].get_attribute(
                        'title')
                    takipciSayisi = int(self.metindenKarakterSil(takipciSayisi, ','))
                else:
                    kaynakTakipciSayisi = self.driver.find_element_by_css_selector(
                        "a.-nal3 > span.g47SY").get_attribute('title')
                    kaynakTakipciSayisi = int(self.metindenKarakterSil(kaynakTakipciSayisi, ','))
                    takipciSayisi = self.hedefKaynaktanBuyukMu(hedefTakipciSayisi, kaynakTakipciSayisi)

                btn_takipciler = self.takipcilerButon()
                btn_takipciler.click()
                sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
                kontrolEdilenKullanicilar = set()
                while devamEtsinMi:
                    dialog_popup = self.driver.find_element_by_css_selector('div._1XyCr')
                    takipciListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                    for takipci in takipciListe:
                        takipciKullaniciAdi = takipci.find_element_by_css_selector("a.FPmhX").get_attribute('href')
                        takipciKullaniciAdi = takipciKullaniciAdi.replace(self.BASE_URL, '').replace('/', '')
                        try:
                            btn_takip = takipci.find_element_by_css_selector('button.sqdOP')
                            if btn_takip.text == "Follow":
                                print(str(self.configGetir(base_warnings + "warning7")).format(
                                    index=self.index, kullanici=takipciKullaniciAdi))
                                btn_takip.click()
                                self.indexArtir()
                                if self.index-1  >= takipciSayisi:
                                    devamEtsinMi = False
                                    break
                                sleep2 = self.configGetir("{base}sleep2".format(base=base_sleep))
                                sleep(self.beklemeSuresiGetir(sleep2[0], sleep2[1]))
                        except:
                            pass
                        kontrolEdilenKullanicilar.add(takipciKullaniciAdi)
                        if hedefTakipciSayisi:
                            if len(kontrolEdilenKullanicilar) >= kaynakTakipciSayisi:
                                devamEtsinMi = False
                        else:
                            if len(kontrolEdilenKullanicilar) >= takipciSayisi:
                                devamEtsinMi = False

                    if devamEtsinMi:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                        sleep(self.configGetir("{base}sleep3".format(base=base_sleep)))
                print(str(self.configGetir(base_warnings + "warning8")).format(kullanici=kullanici))
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings + "warning9")).format(kullanici=kullanici),
                                  2)
            self.profilSec(secim)
        except Exception as error:
            self.uyariOlustur(
                str(self.configGetir(base_warnings + "warning10")).format(kullanici=kullanici, hata=str(error)), 2)
            self.profilSec(secim)

    def kullaniciListesiTakipEt(self,secim):
        dosya = self.dosyaSec()
        kullanicilar = self.dosyaIceriginiAl(dosya)
        if self.dosyaIcerigiAlindiMi(kullanicilar):
            self.kullanicilariTakipEt(kullanicilar, secim)
        else:
            self.kullaniciListesiTakipEt(secim)
        self.kullaniciListesiTakipEt(secim)

    def gonderiBegenenleriTakipEt(self, url=None,secilenIslem=None):
        base_warnings = self.BASE_UYARI(metod=self.gonderiBegenenleriTakipEt, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.gonderiBegenenleriTakipEt, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.gonderiBegenenleriTakipEt)
        try:
            if url is None:
                url = input(self.configGetir(base_inputs+"input1")).strip()
                self.anaMenuyeDonsunMu(url)
                self.urlGirildiMi(url=url,metod=self.gonderiBegenenleriTakipEt)
                self.urlGecerliMi(url=url,metod=self.gonderiBegenenleriTakipEt)
                print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
                self.urlYonlendir(url)

            hedefBegenenSayisi = None

            if secilenIslem is None:
                for secenek in self.configGetir(base_warnings + "warning2"):
                    self.uyariOlustur(secenek,3)
                secilenIslem = str(input(self.configGetir(base_inputs+"input2")).strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 1)
            elif secilenIslem == "2":
                self.uyariOlustur(self.configGetir(base_warnings+"warning4"), 1)
                hedefBegenenSayisi = input(self.configGetir(base_inputs+"input3")).strip()
                self.anaMenuyeDonsunMu(hedefBegenenSayisi)
                if hedefBegenenSayisi.isnumeric():
                    hedefBegenenSayisi = int(hedefBegenenSayisi)
                else:
                    self.uyariOlustur(self.configGetir(base_warnings+"warning5"), 2)
                    print("")
                    self.gonderiBegenenleriTakipEt(url=url,secilenIslem=secilenIslem)
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning6"), 2)
                print("")
                self.gonderiBegenenleriTakipEt(url=url,secilenIslem=None)

            if not self.hesapGizliMi():
                if not self.gonderiTipiVideoMu():
                    print(str(self.configGetir(base_warnings+"warning7")).format(url=url))
                    devamEtsinMi = True
                    self.indexSifirla()


                    if hedefBegenenSayisi is None:
                        begenenSayisi = self.driver.find_element_by_css_selector(
                            "div.Nm9Fw > button.sqdOP > span").text
                        begenenSayisi = int(self.metindenKarakterSil(begenenSayisi, ','))
                    else:
                        kaynakBegenenSayisi = self.driver.find_element_by_css_selector(
                            "div.Nm9Fw > button.sqdOP > span").text
                        kaynakBegenenSayisi = int(self.metindenKarakterSil(kaynakBegenenSayisi, ','))
                        begenenSayisi = int(self.hedefKaynaktanBuyukMu(hedefBegenenSayisi, kaynakBegenenSayisi))

                    btn_begenenler = self.driver.find_element_by_css_selector("div.Nm9Fw > button.sqdOP")
                    btn_begenenler.click()
                    sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
                    kontrolEdilenKullanicilar=set()
                    while devamEtsinMi:
                        dialog_popup = self.driver.find_element_by_css_selector("div.pbNvD")
                        begenenlerKullanicilar = dialog_popup.find_elements_by_css_selector('div.HVWg4')
                        for begenenKullanici in begenenlerKullanicilar:
                            begenenKullaniciAdi = begenenKullanici.find_element_by_css_selector(
                                "div.Igw0E > div.Igw0E > div._7UhW9  a").get_attribute('href')
                            begenenKullaniciAdi = begenenKullaniciAdi.replace(self.BASE_URL, '').replace('/', '')
                            btn_takip = begenenKullanici.find_element_by_css_selector("div.Igw0E > button.sqdOP")
                            if btn_takip.text == "Follow":
                                print(str(self.configGetir(base_warnings+"warning8")).format(
                                    index=self.index, kullanici=begenenKullaniciAdi))
                                btn_takip.click()
                                self.indexArtir()
                                if self.index-1 >= begenenSayisi:
                                    devamEtsinMi = False
                                    break
                                sleep2=self.configGetir("{base}sleep2".format(base=base_sleep))
                                sleep(self.beklemeSuresiGetir(sleep2[0],sleep2[1]))

                            kontrolEdilenKullanicilar.add(begenenKullaniciAdi)

                            if hedefBegenenSayisi:
                                if len(kontrolEdilenKullanicilar) >= kaynakBegenenSayisi:
                                    devamEtsinMi = False
                                    break
                            else:
                                if len(kontrolEdilenKullanicilar) >= begenenSayisi:
                                    devamEtsinMi = False
                                    break
                        if devamEtsinMi:
                            self.popupAsagiKaydir(secici='div[role="dialog"]  .i0EQd > div:nth-child(1)')
                            sleep(self.configGetir("{base}sleep3".format(base=base_sleep)))
                        else:
                            print(self.configGetir(base_warnings+"warning9"))
                else:
                    print(str(self.configGetir(base_warnings+"warning10")).format(
                        url=url))
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning11")).format(url=url),
                                  2)
            self.gonderiBegenenleriTakipEt()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning12")).format(hata=str(error)), 2)
            self.gonderiBegenenleriTakipEt()

    def etiketeGoreTakipEtme(self):
        base_warnings = self.BASE_UYARI(metod=self.etiketeGoreTakipEtme, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.etiketeGoreTakipEtme)
        try:
            etiket = self.etiketGetir()

            limit = self.etiketeGoreIslemLimitiGetir(2)

            kaynakGonderiSayisi = int(
                self.metindenKarakterSil(self.driver.find_element_by_css_selector("span.g47SY").text, ','))
            limit = self.hedefKaynaktanBuyukMu(limit, kaynakGonderiSayisi)
            self.ilkGonderiTikla()
            sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
            self.indexSifirla()

            print(str(self.configGetir(base_warnings+"warning1")).format(etiket=etiket))
            while True:
                kullaniciAdi =self.driver.find_element_by_css_selector("div.e1e1d a.sqdOP").text
                btn_takip = self.driver.find_element_by_css_selector("div.bY2yH >button.sqdOP")
                if btn_takip.text != "Following":
                    btn_takip.click()
                    self.uyariOlustur(
                        str(self.configGetir(base_warnings+"warning2")).format(index=self.index,
                                                                               kullanici=kullaniciAdi), 1)
                    self.indexArtir()
                    if self.index-1 >= limit:
                        break
                    sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
                    self.gonderiIlerlet()
                    sleep3=self.configGetir("{base}sleep3".format(base=base_sleep))
                    sleep(self.beklemeSuresiGetir(sleep3[0],sleep3[1]))
                else:
                    print(str(self.configGetir(base_warnings+"warning3")).format(kullanici=kullaniciAdi))
                    self.gonderiIlerlet()
                    sleep(self.configGetir("{base}sleep4".format(base=base_sleep)))
            print(str(self.configGetir(base_warnings+"warning4")).format(etiket=etiket))
            self.etiketeGoreTakipEtme()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.etiketeGoreTakipEtme()

    def etiketeGoreBegenme(self):
        base_warnings = self.BASE_UYARI(metod=self.etiketeGoreBegenme, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.etiketeGoreBegenme)
        try:
            etiket = self.etiketGetir()
            limit = self.etiketeGoreIslemLimitiGetir(1)
            kaynakGonderiSayisi = int(
                self.metindenKarakterSil(self.driver.find_element_by_css_selector("span.g47SY").text, ','))
            limit = self.hedefKaynaktanBuyukMu(limit, kaynakGonderiSayisi)
            self.ilkGonderiTikla()
            sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
            self.indexSifirla()

            print(str(self.configGetir(base_warnings+"warning1")).format(etiket=etiket))
            while True:
                btn_begen = self.begenButon()
                begeniDurum = self.begenButonuDurumGetir(btn_begen)
                if begeniDurum != "unlike":
                    btn_begen.click()
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(index=self.index,url=self.driver.current_url),1)
                    self.indexArtir()
                    if self.index-1 >= limit:
                        break
                    sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
                    self.gonderiIlerlet()
                    sleep3=self.configGetir("{base}sleep3".format(base=base_sleep))
                    sleep(self.beklemeSuresiGetir(sleep3[0],sleep3[1]))
                else:
                    print(str(self.configGetir(base_warnings+"warning3")).format(url=self.driver.current_url))
                    self.gonderiIlerlet()
                    sleep(self.configGetir("{base}sleep4".format(base=base_sleep)))
            print(str(self.configGetir(base_warnings+"warning4")).format(etiket=etiket))
            self.etiketeGoreBegenme()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.etiketeGoreBegenme()

    def gonderiBegen(self, durum=True):
        base_warnings = self.BASE_UYARI(metod=self.gonderiBegen, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.gonderiBegen, inputs=True)

        try:
            if durum:
                url = input(self.configGetir(base_inputs+"input1")).strip()
            else:
                url = input(self.configGetir(base_inputs+"input2")).strip()

            self.anaMenuyeDonsunMu(url)
            self.urlGirildiMi(url=url, metod=self.gonderiBegen,metodDeger=durum)
            self.urlGecerliMi(url=url,metod=self.gonderiBegen,metodDeger=durum)
            print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
            self.urlYonlendir(url)
            if not self.hesapGizliMi():
                if durum:
                    print(str(self.configGetir(base_warnings+"warning2")).format(url=url))
                else:
                    print(str(self.configGetir(base_warnings+"warning3")).format(url=url))
                btn_begen = self.begenButon()
                begeniDurum = self.begenButonuDurumGetir(btn_begen)
                if durum:
                    if begeniDurum == "like":
                        btn_begen.click()
                        print(
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(url=self.driver.current_url),
                                              1))
                    else:
                        print(str(self.configGetir(base_warnings+"warning5")).format(url=self.driver.current_url))
                else:
                    if begeniDurum == "unlike":
                        btn_begen.click()
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(url=self.driver.current_url), 1)
                    else:
                        print(str(self.configGetir(base_warnings + "warning7")).format(url=self.driver.current_url))
                if durum:
                    print(str(self.configGetir(base_warnings+"warning8")).format(url=url))
                else:
                    print(str(self.configGetir(base_warnings+"warning9")).format(url=url))
            else:
                if durum:
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning10")).format(
                        url=url), 2)
                else:
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning11")).format(
                        url=url), 2)
            self.gonderiBegen(durum)
        except Exception as error:
            if durum:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning12")).format(hata=error),2)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning13")).format(hata=error), 2)
            self.gonderiBegen(durum)

    def gonderiYorumYapma(self, url=None, yorum=None):
        base_warnings = self.BASE_UYARI(metod=self.gonderiYorumYapma, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.gonderiYorumYapma, inputs=True)
        try:

            if url is None:
                url = input(self.configGetir(base_inputs+"input1")).strip()
                self.anaMenuyeDonsunMu(url)
            if not yorum:
                yorum = input(self.configGetir(base_inputs+"input2")).strip()
                self.anaMenuyeDonsunMu(yorum)


            self.urlGirildiMi(url=url,metod=self.gonderiYorumYapma,metodDeger=yorum)
            self.urlGecerliMi(url=url,metod=self.gonderiYorumYapma,metodDeger=yorum)


            if not self.degerVarMi(yorum):
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
                self.gonderiYorumYapma(url=url, yorum=None)

            print(str(self.configGetir(base_warnings+"warning2")).format(url=url))
            self.urlYonlendir(url)

            if not self.sayfaMevcutMu():
                self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 2)
                self.gonderiYorumYapma()

            if not self.hesapGizliMi():
                yorum = yorum[0:250]
                print(str(self.configGetir(base_warnings+"warning4")).format(url=url))
                self.yorumYap(yorum)
                print(str(self.configGetir(base_warnings+"warning5")).format(url=url))
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(url=url), 2)
            self.gonderiYorumYapma()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning7")).format(url=url,hata=str(error)),
                              2)
            self.gonderiYorumYapma()

    def kullaniciTakipEt(self, kullanici, secim,durum=True):
        base_warnings = self.BASE_UYARI(metod=self.kullaniciTakipEt, warnings=True)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if durum:
                print(str(self.configGetir(base_warnings+"warning1")).format(kullanici=kullanici))
            else:
                print(str(self.configGetir(base_warnings+"warning2")).format(kullanici=kullanici))


            self.kullaniciTakipDurumDegistir(kullanici=kullanici,durum=durum)
            if durum:
                print(str(self.configGetir(base_warnings+"warning3")).format(kullanici=kullanici))
            else:
                print(str(self.configGetir(base_warnings+"warning4")).format(kullanici=kullanici))
            if secim != 13:
                self.profilSec(secim)
        except Exception as error:
            if durum:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(kullanici=kullanici,hata=str(error)),2)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(kullanici=kullanici,
                                                                                         hata=str(error)), 2)
            if secim != 13:
                self.profilSec(secim)

    def kullaniciEngelle(self, kullanici, secim,durum=True):
        base_warnings = self.BASE_UYARI(metod=self.kullaniciEngelle, warnings=True)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if durum:
                print(str(self.configGetir(base_warnings+"warning1")).format(kullanici=kullanici))
            else:
                print(str(self.configGetir(base_warnings+"warning2")).format(kullanici=kullanici))

            if self.hesapGizliMi():
                btnText = str(self.driver.find_element_by_css_selector('div.BY3EC >button').text).lower()
                if durum:
                    if btnText!="unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(kullanici=kullanici), 2)
                else:
                    if btnText=="unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(kullanici=kullanici), 2)
            else:
                btnText =str(self.driver.find_element_by_css_selector('span.vBF20 > button._5f5mN').text).lower()
                if durum:
                    if btnText != "unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(kullanici=kullanici), 2)
                else:
                    if btnText == "unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(kullanici=kullanici), 2)

            if durum:
                print(str(self.configGetir(base_warnings+"warning7")).format(kullanici=kullanici))
            else:
                print(str(self.configGetir(base_warnings+"warning8")).format(kullanici=kullanici))
            self.profilSec(secim)
        except Exception as error:
            if durum:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning9")).format(kullanici=kullanici,hata=str(error)),2)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning10")).format(kullanici=kullanici,hata=str(error)), 2)
            self.profilSec(secim)

    def ayarlar(self,durum=True):
        base_warnings = self.BASE_UYARI(metod=self.ayarlar, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.ayarlar,inputs=True)
        try:
            if durum:
                ayarlar=self.configGetir("{base}ana_ekran.secenekler".format(base=self.BASE_AYARLAR()))
                for secenek in ayarlar:
                    self.uyariOlustur(secenek,3)
            secilenIslem=input(self.configGetir(base_inputs+"input1"))

            if secilenIslem=="1":
                self.dilAyarlari()
            elif secilenIslem=="2":
                self.tarayiciAyarlari()
            elif secilenIslem=="3":
                self.menu()
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
                self.ayarlar(durum=False)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)),2)

    def oturumKapat(self):
        base_warnings = self.BASE_UYARI(metod=self.oturumKapat, warnings=True)
        print(self.configGetir(base_warnings+"warning1"))
        try:
            self.driver.find_elements_by_css_selector("div._47KiJ > div.Fifk5")[-1].click()
            sleep(0.10)
            self.driver.find_elements_by_css_selector("div.-qQT3")[-1].click()
            self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 1)
            self.driver.get(self.BASE_URL + 'accounts/login/')
            self.girisYapildimi = False
            self.girisYap()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(hata=str(error)), 2)
            self.menu()

    def quit(self):
        base_warnings = self.BASE_UYARI(metod=self.quit, warnings=True)
        try:
            print(self.configGetir(base_warnings+"warning1"))
            self.driver.quit()
            self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 1)
            exit()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(hata=str(error)), 2)
            self.driver.quit()
            exit()

    def ayarlarYukle(self):
        if self.dosyaMevcutMu("config.json"):
            with open('config.json', 'r+', encoding="utf-8") as dosya:
                self.config = json.load(dosya)
        else:
            self.uyariOlustur("Config file is missing - Config dosyası eksik !",2)
            exit()

    def configGetir(self,anahtar):
        deger=self.config
        for key in anahtar.split('.'):
            deger = deger[key]
        return deger

    def dilYukle(self):
        self.dil=self.configGetir("language")

    def dilGetir(self):
        if self.dil=="tr":
            return "Türkçe"
        else:
            return "English"

    def dilAyarlari(self,durum=True):
        base_warnings = self.BASE_UYARI(metod=self.dilAyarlari, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.dilAyarlari,inputs=True)
        try:
            if durum:
                ayarlar=self.configGetir("{base}dil_ayarlari.secenekler".format(base=self.BASE_AYARLAR()))
                for secenek in ayarlar:
                    if "{dil}" in secenek:
                        self.uyariOlustur(str(secenek).format(dil=self.dilGetir()),3)
                    else:
                        self.uyariOlustur(secenek, 3)
            secilenIslem=input(self.configGetir(base_inputs+"input1"))

            if secilenIslem=="1":
                self.dilSec()
            elif secilenIslem=="2":
                self.ayarlar()
            elif secilenIslem=="3":
                self.menu()
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"),2)
                self.dilAyarlari(durum=False)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)),2)

    def tarayiciAyarlari(self,durum=True):
        base_warnings = self.BASE_UYARI(metod=self.tarayiciAyarlari, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.tarayiciAyarlari,inputs=True)
        try:
            if durum:
                ayarlar=self.configGetir("{base}tarayici_ayarlari.secenekler".format(base=self.BASE_AYARLAR()))
                for secenek in ayarlar:
                    if "{path}" in secenek:
                        self.uyariOlustur(str(secenek).format(path=self.tarayiciPathGetir()),3)
                    elif "{durum}" in secenek:
                        self.uyariOlustur(str(secenek).format(durum=self.tarayiciHeadlessGetir()), 3)
                    else:
                        self.uyariOlustur(secenek, 3)
            secilenIslem=input(self.configGetir(base_inputs+"input1"))

            if secilenIslem=="1":
                self.tarayiciGorunmeDurumuAyarlari()
            elif secilenIslem=="2":
                self.tarayiciPathAyarlari()
            elif secilenIslem=="3":
                self.ayarlar()
            elif secilenIslem=="4":
                self.menu()
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"),2)
                self.tarayiciAyarlari(durum=False)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning2")).format(hata=str(error)), 2)

    def tarayiciHeadlessGetir(self):
        headless=self.configGetir("headless")
        durum=None
        if headless=="true":
            if self.dil=="tr":
                durum= "Açık"
            elif self.dil=="en":
                durum= "Open"
        else:
            if self.dil == "tr":
                durum= "Kapalı"
            elif self.dil == "en":
                durum= "Close"
        return durum

    def dilSec(self,durum=True):
        base_warnings = self.BASE_UYARI(metod=self.dilSec, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.dilSec,inputs=True)
        try:
            if durum:
                ayarlar=self.configGetir("{base}dil_ayarlari.dil_degistir.secenekler".format(base=self.BASE_AYARLAR()))
                for secenek in ayarlar:
                    self.uyariOlustur(secenek,3)
            secilenIslem=input(self.configGetir(base_inputs+"input1"))

            if secilenIslem in ["1","2"]:
                self.uygulamaDilDegistir(dilNo=secilenIslem)
                self.ayarlar()
            elif secilenIslem=="3":
                self.dilAyarlari()
            elif secilenIslem=="4":
                self.ayarlar()
            elif secilenIslem=="5":
                self.menu()
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"),2)
                self.dilSec(durum=False)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning2")).format(hata=str(error)), 2)

    def uygulamaDilDegistir(self,dilNo):
        base_warnings = self.BASE_UYARI(metod=self.uygulamaDilDegistir, warnings=True)
        try:
            if dilNo=="1":
                dil="tr"
            elif dilNo=="2":
                dil="en"
            with open('config.json', 'r+', encoding="utf-8") as dosya:
                veri = json.load(dosya)
                veri["language"]=dil
                dosya.seek(0)
                json.dump(veri, dosya, indent=4,ensure_ascii=False)
                dosya.truncate()
            self.uyariOlustur(self.configGetir(base_warnings+"warning1"),1)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)), 2)

    def tarayiciThreadOlustur(self):
        t1 = threading.Thread(target=self.tarayiciBaslat)
        t1.daemon = True
        t1.start()


    def tarayiciBaslat(self):
        base_warnings = self.BASE_UYARI(metod=self.tarayiciBaslat, warnings=True)
        try:
            print(self.configGetir(base_warnings+"warning1"))
            firefox_options = Options()
            headless=self.configGetir("headless")
            if headless=="false":
                firefox_options.add_argument('--headless')
            self.driver = webdriver.Firefox(firefox_profile=self.tarayiciDilDegistir(),options=firefox_options,executable_path=self.tarayiciPathGetir())
            self.driver.get(self.BASE_URL + 'accounts/login/')
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)),2)
            exit()

    def tarayiciPathGetir(self):
        return self.configGetir("driver_path")

    def tarayiciDilDegistir(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'en-US, en')
        return profile

    def tarayiciPathAyarlari(self,durum=True):
        base_warnings = self.BASE_UYARI(metod=self.tarayiciPathAyarlari, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.tarayiciPathAyarlari,inputs=True)
        try:
            if durum:
                ayarlar=self.configGetir(self.BASE_AYARLAR()+"tarayici_ayarlari.path_degistir.secenekler")
                for secenek in ayarlar:
                    self.uyariOlustur(secenek,3)
            secilenIslem = input(self.configGetir(base_inputs+"input1"))
            if secilenIslem=="1":
                self.tarayiciPathDegistir()
                self.ayarlar()
            elif secilenIslem=="2":
                self.tarayiciAyarlari()
            elif secilenIslem=="3":
                self.ayarlar()
            elif secilenIslem=="4":
                self.menu()
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"),2)
                self.tarayiciPathAyarlari(durum=False)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)), 2)

    def tarayiciPathDegistir(self):
        base_warnings = self.BASE_UYARI(metod=self.tarayiciPathDegistir, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.tarayiciPathDegistir,inputs=True)
        try:
            path = input(self.configGetir(base_inputs+"input1"))
            if self.dosyaMevcutMu(path):
                with open('config.json', 'r+', encoding="utf-8") as dosya:
                    veri = json.load(dosya)
                    veri["driver_path"]=path
                    dosya.seek(0)
                    json.dump(veri, dosya, indent=4,ensure_ascii=False)
                    dosya.truncate()
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"),1)
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
                self.tarayiciPathAyarlari()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(hata=str(error)), 2)

    def tarayiciGorunmeDurumuAyarlari(self,durum=True):
        base_warnings = self.BASE_UYARI(metod=self.tarayiciGorunmeDurumuAyarlari, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.tarayiciGorunmeDurumuAyarlari, inputs=True)
        try:
            if durum:
                ayarlar=self.configGetir("{base}tarayici_ayarlari.gorunme_durumu_degistir.secenekler".format(base=self.BASE_AYARLAR()))
                for secenek in ayarlar:
                    self.uyariOlustur(secenek,3)
            secilenIslem=input(self.configGetir(base_inputs+"input1"))
            if secilenIslem in ["1","2"]:
                self.tarayiciGorunmeDurumDegistir(durum=secilenIslem)
                self.ayarlar()
            elif secilenIslem=="3":
                self.tarayiciAyarlari()
            elif secilenIslem=="4":
                self.ayarlar()
            elif secilenIslem=="5":
                self.menu()
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"),2)
                self.tarayiciGorunmeDurumuAyarlari(durum=False)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning2")).format(hata=str(error)), 2)

    def tarayiciGorunmeDurumDegistir(self,durum):
        base_warnings = self.BASE_UYARI(metod=self.tarayiciGorunmeDurumDegistir, warnings=True)
        try:
            if durum=="1":
                headless="true"
            elif durum=="2":
                headless="false"
            with open('config.json', 'r+', encoding="utf-8") as dosya:
                veri = json.load(dosya)
                veri["headless"]=headless
                dosya.seek(0)
                json.dump(veri, dosya, indent=4,ensure_ascii=False)
                dosya.truncate()
            self.uyariOlustur(self.configGetir(base_warnings+"warning1"),1)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)), 2)


    def takipcilerButon(self):
        return self.driver.find_elements_by_css_selector("ul.k9GMp >li.Y8-fY")[1]

    def takipEdilenlerButon(self):
        return self.driver.find_elements_by_css_selector("ul.k9GMp >li.Y8-fY")[2]

    def takipcileriGetir(self):
        base_warnings = self.BASE_UYARI(metod=self.takipcileriGetir, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.takipcileriGetir)
        try:
            print(self.configGetir(base_warnings + "warning1"))
            self.kullaniciProfilineYonlendir(self.aktifKullanici)
            takipciSayisi = self.takipciSayisiGetir()

            btn_takipciler = self.takipcilerButon()
            btn_takipciler.click()
            sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
            takipciler = set()
            self.indexSifirla()
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipcilerPopup = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takipci in takipcilerPopup:
                    takipciKullaniciAdi = takipci.find_element_by_css_selector("a.FPmhX").get_attribute('href')
                    takipciKullaniciAdi = self.metindenKarakterSil(
                        self.metindenKarakterSil(takipciKullaniciAdi, self.BASE_URL), '/')
                    if takipciKullaniciAdi not in takipciler:
                        print(str(self.configGetir(base_warnings + "warning2")).format(index=self.index,kullanici=takipciKullaniciAdi))
                        takipciler.add(takipciKullaniciAdi)
                        self.indexArtir()
                        if (self.index - 1) >= takipciSayisi:
                            devamEtsinMi = False
                            break
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        self.uyariOlustur(str(self.configGetir(base_warnings + "warning3")).format(
                            hata=str(error)), 2)
                        pass
                    sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
            btn_close_dialog = self.driver.find_element_by_css_selector("div.WaOAr >button.wpO6b")
            btn_close_dialog.click()
            return takipciler
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning4")).format(hata=str(error)), 2)
            self.menu()

    def takipEdilenleriGetir(self, takipciler):
        base_warnings = self.BASE_UYARI(metod=self.takipEdilenleriGetir, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.takipEdilenleriGetir)
        try:
            takipEdilenSayisi = self.takipEdilenSayisiGetir()
            btn_takipEdilenler = self.takipEdilenlerButon()
            btn_takipEdilenler.click()
            sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
            self.indexSifirla()
            islemIndex = 0
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takip in takipListe:
                    takipEdilenKullanıcıAdi = self.takipEdilenKullaniciAdiGetir(element=takip)

                    if takipEdilenKullanıcıAdi not in takipciler:
                        btn_takip = takip.find_element_by_css_selector('button.sqdOP')
                        if btn_takip.text == "Following":
                            btn_takip.click()
                            sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
                            try:
                                btn_onay = self.driver.find_element_by_css_selector("div.mt3GC > button.aOOlW")
                                btn_onay.click()
                            except Exception as error:
                                self.uyariOlustur(str(self.configGetir(base_warnings + "warning1")).format(
                                    kullanici=takipEdilenKullanıcıAdi, hata=str(error)), 2)
                                continue
                            self.uyariOlustur(str(self.configGetir(base_warnings + "warning2")).format(
                                index=self.index, kullanici=takipEdilenKullanıcıAdi), 1)
                            self.indexArtir()
                            if self.index - 1 >= takipEdilenSayisi:
                                devamEtsinMi = False
                                break
                            sleep3 = self.configGetir("{base}sleep3".format(base=base_sleep))
                            sleep(self.beklemeSuresiGetir(sleep3[0], sleep3[1]))
                    islemIndex = islemIndex + 1
                    if islemIndex >= takipEdilenSayisi:
                        devamEtsinMi = False
                        break
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        self.uyariOlustur(str(self.configGetir(base_warnings + "warning3")).format(
                            hata=str(error)), 2)
                        pass
                    sleep(self.configGetir("{base}sleep4".format(base=base_sleep)))

        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning4")).format(
                hata=str(error)), 2)
            self.menu()

    def takipEdilenSayisiGetir(self):
        takipEdilenSayisi = self.driver.find_elements_by_css_selector("ul.k9GMp li.Y8-fY >a.-nal3 >span.g47SY")[-1].text
        return int(self.metindenKarakterSil(takipEdilenSayisi, ','))

    def takipciSayisiGetir(self):
        takipciSayisi = self.driver.find_elements_by_css_selector("ul.k9GMp li.Y8-fY >a.-nal3 >span.g47SY")[0].get_attribute('title')
        return int(self.metindenKarakterSil(takipciSayisi, ','))

    def takipEdilenKullaniciAdiGetir(self, element):
        takipEdilenKullanıcıAdi = element.find_element_by_css_selector("a.FPmhX").get_attribute('href')
        return self.metindenKarakterSil(self.metindenKarakterSil(takipEdilenKullanıcıAdi, self.BASE_URL), '/')

    def girisYap(self, username=False, password=False):
        base_warnings = self.BASE_UYARI(metod=self.girisYap, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.girisYap, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.girisYap)

        try:
            if not username and not password:
                print(" ")
                print(" ")
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 1)
                username = input(self.configGetir(base_inputs+"input1"))
                password = getpass.getpass(prompt=self.configGetir(base_inputs+"input2"))
            elif not username:
                username = input(self.configGetir(base_inputs+"input1"))
            elif not password:
                password = getpass.getpass(prompt=self.configGetir(base_inputs+"input2"))

            if not username and not password:
                self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
                self.girisYap()
            elif not username:
                self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 2)
                self.girisYap(False, password)
            elif not password:
                self.uyariOlustur(self.configGetir(base_warnings+"warning4"), 2)
                self.girisYap(username, False)

            print(self.configGetir(base_warnings+"warning5"))
            sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
            usernameInput = self.driver.find_elements_by_css_selector('form input')[0]
            passwordInput = self.driver.find_elements_by_css_selector('form input')[1]
            usernameInput.send_keys(username.strip())
            passwordInput.send_keys(password.strip())
            passwordInput.send_keys(Keys.ENTER)
            sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
            self.girisKontrol()
            if self.girisYapildimi:
                self.bildirimThreadOlustur()
                self.menu()
            else:
                self.inputTemizle(usernameInput)
                self.inputTemizle(passwordInput)
                self.girisYap()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(hata=str(error)), 2)

    def girisKontrol(self):
        base_warnings = self.BASE_UYARI(metod=self.girisKontrol, warnings=True)
        if "The username you entered doesn't belong to an account. Please check your username and try again." in self.driver.page_source:
            self.uyariOlustur(self.configGetir(base_warnings+"warning1"),2)
        elif "Sorry, your password was incorrect. Please double-check your password." in self.driver.page_source:
            self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
        elif self.BASE_URL + "accounts/login/two_factor" in self.driver.current_url:
            self.girisDogrulama()
        elif self.driver.current_url != self.BASE_URL + "accounts/login/":
            self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 1)
            self.girisYapildimi = True
        else:
            self.uyariOlustur(self.configGetir(base_warnings+"warning4"), 2)

    def girisDogrulama(self, durum=True):
        base_warnings = self.BASE_UYARI(metod=self.girisDogrulama, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.girisDogrulama, inputs=True)
        base_sleep = self.BASE_SLEEP(metod=self.girisDogrulama)

        kod = input(self.configGetir(base_inputs+"input1")).strip()
        if not kod:
            self.girisYap(durum)

        if durum:
            sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
        kodInput = self.driver.find_elements_by_css_selector('form input')[0]
        kodInput.send_keys(kod)
        kodInput.send_keys(Keys.ENTER)
        sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
        if "A security code is required." in self.driver.page_source:
            self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
            self.inputTemizle(kodInput)
            self.girisDogrulama(False)
        elif "Please check the security code and try again." in self.driver.page_source:
            self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
            self.inputTemizle(kodInput)
            self.girisDogrulama(False)
        elif self.BASE_URL + "accounts/login/two_factor" not in self.driver.current_url:
            self.girisYapildimi = True
            self.uyariOlustur(self.configGetir(base_warnings+"warning3"),1)
        else:
            self.uyariOlustur(self.configGetir(base_warnings+"warning4"),2)

    def etiketGetir(self):
        base_warnings = self.BASE_UYARI(metod=self.etiketGetir, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.etiketGetir, inputs=True)
        try:
            etiket = input(self.configGetir(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(etiket)

            if self.degerVarMi(etiket):
                url = "{BASE_URL}explore/tags/{etiket}".format(BASE_URL=self.BASE_URL, etiket=str(etiket))
                print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
                self.urlYonlendir(url)
                if not self.sayfaMevcutMu():
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(etiket=etiket),
                                      2)
                    return self.etiketGetir()
                return etiket
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 2)
                return self.etiketGetir()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(hata=str(error)), 2)

    def etiketeGoreIslemLimitiGetir(self, islemNo):
        base_warnings = self.BASE_UYARI(metod=self.etiketeGoreIslemLimitiGetir, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.etiketeGoreIslemLimitiGetir, inputs=True)
        try:
            if islemNo == 1:
                limit = input(self.configGetir(base_inputs+"input1")).strip()
            elif islemNo == 2:
                limit = input(self.configGetir(base_inputs+"input2")).strip()

            self.anaMenuyeDonsunMu(limit)
            if limit.isnumeric() and int(limit) > 0:
                return int(limit)
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
                return self.etiketeGoreIslemLimitiGetir(islemNo=islemNo)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)), 2)
            if islemNo == 1:
                self.etiketeGoreBegenme()
            elif islemNo == 2:
                self.etiketeGoreTakipEtme()

    def hikayeVarMi(self):
        try:
            durum = self.driver.find_element_by_css_selector("div.RR-M-").get_attribute("aria-disabled")
            if durum == "false":
                return True
            else:
                return False
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.hikayeVarMi, warnings=True)
            self.uyariOlustur(
                str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)),
                2)

    def hikayeVideoMu(self):
        try:
            self.driver.find_element_by_css_selector("div.qbCDp > video.y-yJ5")
            return True
        except:
            return False

    def hikayeSayisiGetir(self):
        try:
            hikayeSayisi = self.driver.find_elements_by_css_selector("div.w9Vr-  > div._7zQEa")
            return len(hikayeSayisi)
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.hikayeSayisiGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)

    def hikayeleriGetir(self):
        base_sleep = self.BASE_SLEEP(metod=self.hikayeleriGetir)

        try:
            for i in range(self.hikayeSayisiGetir()):
                if self.hikayeVideoMu():
                    url = self.driver.find_element_by_css_selector("div.qbCDp > video.y-yJ5 > source").get_attribute(
                        "src")
                    self.dosyaIndir(url, 2)
                else:
                    foto_srcset = str(
                        self.driver.find_element_by_css_selector("div.qbCDp >  img.y-yJ5").get_attribute("srcset"))
                    url = (foto_srcset.split(",")[-1]).split(" ")[0]
                    self.dosyaIndir(url, 1)
                btn_ileri = self.driver.find_element_by_css_selector("button.ow3u_")
                btn_ileri.click()
                sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.hikayeleriGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)

    def yorumUzunlukBelirle(self, yorum):
        return yorum[0:randint(5, 100)]

    def yorumYap(self, yorum):
        try:

            textarea = self.driver.find_element_by_class_name('Ypffh')
            self.inputTemizle(textarea)
            textarea.click()
            textarea = self.driver.find_element_by_class_name('Ypffh')

            textarea.send_keys(yorum)
            textarea.send_keys(Keys.ENTER)
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.yorumYap, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning1")).format(hata=str(error)), 2)

    def rastgeleYorumGetir(self):
        try:
            return requests.get("http://metaphorpsum.com/paragraphs/1/1").text
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.rastgeleYorumGetir, warnings=True)
            self.uyariOlustur(
                str(self.configGetir(base_warnings + "warning1")).format(hata=str(error)), 2)

    def yorumLimitiAsildiMi(self, yorumSayisi):
        if yorumSayisi > 50:
            return True
        else:
            return False

    def mesajSil(self,mesaj):
        mesaj.click()
        base = self.BASE_SLEEP(metod=self.mesajSil)
        sleep1=self.configGetir(base + "sleep1")
        sleep(self.beklemeSuresiGetir(sleep1[0],sleep1[1]))
        self.driver.find_element_by_css_selector("div.PjuAP button.wpO6b").click()
        sleep(self.configGetir(base + "sleep2"))
        self.driver.find_elements_by_css_selector("div._9XapR >div._7zBYT button.sqdOP")[0].click()
        sleep(self.configGetir(base + "sleep3"))
        self.driver.find_elements_by_css_selector("div.mt3GC >button.aOOlW")[0].click()

    def kullaniciEngelDurumDegistir(self):
        base_sleep = self.BASE_SLEEP(metod=self.kullaniciEngelDurumDegistir)
        self.driver.find_element_by_css_selector("button.wpO6b").click()
        sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
        self.driver.find_elements_by_css_selector("div.mt3GC > button.aOOlW")[0].click()
        sleep(self.configGetir("{base}sleep2".format(base=base_sleep)))
        self.driver.find_elements_by_css_selector("div.mt3GC > button.aOOlW")[0].click()

    def kullaniciTakipDurumDegistir(self,kullanici,durum):
        base_warnings = self.BASE_UYARI(metod=self.kullaniciTakipDurumDegistir, warnings=True)
        base_sleep = self.BASE_SLEEP(metod=self.kullaniciTakipDurumDegistir)

        if self.hesapGizliMi():
            btn_takip = self.driver.find_element_by_css_selector("div.BY3EC >button")
            btn_text = str(btn_takip.text).lower()
            if durum:
                if btn_text in ["follow","follow back"]:
                    btn_takip.click()
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(kullanici=kullanici), 1)
                elif btn_text == "requested":
                    print(str(self.configGetir(base_warnings+"warning2")).format(kullanici=kullanici))
                elif btn_text == "unblock":
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(
                        kullanici=kullanici), 2)
            else:
                if btn_text=="requested":
                    btn_takip.click()
                    sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
                    self.driver.find_elements_by_css_selector("div.mt3GC >button.aOOlW")[0].click()
                    self.uyariOlustur(str(self.configGetir(base_warnings + "warning8")).format(kullanici=kullanici), 1)
                else:
                    print(str(self.configGetir(base_warnings+"warning4")).format(kullanici=kullanici))

        else:
            btn_takip = self.driver.find_element_by_css_selector('span.vBF20 > button._5f5mN')
            btn_text = str(btn_takip.text).lower()
            if durum:
                if btn_text in ["follow","follow back"]:
                    btn_takip.click()
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(kullanici=kullanici), 1)
                elif btn_text == "unblock":
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(kullanici=kullanici), 2)
                else:
                    ariaLabel = btn_takip.find_element_by_tag_name("span").get_attribute("aria-label")
                    if ariaLabel == "Following":
                        print(str(self.configGetir(base_warnings+"warning7")).format(kullanici=kullanici))
            else:
                try:
                    ariaLabel = btn_takip.find_element_by_tag_name("span").get_attribute("aria-label")
                    if ariaLabel == "Following":
                        btn_takip.click()
                        sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
                        self.driver.find_elements_by_css_selector("div.mt3GC >button.aOOlW")[0].click()
                        self.uyariOlustur(str(self.configGetir(base_warnings + "warning8")).format(kullanici=kullanici),
                                          1)
                    else:
                        print(str(self.configGetir(base_warnings + "warning4")).format(kullanici=kullanici))
                except:
                    print(str(self.configGetir(base_warnings + "warning4")).format(kullanici=kullanici))


    def gonderiIlerlet(self):
        try:
            self.driver.find_element_by_css_selector("a._65Bje").click()
        except:
            pass

    def gonderiBegenDurumDegistir(self, btn):
        base_sleep = self.BASE_SLEEP(metod=self.gonderiBegenDurumDegistir)
        btn.click()
        self.indexArtir()
        sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
        self.gonderiIlerlet()
        sleep2=self.configGetir("{base}sleep2".format(base=base_sleep))
        sleep(self.beklemeSuresiGetir(sleep2[0],sleep2[1]))

    def begenButon(self):
        return self.driver.find_element_by_css_selector("article.M9sTE section.ltpMr >span.fr66n >button")

    def begenButonuDurumGetir(self, buton):
        return str(buton.find_element_by_tag_name("svg").get_attribute("aria-label")).lower()

    def gonderiVarMi(self, kullanici, gonderiSayisi, secim):
        if gonderiSayisi < 1:
            base_warnings = self.BASE_UYARI(metod=self.gonderiVarMi, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(kullanici=kullanici), 2)
            self.profilSec(secim)

    def gonderiSayisi(self):
        return self.driver.find_element_by_css_selector("ul.k9GMp >li.Y8-fY >span >span.g47SY").text

    def gonderiTipiVideoMu(self, element=None):
        try:
            if element:
                element.find_element_by_css_selector("video.tWeCl")
            else:
                self.driver.find_element_by_css_selector("video.tWeCl")
            return True
        except:
            return False

    def gonderiUrlGetir(self):
        try:
            veriTuru = None
            if self.gonderiTipiVideoMu():
                url = self.driver.find_element_by_css_selector("video.tWeCl").get_attribute("src")
                veriTuru = 2
            else:
                url = self.driver.find_element_by_css_selector("article.M9sTE div.KL4Bh > img.FFVAD").get_attribute("src")
                veriTuru = 1
            return url, veriTuru
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.gonderiUrlGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)
            return None, None

    def gonderiAlbumMu(self):
        try:
            self.driver.find_element_by_css_selector("div.Yi5aA")
            return True
        except:
            return False

    def albumUrlGetir(self):
        base_sleep = self.BASE_SLEEP(metod=self.albumUrlGetir)

        try:
            album = set()
            ul = self.driver.find_element_by_css_selector("article ul.vi798")
            for i in range(self.albumIcerikSayisiGetir()):
                liste = ul.find_elements_by_css_selector("li.Ckrof")
                for li in liste:
                    [url, veriTuru] = self.albumIcerikUrlGetir(li)
                    if url not in album and url is not None:
                        album.add(url)
                        self.dosyaIndir(url, veriTuru)
                btn_ileri = self.driver.find_element_by_css_selector("button._6CZji div.coreSpriteRightChevron")
                btn_ileri.click()
                sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
        except:
            pass

    def albumIcerikSayisiGetir(self):
        try:
            return len(self.driver.find_elements_by_css_selector("div.Yi5aA"))
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.albumIcerikUrlGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format( url=str(self.driver.current_url), hata=str(error)), 2)
            return None

    def albumIcerikUrlGetir(self, element):
        try:
            veriTuru = None
            if self.gonderiTipiVideoMu(element):
                url = element.find_element_by_css_selector("video.tWeCl").get_attribute("src")
                veriTuru = 2
            else:
                url = element.find_element_by_css_selector("img.FFVAD").get_attribute("src")
                veriTuru = 1
            return url, veriTuru
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.albumIcerikUrlGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)
            return None, None

    def aktifKullaniciGetir(self):
        try:
            self.driver.find_elements_by_css_selector("div._47KiJ > div.Fifk5")[-1].click()
            kullanici = self.driver.find_elements_by_css_selector("div._01UL2 >a.-qQT3")[0].get_attribute(
                "href")
            self.aktifKullanici = str(kullanici).replace(self.BASE_URL, "")
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.aktifKullaniciGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)
            self.aktifKullaniciGetir()

    def anaMenuyeDonsunMu(self, deger):
        if deger == "menu":
            self.menu()

    def BASE_AYARLAR(self):
        try:
            return "languages.{dil}.ayarlar.".format(dil=self.dil)
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.BASE_AYARLAR, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)),2)

    def BASE_SLEEP(self,metod):
        try:
            return "time.{metod}.".format(metod=metod.__name__)
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.BASE_SLEEP, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)),2)

    def BASE_UYARI(self, metod, warnings=None, inputs=None):
        try:
            if warnings:
                return "languages.{dil}.warnings.{metod}.warnings.".format(dil=self.dil, metod=metod.__name__)
            elif inputs:
                return "languages.{dil}.warnings.{metod}.inputs.".format(dil=self.dil, metod=metod.__name__)
            else:
                return "languages.{dil}.warnings.{metod}.".format(dil=self.dil, metod=metod.__name__)
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.BASE_UYARI, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings + "warning1")).format(hata=str(error)))

    def beklemeSuresiGetir(self, baslangic, bitis):
        return randint(baslangic, bitis)

    def bildirimThreadOlustur(self):
        t1 = threading.Thread(target=self.bildirimPopupKapat)
        t1.daemon = True
        t1.start()

    def bildirimPopupKapat(self):
        base_sleep = self.BASE_SLEEP(metod=self.bildirimPopupKapat)
        try:
            for i in range(2):
                sleep(self.configGetir("{base}sleep1".format(base=base_sleep)))
                btn = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
                if btn:
                    self.driver.execute_script("arguments[0].click();", btn)
                    self.aktifKullaniciGetir()
            self.aktifKullaniciGetir()

        except:
            pass

    def popupAsagiKaydir(self, secici):
        self.driver.execute_script('''
                                     var fDialog = document.querySelector('{secici}');
                                     fDialog.scrollTop = fDialog.scrollHeight
                                  '''.format(secici=secici))

    def hesapGizliMi(self):
        if "This Account is Private" in self.driver.page_source:
            return True
        else:
            return False

    def sayfaMevcutMu(self):
        if "Sorry, this page isn't available." not in self.driver.page_source:
            return True
        else:
            return False

    def kullanicilariTakipEt(self, kullaniciListesi, secim):
        base_sleep = self.BASE_SLEEP(metod=self.kullanicilariTakipEt)
        base_warnings = self.BASE_UYARI(metod=self.kullanicilariTakipEt, warnings=True)
        print(self.configGetir(base_warnings + "warning1"))
        sleep1 = self.configGetir("{base}sleep1".format(base=base_sleep))
        for kullanici in kullaniciListesi:
            if self.kullaniciKontrol(kullanici):
                self.kullaniciTakipEt(kullanici=kullanici.strip(),secim=secim)
                sleep(self.beklemeSuresiGetir(sleep1[0], sleep1[1]))
        print(self.configGetir(base_warnings + "warning2"))

    def kullaniciKontrol(self, kullanici):
        return self.urlKontrol(self.BASE_URL + kullanici)

    def kullaniciProfilineYonlendir(self, kullanici):
        self.driver.get(self.BASE_URL + kullanici)
        base = self.BASE_SLEEP(metod=self.kullaniciProfilineYonlendir)
        sleep(self.configGetir("{base}sleep1".format(base=base)))

    def urlGirildiMi(self, url, metod, metodDeger=None):
        base_warnings = self.BASE_UYARI(metod=self.urlGirildiMi, warnings=True)
        if url is None or len(url) < 12:
            self.uyariOlustur(self.configGetir(base_warnings + "warning1"), 2)
            if metodDeger:
                if "gonderiYorumYapma" == metod.__name__:
                    metod(yorum=metodDeger)
                metod(metodDeger)
            metod()

    def urlGecerliMi(self, url, metod, metodDeger=None):
        if not self.urlKontrol(url):
            base_warnings = self.BASE_UYARI(metod=self.urlGecerliMi, warnings=True)
            self.uyariOlustur(self.configGetir(base_warnings + "warning1"), 2)
            if metodDeger:
                if "gonderiYorumYapma" == metod.__name__:
                    metod(yorum=metodDeger)
                metod(metodDeger)
            metod()

    def urlKontrol(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 404:
                return False
            else:
                return True
        except:
            return False

    def urlYonlendir(self, url):
        self.driver.get(url)
        base = self.BASE_SLEEP(metod=self.urlYonlendir)
        sleep(self.configGetir("{base}sleep1".format(base=base)))

    def uyariOlustur(self, mesaj, durum):
        if durum == 1:
            uyari= colored(mesaj, "green")
        elif durum == 2:
            uyari=  colored(mesaj, "red")
        elif durum == 3:
            uyari=  colored(mesaj, "blue")
        print(uyari)

    def dosyaAdiOlustur(self,veriTuru):
        dt=str(datetime.now()).replace(":", "_").replace(" ", "")
        if veriTuru == 1:
            isim="{index}_{tarih}.jpg".format(index=str(self.index),tarih=dt)
        elif veriTuru == 2:
            isim = "{index}_{tarih}.mp4".format(index=str(self.index), tarih=dt)
        return isim

    def dosyaIndir(self, url, veriTuru):
        base_warnings = self.BASE_UYARI(metod=self.dosyaIndir, warnings=True)
        try:
            dosyaAdi=self.dosyaAdiOlustur(veriTuru)
            urllib.request.urlretrieve(url, dosyaAdi)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(url=url), 1)
            self.indexArtir()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)), 2)

    def dosyaSec(self):
        base_warnings = self.BASE_UYARI(metod=self.dosyaSec, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.dosyaSec, inputs=True)
        try:
            dosyaAdi = input(self.configGetir(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(dosyaAdi)
            if self.dosyaMevcutMu(dosyaAdi) and self.txtDosyasiMi(dosyaAdi):
                return str(dosyaAdi)
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
                return self.dosyaSec()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)), 2)
            return self.dosyaSec()

    def dosyaIceriginiAl(self, dosya):
        try:
            icerik = set()
            with open(dosya, "r", encoding="utf-8") as satirlar:
                for satir in satirlar:
                    if len(satir.strip()) > 0:
                        icerik.add(satir.strip())
            return icerik
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.dosyaIceriginiAl, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)
            return False

    def dosyaIcerigiAlindiMi(self, icerik):
        if icerik:
            return True
        else:
            return False

    def dosyaMevcutMu(self, path):
        if os.path.isfile(path):
            return True
        else:
            return False

    def txtDosyasiMi(self, dosya):
        if os.path.splitext(dosya)[-1].lower() == ".txt":
            return True
        else:
            return False

    def klasorOlustur(self, klasor):
        base_warnings = self.BASE_UYARI(metod=self.klasorOlustur, warnings=True)
        if not os.path.exists(klasor):
            os.mkdir(klasor)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(klasor=klasor), 1)
        else:
            print(str(self.configGetir(base_warnings+"warning2")).format(klasor=klasor))
        self.klasorDegistir(klasor)
        print(str(self.configGetir(base_warnings+"warning3")).format(klasor=klasor))

    def klasorDegistir(self, klasor):
        os.chdir(klasor)

    def metindenKarakterSil(self, metin, silinecekKarakterler):
        return metin.replace(silinecekKarakterler, '')

    def inputTemizle(self, inpt):
        inpt.clear()

    def hedefKaynaktanBuyukMu(self, hedef, kaynak):
        if hedef > kaynak:
            hedef = kaynak
        return hedef

    def indexSifirla(self):
        self.index = 1

    def indexArtir(self):
        self.index = self.index + 1

    def degerVarMi(self, yorum):
        if len(yorum) > 0:
            return True
        else:
            return False

try:
    instagram = Instagram()
except KeyboardInterrupt:
    print("\n [*] Signing out from the application...")
    exit()


