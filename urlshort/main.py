from flask import Flask, redirect

app = Flask(__name__)


pathsToUrls = {
    "test-google": "https://google.com",
    "test-face":     "https://facebook.com",
    "main-landing": "https://bloomberg.com"
}


@app.route('/')
def index():
    return '<h2>Hello</h2>'


@app.route("/<short_url>")
def shorter_url(short_url):
    redirected_url = pathsToUrls.get(short_url, "https://bloomberg.com")
    return redirect(redirected_url)


if __name__ == "__main__":
    app.run(debug=True)
