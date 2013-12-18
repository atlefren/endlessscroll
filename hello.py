import json
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def list():
    return render_template('list.html')

@app.route("/api/items/")
def api():

    limit = int(request.args.get('limit', 20))
    offset = int(request.args.get('offset', 0))

    return json.dumps([{"name": "Item %s" % index } for index in range(offset, offset + limit)])


if __name__ == "__main__":
    app.run()
