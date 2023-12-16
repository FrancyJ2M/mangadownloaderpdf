import requests
import time

url = 'https://api.render.com/deploy/srv-clbo0qeg1b2c73cfqud0?key=5GGATa11GRA'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'	
}

def reiniciar_proyecto():
    response = requests.post(url,headers=headers)
    print(response.text)
    if response.status_code == 200:
        print("\nBot: @manga_pdf_Robot reiniciado exitosamente")
    else:
        print(f"Hubo un error al reiniciar el proyecto. Código de estado: {response.status_code}")

#reiniciar_proyecto()

while True:
    reiniciar_proyecto()
    time.sleep(3600 * 8)
    
#Power by frankramiro.martinez@nauta.cu