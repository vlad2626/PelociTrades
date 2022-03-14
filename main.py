import requests, bs4
from plyer import notification
import os



numTrades = 0 # number online in website

def main():
    request()
    compare()



def request():
    res = requests.get('https://www.capitoltrades.com/politicians/P000197')
    res.raise_for_status()
    pelosiSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    #print(res.text)
    compile(pelosiSoup)


def compile(pelosiSoup):
    global numTrades
    name = pelosiSoup.select('div.politician-profile__senator-name')
    trades = pelosiSoup.select('div.q-value')
    numTrades = trades[0].getText()


def compare():

    if(os.stat("CurrentTrades.py").st_size == 0):
        print("file is empty ")
        exit()




    file = open("CurrentTrades.py" , "r")

    trades=0
    madeTrade = False

    trades= file.read()

    print ("online", numTrades, " local", trades)
    x = int(trades) # local number on file


    file.close()

    print(os.getcwd())
    if int(numTrades) >= x :
        #print("No new Trades")
        openfile = open("C:/Users/valmi/Documents/Code/Temp Files/output.txt","w")
        openfile.write("No new trades for now.")
        openfile.close()

        notification.notify(
            title='Nancy Pelocy Trade',
            message=' no New Trades',
            app_icon= None,
            app_name = 'Nancy Pelocy Trades',
            timeout=10
        )
        madeTrade= False
    else:
        madeTrade = True
        openfile = open("C:/Users/valmi/Documents/Code/Temp Files/output.txt", "w")
        openfile.write("New Trade Alert.")
        openfile.close()

        notification.notify(
            title = 'testing',
            message = ' Nancy Pelocy made a Trade',
            app_icon = None,
            app_name = 'Nancy Pelocy Trades',
            timeout = 10
        )
        file = open("CurrentTrades.py", "w")
        file.write(numTrades)
        file.close()









main()
