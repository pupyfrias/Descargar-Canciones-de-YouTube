
import urllib.request
import urllib.parse
import requests
import os
import youtube_dl
from bs4 import BeautifulSoup as bs
import drivers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

os.system('cls')


def descargarMP3(enlace):

    try:
        video_info = youtube_dl.YoutubeDL().extract_info(url=enlace, download=False)
        video_title = video_info['title'].replace("/","").replace(":","").replace("?","")\
            .replace('"',"").replace("<","").replace(">","").replace("|","").replace(r"\ ","")\
               

        video_title2 = video_title.split(" ")  
        i = 0
        porcieto = 0
        duplicado = 0
        cantidaPalabras = len(video_title2)
        cantidaPalabras2 = len(video_title2)

        todasCanciones = os.listdir()
        total = len(todasCanciones)
        total2 = len(todasCanciones)

        while total >0:

            
            titulo = todasCanciones[total-1][:todasCanciones[total-1].find(".")]
            
            while cantidaPalabras >0:
            
                if video_title2[cantidaPalabras-1].lower() in  titulo.lower():
                    i += 1

                cantidaPalabras += -1

            try:    
                porcieto = (i/cantidaPalabras2)*100 
            except ZeroDivisionError:
                pass
            
            if porcieto >= 55:
                duplicado= 1
                porcieto = 0

            total += -1
            i = 0
            cantidaPalabras = cantidaPalabras2

        #Setear las opciones para la descarga del video
      
        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': f"./{busqueda}/{video_title}.mp3", #Seteamos la ubicacion deseada
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }],
        }

        #Descargamos el video
        with youtube_dl.YoutubeDL(opciones) as ydl:
            if os.path.isfile(f"./{busqueda}/{video_title}.mp3"):
                pass
            elif duplicado == 1:
                pass
            else:
                
                ydl.download([enlace]) 
    except:
        pass       


#youtube_dl.expand_path("")

busqueda = input("INGRESE EL NOMBRE DEL ARTISTA:\n")


driver = drivers.driver()
driver.get("https://www.youtube.com")

WebDriverWait(driver, 15)\
                .until(EC.element_to_be_clickable((By.XPATH,
                                                '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')))\
                .send_keys(busqueda)


WebDriverWait(driver, 10)\
                .until(EC.element_to_be_clickable((By.XPATH,
                                                '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')))\
                .click()

WebDriverWait(driver, 10)\
                .until(EC.element_to_be_clickable((By.XPATH,
                                                '//*[@id="items"]/ytd-watch-card-compact-video-renderer[1]')))\
                .click()


time.sleep(5)
soup = bs(driver.page_source, "html.parser")
pagina = soup.findAll("ytd-playlist-panel-video-renderer",class_="style-scope ytd-playlist-panel-renderer")
driver.close()


for x in pagina:
   link = "https://www.youtube.com"+ x.a.get("href")[:20]
   descargarMP3(link)

exit()


