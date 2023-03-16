from bs4 import BeautifulSoup 
import requests 
import subprocess
import os
import shutil
import webbrowser
def extract_headlines():
    source = requests.get('https://www.prensalibre.com/')
    soup = BeautifulSoup(source.text, 'lxml')
   
    cont = 0
    for article in soup.find_all('article'):
        
        try:
            
            headline = article.h1.a.text
            headline_url = article.h1.a
            url_list.append(headline_url['href'])
            cont += 1 
            headline_list.append(str(cont) + ". " + headline.strip()) 
              
        except AttributeError:
            pass 
        
def open_browser(choose):
    webbrowser.open(url_list[choose-1], new=0)
    #subprocess.Popen(['c:/Program Files/Mozilla Firefox/firefox.exe', url_list[choose-1]])

def show_page(page):
      columns = shutil.get_terminal_size().columns 
      try: 
    
          if(page == 1):
            print("\npagina 1/11")
            print("Primera Plana\n".center(columns))
            for page_1 in range(0, 4):
                print(headline_list[page_1]) 

          elif(page == 2):
            print("\npagina 2/11") 
            print("La mas reciente\n".center(columns))
            for page_2 in range(4, 9):
                print(headline_list[page_2])  

          elif(page == 3):
            print("\npagina 3/11") 
            print("Todo sobre las vacunas contra covidad 19\n".center(columns))
            for page_3 in range(9, 14):
                print(headline_list[page_3])  

          elif(page == 4):
            print("\npagina 4/11") 
            print("Lo mas destacado\n".center(columns)) 
            for page_4 in range(14, 21):
                print(headline_list[page_4])  

          elif(page == 5):
            print("\npagina 5/11") 
            print("BBC News Mundo\n".center(columns))
            for page_5 in range(21,28):
                print(headline_list[page_5])  

          elif(page == 6):
            print("\npagina 6/11") 
            print("The Conversation\n".center(columns))
            for page_6 in range(28,34):
                print(headline_list[page_6])  
          elif(page == 7):
            print("pagina 7/11") 
            print("Editorial\n".center(columns))
            for page_7 in range(34,36):
                print(headline_list[page_7])  

          elif(page == 8):
            print("\npagina 8/11") 
            print("Ciudades\n".center(columns))
            for page_8 in range(36,41):
                print(headline_list[page_8])  

          elif(page == 9):
            print("\npagina 9/11")   
            print("Internacional\n".center(columns))
            for page_9 in range(41,48):
                print(headline_list[page_9])  

          elif(page == 10):
            print("\npagina 10/11") 
            print("Vida\n".center(columns))
            for page_10 in range(48,53):
                print(headline_list[page_10])  

          elif(page == 11):
            print("\npagina 11/11".center(columns))
            print("Deportes\n".center(columns)) 
            for page_11 in range(53, 60):
                print(headline_list[page_11])  
       
          elif(page < 1 or page > 11):
            print("paginas '11'")
            print("Error: Esta pagina no existe")

      except (ValueError, TypeError):
          print("Error: Esta opcion no existe")                   

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
   
    extract_headlines()
    show_page(1) 
    
    flag = True
    actual_page = "1"
    while(flag):
        
        try:
        
            print("\n(Escribe '0' para salir) \n(Escribe 'this' para elegir la pagina acutal pagina)", end='') 
            choose = input("\nPagina a Elegir: ")
            if(choose == "0"):
                print("Saliendo...")
                flag = False
            elif(choose == "this"):
                clear()
                show_page(int(actual_page))
                choose_news = input("\nElige la notcia: ")
                if(choose_news == "back"):
                    clear()
                    show_page(actual_page)
                    continue
                else:
                    open_browser(int(choose_news))
                    flag = False
            else:
                actual_page = choose
                clear() 
                show_page(int(choose))

        except (ValueError, TypeError):
            clear()
            print("paginas '11'")
            show_page(actual_page)

headline_list = []
url_list = []
main()
