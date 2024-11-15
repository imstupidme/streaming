from flask import Flask, render_template, request
from googleapiclient.discovery import build

app = Flask(__name__)

YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    response = youtube.search().list(q=query, part='snippet', type='video').execute()
    videos = response.get('items', [])
    return render_template('results.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
