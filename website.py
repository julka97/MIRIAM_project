import requests, webbrowser, bs4

def open(word_to_search):
    res = requests.get('http://google.com/search?q={0}'.format(word_to_search), 'lxml')
    res.raise_for_status()

    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Open a browser tab for each result.
    linkElems = soup.select('.r a')
    webbrowser.open('http://google.com' + linkElems[0].get('href'))