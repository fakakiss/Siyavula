from pyramid.view import view_config
import requests
from bs4 import BeautifulSoup


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    if request.method == "POST":
        clearwiki = request.POST["clearwiki"]
        if clearwiki == 1:
            scrapwiki = 0
            tch = 0

    return {'project': 'siya'}


@view_config(route_name='scrap', renderer='templates/scrap.jinja2')
def scrap(request):
    global tch

    if request.method == "POST":
        tch = 0
        scrapwiki = request.POST["scrapwiki"]


        if scrapwiki is not None and ("https://en.wikipedia.org/wiki/" or "http://en.wikipedia.org/wiki/") in scrapwiki:


            request = requests.get(scrapwiki)
            content = request.content
            soup = BeautifulSoup(content, "html.parser")
            element = soup.find("div", {"id": "toc", "class": "toc"})
            tch = element

            if tch is not None:
                # Scrap.scrapper(scrapurl)
                #tc  = element.text
                tch = element
            else:
                tch = "This Link Does Not Have a Table of Content or not a valid URL for the APP"
        tch=tch
        scrapwiki =0

        return {'url': tch}