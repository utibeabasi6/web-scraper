from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

server = Flask(__name__)

def scrape_website(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        return soup.find("title").text
    except:
        return "Sorry couldnt connect to the url"

@server.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get('url')
        result = scrape_website(url)
        return render_template('index.html', result=result)
    else:
        return render_template('index.html', result="")

if __name__ == "__main__":
    server.run(debug=True)