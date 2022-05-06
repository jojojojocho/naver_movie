import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
from datetime import timedelta
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.DataFrame(columns=['ranking', 'title', 'score', 'date'])
    formatter = "%Y%m%d"

    date = datetime(2022, 5, 5)
    enddate = datetime(2022, 5, 6)
    sub = (enddate - date).days
    for n in range(0, sub):

        string_date = str(date.strftime(formatter))
        url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=" + string_date
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        response = requests.get(url=url, headers=headers)
        soup = bs(response.text, 'html.parser')
        title = soup.find_all("div", "tit5")
        score = soup.find_all("td", "point")

        for i in range(0, len(title)):
            df1 = pd.DataFrame(
                {'ranking': i+1, 'title': title[i].find_next('a').attrs['title'], 'score': score[i].text, 'date': [string_date]},
                columns=['ranking', 'title', 'score', 'date'])
            df = pd.concat([df, df1])

        date += timedelta(days=1)

    df.to_csv("./naver_movie.csv", index=False, encoding='utf-8')
