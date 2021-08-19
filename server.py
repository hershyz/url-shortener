from flask import Flask, request

app = Flask(__name__)

# [shortened string, url]
db = []

@app.route("/")
def home():
    return "no url!"

@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    shortened = data['shortened']
    url = data['url']
    for element in db:
        if element[0] == shortened:
            return "shortened url already exists!"
    db.append([shortened, url])
    return "shortened url created!"

@app.route("/<shortened>")
def redirect(shortened):
    for element in db:
        if element[0] == shortened:
            return '<a href="' + element[1] + '">Link</a>'
    return "shortened url not found!"

if __name__ == "__main__":
    app.run()