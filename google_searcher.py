import webbrowser
import sys
import pyperclip
import requests
import bs4


def main():
    if len(sys.argv) > 1:
        keyword = ' '.join(sys.argv[1:])
    else:
        keyword = pyperclip.paste()

    res = requests.get('http://google.com/search?q=' + keyword)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    linkElems = soup.select('.r a')
    numOpen = min(5, len(linkElems))

    for i in range(numOpen):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))


if __name__ == '__main__':
    main()
