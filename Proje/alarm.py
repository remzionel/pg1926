#!/usr/bin/env python
# -*- coding: UTF-8 -*-



import RPi.GPIO as GPIO

import os

import sys

import time

import pytz

import smtplib

import subprocess

from email.mime.multipart import MIMEMultipart

from email.mime.image import MIMEImage

from email.mime.text import MIMEText

from email.utils import formataddr

from email import encoders

from threading import Thread

from datetime import datetime

from requests import get


ALARM_SURESI = 30
BEKLEME_SURESI = 3

LED_YAK = True
ALARM_CAL = False
EPOSTA_GONDER = True

SENSOR = 29
LED_K_1 = 31
LED_K_2 = 33
LED_P = 35
LED_Y = 11
BUZZ = 37
MOTION_PORT = 8080
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_K_1, GPIO.OUT)
GPIO.output(LED_K_1, GPIO.LOW)
GPIO.setup(LED_K_2, GPIO.OUT)
GPIO.output(LED_K_2, GPIO.LOW)
GPIO.setup(LED_P, GPIO.OUT)
GPIO.output(LED_P, GPIO.LOW)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.output(LED_Y, GPIO.LOW)  
GPIO.setup(BUZZ, GPIO.OUT)
GPIO.output(BUZZ, GPIO.LOW)

sunucu = 'smtp.example.com'
port = 465
sertifika = 'ssl'

gonderen_isim = 'Home Security'
gonderen_eposta = 'home@example.com'
gonderen_sifre =  'Password'

alici_eposta = 'johndoe@example.com'
alici_isim = 'John Doe'

resim_yolu = '/root/alarm/resimler/'
resim_ismi = '';

eskileriSil = subprocess.Popen('find ' + resim_yolu + ' -type f -mtime +15 -delete', shell=True)

eskileriSil.wait()

def epostaGonder():
    
    global ZAMAN
    
    global resim_ismi
    
    print ('E-Posta Gönderiliyor...')
    
    ip = get('https://api.ipify.org').text

    mesaj = MIMEMultipart()

    mesaj['Subject'] = 'ALARM!'

    mesaj['From'] = formataddr((gonderen_isim, gonderen_eposta))

    mesaj['To'] = formataddr((alici_isim, alici_eposta))
    
    metin = MIMEText('<h3><b>' + ZAMAN.strftime('%d/%m/%Y - %H:%M:%S') + ' Tarihinde Evde Hareket Algılandı!<br>Anlık görüntü ektedir.<br><br><a href="http://' + ip + ':' + MOTION_PORT + '/">CANLI İZLEMEK İÇİN TIKLAYIN!</a></b></h3>', 'html', 'utf-8')
    
    mesaj.attach(metin)
    
    try:
    
        with open(resim_yolu + resim_ismi, 'rb') as resim_oku:
            
            resim = MIMEImage(resim_oku.read(), name=os.path.basename(resim_yolu + resim_ismi))
        
        resim.add_header('Content-Disposition', 'attachment; filename=' + resim_ismi)
        
        mesaj.attach(resim)
    
    except Exception as hata:
    
        print(resim_yolu + resim_ismi + ' isimli resim dosyası yüklenemedi!n' + str(hata))
        
        
    try:
        
        if (sertifika=='ssl'):

            eposta = smtplib.SMTP_SSL(sunucu, port)
        
        elif (sertifika=='tls'):

            eposta = smtplib.SMTP_TLS(sunucu, port)            

        eposta.login(gonderen_eposta, gonderen_sifre)

        eposta.sendmail(gonderen_eposta, alici_eposta, mesaj.as_string())

        eposta.quit()

        os.remove(resim_yolu + resim_ismi)

        print('E-Posta Gönderildi.')

    except Exception as hata:

        print('E-Posta Gönderilemedi!n' + hata)
        
        
def fotoCekveGonder():
    
    global ZAMAN
    
    global resim_ismi
    
    resim_ismi = 'home-' + str(ZAMAN.timestamp()) + '.jpg'
        
    print('Fotoğraf Çekiliyor...')
    
    motionKapat = subprocess.Popen('service motion stop', shell=True)
    
    motionKapat.wait()
    
    camera = subprocess.Popen('fswebcam -s brightness=50% -r 640x480 ' + resim_yolu + resim_ismi, shell=True)

    camera.wait()
    
    print('Fotoğraf Çekildi.')
    
    motionBaslat = subprocess.Popen('service motion start', shell=True)
        
    if(EPOSTA_GONDER==True):
    
        epostaGonder()
        

ALARM_SAY = 0

def alarmCal():
    
    global ALARM_SAY
    
    global ALARM_SURESI
    
    GPIO.output(LED_Y, GPIO.LOW)
    
    if(ALARM_SAY==0):
        
        print('Alarm Çalıyor...')
        
    while(ALARM_SAY < ALARM_SURESI):
        
        if(LED_YAK==True):
    
            GPIO.output(LED_K_1, GPIO.HIGH)
    
            GPIO.output(LED_K_2, GPIO.LOW)
    
            GPIO.output(LED_P, GPIO.HIGH)
        
        if(ALARM_CAL==True):
        
            GPIO.output(BUZZ, GPIO.HIGH)
        
        time.sleep(0.3)
        
        if(LED_YAK==True):
        
            GPIO.output(LED_K_1, GPIO.LOW)
            
            GPIO.output(LED_K_2, GPIO.HIGH)
            
        if(ALARM_CAL==True):
            
            GPIO.output(BUZZ, GPIO.LOW)
        
        time.sleep(0.3)
        
        ALARM_SAY += 1
        
        return alarmCal()
    
    else:
    
        return alarmDur()
    
        
def alarmDur():
    
    global ALARM_SAY
        
    GPIO.output(LED_K_1, GPIO.LOW)
        
    GPIO.output(LED_K_2, GPIO.LOW)
    
    GPIO.output(LED_P, GPIO.LOW)
        
    GPIO.output(BUZZ, GPIO.LOW)
    
    GPIO.output(LED_Y, GPIO.HIGH)
    
    ALARM_SAY = 0
    
    print('Alarm Durdu.')
    

yayinBaslat = subprocess.Popen('service motion start', shell=True)

    
BEKLE = 0

def alarmBaslat():

    global BEKLE

    global BEKLEME_SURESI
    
    while(BEKLE < BEKLEME_SURESI):

        SAY = BEKLEME_SURESI-BEKLE

        print('Alarm ' + str(SAY) + ' Saniye İçinde Aktifleştirilecek...')

        time.sleep(1)

        BEKLE += 1
        
        return alarmBaslat()

    else:

        GPIO.setup(SENSOR, GPIO.IN)

        GPIO.output(LED_Y, GPIO.HIGH)

        print('Alarm Aktifleştirildi!')


alarmBaslat()

try:
    
    while True:
        
        if(GPIO.input(SENSOR)):
            
            print('Hareket Algılandı!')
            
            ZAMAN = datetime.now(pytz.timezone('Europe/Istanbul'))
            
            fotoCekveGonderFunc = Thread(target=fotoCekveGonder)
            
            alarmCalFunc = Thread(target=alarmCal)
            
            fotoCekveGonderFunc.start()
            
            alarmCalFunc.start()
            
            time.sleep(ALARM_SURESI)
        
except KeyboardInterrupt:
        
    GPIO.cleanup()
        
except:
        
    GPIO.cleanup()
