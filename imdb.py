from requests import Session
s = Session()
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Alt-Used': 'www.imdb.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.imdb.com/title/tt5433140/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_fast',
    # 'Cookie': 'session-id=144-4361253-3421746; session-id-time=2082787201l; csm-hit=tb:V38WBEE07DGW3XZ4B2QA+s-M9QQS60WW0SZKJ98RRZF^|1686044466008&t:1686044466009&adb:adblk_no; ubid-main=130-2846059-1262016; session-token=1hjEbFPDVpRZHHsgITNrtCIV5exLRaMfTCb/81Tz14lOrNewGM5IRPSYYz4barGGLWNsRWRVQsVr4IcHDQEnWZGbXoZoRVhWq3PSxStV+DUsCE/XeH2l7WM6pfg8ew5pjuUb1goBmZhzWVSTsZn4vm/TfxR4EWN/hwPFOuy5YW9XWdpZqaiRja5tlPFg4QegpEo+PzmraDGD+yI9+mTZ/g',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

s.headers.update(headers)
url="https://www.imdb.com/title/tt0458339/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_avenger"
def main_crawler(url):
    r=s.get(url)
    soup=bs(r.content,"html.parser")
    products=soup.find_all("div","ipc-page-content-container ipc-page-content-container--center")
    for i in products:
        e=i.find('h1')
        if e:
            # print(e.text)
            realising_date=i.find('ul','ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt')
            realising_date=realising_date.text.replace("PG-13"," ")
            rating=i.find("div","sc-bde20123-2 gYgHoj")
            rating=rating.text
            video_link=i.find("div","sc-385ac629-9 jiVoNU")
            video_link=video_link.find('a').get('href')
            # print("https://www.imdb.com"+video_link)
            photo_link=i.find("a","ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-baseAlt ipc-btn--theme-baseAlt ipc-btn--on-onBase ipc-secondary-button sc-ceb22a5b-3 lltPEH")
            photo_link=photo_link.get('href')
            print("https://www.imdb.com"+photo_link)
            movie_history=i.find("span","sc-2eb29e65-2 jBnwaA")
            movie_history=movie_history.text
            star_name=i.find("a","ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
            star_name=star_name.text
            writers = [i.text.strip() for i in soup.find('div', 'sc-52d569c6-3 jBXsRT').find('li', 'ipc-metadata-list__item ipc-metadata-list-item--link').find('div', 'ipc-metadata-list-item__content-container').find_all('li')]
            print(writers)
main_crawler(url)
            