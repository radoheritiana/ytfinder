from flask import Flask, request, jsonify
from flask_cors import CORS
from YTagFinder import YTagFinder

def tag_finder(url):
    ytag = YTagFinder()
    return ytag.find_tags(url)


app = Flask(__name__)
cors = CORS(app, resources={r"/ytag/api/*": {"origins": "https://ytagfinder.onrender.com"}})

@app.route('/ytag/api/tag_finder', methods=['GET'])
def get_tag():
	url = request.args.get('url')
	tags = {"tags": tag_finder(url)}
	return jsonify(tags)


if __name__ == "__main__":
	app.run(debug=True)