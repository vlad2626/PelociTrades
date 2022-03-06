import requests, bs4
from plyer import notification



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


    if int(numTrades) == x :
        print("No new Trades")
    else:
        notification.notify(
            title = 'testing',
            message = ' Nancy Pelocy made a Trade',
            app_icon = None,
            timeout = 10

        )

        file.close()
        updateFile(trades) #update the file witha new number


def updateFile(trades):
    file = open("CurrentTrades.py", "w")
    file.write(int(trades))




main()
