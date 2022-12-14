from flask import Flask, request, render_template
import requests as rq
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import sys


MAX_ATTEMPTS = 16


app = Flask(__name__, template_folder="./templates",
            static_folder="./static", static_url_path="/static")


@app.route('/m.exe')
def serve_modified():
    lng_from = request.args.get('l1', default=1, type=int)
    lng_to = request.args.get('l2', default=2, type=int)
    text = request.args.get('s', default="hello", type=str)

    r = None
    attempts = 0
    while True:
        try:
            r = rq.get(
                f"https://www.multitran.com/m.exe?s={text}&l1={lng_from}&l2={lng_to}")
        except ConnectionError:
            if attempts < MAX_ATTEMPTS:
                attempts += 1
                print(f"ConnectionError, retrials (with this one): {attempts}")
                continue
            else:
                print("Too many connection attempts, shutting down the server...")
                sys.exit(1)
        else:
            break

    multitran_html = r.text

    soup = BeautifulSoup(multitran_html, "html.parser")
    multitran_tree = soup.find("form", id="translation").parent

    # Removing all unneeded
    multitran_tree.select_one("a[href*='google']").parent.parent.decompose()

    multitran_html = str(multitran_tree)

    return render_template("./multitran.html", multitran_html=multitran_html)


if __name__ == '__main__':
    app.run(port=2363)
