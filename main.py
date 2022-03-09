import requests, bs4
from plyer import notification
import os



numTrades = 0

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
    file = open("CurrentTrades.py" , "r")
    trades=0

    trades= file.read()

    print ( numTrades, trades)
    x = int(trades)


    file.close()

    print(os.getcwd())
    if int(numTrades) == x :
        #print("No new Trades")
        openfile = open("C:/Users/valmi/Documents/Code/Temp Files/output.txt","w")
        openfile.write("No new trades for now.")
        openfile.close()
    else:
        openfile = open("C:/Users/valmi/Documents/Code/Temp Files/output.txt", "w")
        openfile.write("New Trade Alert.")
        openfile.close()

        notification.notify(
            title = 'testing',
            message = ' Nancy Pelocy made a Trade',
            app_icon = None,
            timeout = 10

        )


        updateFile(x) #update the file witha new number


def updateFile(trades):
    file = open("CurrentTrades.py", "a")
    file.write(trades)
    file.close()




main()
