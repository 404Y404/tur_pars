import requests
from bs4 import BeautifulSoup

links = ["https://vvvgamers.com/ru/pubg-mobile/tournaments", "https://vvvgamers.com/ru/pubg-desktop/tournaments", "https://vvvgamers.com/ru/brawl-stars/tournaments", "https://vvvgamers.com/ru/free-fire/tournaments",
                 "https://vvvgamers.com/ru/standoff/tournaments", "https://vvvgamers.com/ru/pubg-new-state/tournaments", "https://vvvgamers.com/ru/clash-royale/tournaments", "https://vvvgamers.com/ru/lichess/tournaments"]

intro = """
  ________  ______  _   __________     ____  ___    ____  _____ ______
 /_  __/ / / / __ \/ | / /  _/ __ \   / __ \/   |  / __ \/ ___// ____/
  / / / / / / /_/ /  |/ // // /_/ /  / /_/ / /| | / /_/ /\__ \/ __/   
 / / / /_/ / _, _/ /|  // // _, _/  / ____/ ___ |/ _, _/___/ / /___   
/_/  \____/_/ |_/_/ |_/___/_/ |_|  /_/   /_/  |_/_/ |_|/____/_____/   
                                                                      

"""


def parse(link):
    respon = requests.get(link)
    soup = BeautifulSoup(respon.text, 'html.parser')
    res = []
    for tur in soup.find_all("a"):
        if "Freeroll" in str(tur):
            res.append("https://vvvgamers.com/" + tur.get("href"))
    return res


def main():
    print(intro)
    for link in links:
        out = parse(link)
        if out != []:
            print(out[0].split("/")[5])
            print(*out, sep="\n")
            print()


if __name__ == '__main__':
    main()
