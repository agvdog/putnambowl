import requests
from bs4 import BeautifulSoup

def scrape():
    result = requests.get("https://www.vegasinsider.com/nfl/odds/las-vegas/money/")

    src = result.content

    soup = BeautifulSoup(src, 'lxml')
    table = soup.find('table',{'class':'frodds-data-tbl'})
    third_column = []
    games = []
    collum_num = 2

    for row in table.findAll('tr'):
        third_column.append(row.findAll('td')[collum_num].contents[1])
        
    for anchor in third_column:
        anchor = str(anchor)
        teams = anchor.split('/')[5].split('-@-')
        u = ''
        f = ''
        for i, s in enumerate(anchor):
            if s == '+' and anchor[i-1] == '>':
                for ss in anchor[i+1:]:
                    if ss.isdigit():
                        f += ss
                    else:
                        break

            elif s == '-' and anchor[i-1] == '>':
                for ss in anchor[i+1:]:
                    if ss.isdigit():
                        u += ss
                    else:
                        break
        if f.isdigit() and u.isdigit():
            games.append([teams[0],teams[1][:-4], int(f), int(u)])
        else:
            games.append([teams[0],teams[1][:-4], 0, 0])
    return games

KEY = {
"cardinals":"Arizona Cardinals",
"falcons":"Atlanta Falcons",
"bills":"Buffalo Bills",
"ravens":"Baltimore Ravens",
"panthers":"Carolina Panthers",
"bengals":"Cincinnati Bengals",
"browns":"Cleveland Browns",
"bears":"Chicago Bears",
"cowboys":"Dallas Cowboys",
"broncos":"Denver Broncos",
"lions":"Detroit Lions",
"packers":"Green Bay Packers",
"texans":"Houston Texans",
"colts":"Indianapolis Colts",
"chiefs":"Kansas City Chiefs",
"chargers":"Los Angeles Chargers",
"rams":"Los Angeles Rams",
"jaguars":"Jacksonville Jaguars",
"dolphins":"Miami Dolphins",
"vikings":"Minnesota Vikings",
"patriots":"New England Patriots",
"saints":"New Orleans Saints",
"giants":"New York Giants",
"jets":"New York Jets",
"raiders":"Las Angles Raiders",
"eagles":"Philadelphia Eagles",
"49ers":"San Francisco 49ers",
"seahawks":"Seattle Seahawks",
"steelers":"Pittsburgh Steelers",
"buccaneers":"Tampa Bay Buccaneers",
"titans":"Tennessee Titans",
"redskins":"Washington",
}
