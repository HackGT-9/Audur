import os
from flask import Flask, render_template, request, send_from_directory
import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/ec2-user/AudioShare/uploads'

def shorten(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

@app.route('/')
def hello():
        return render_template("index_old.html")

@app.route('/about_old.html', methods=['GET', 'POST'])
def hello_from_about():
        return render_template("about_old.html")

@app.route('/index_old.html')
def return_here():
        return render_template('index_old.html')

@app.route('/upload_old.html', methods=['GET', 'POST'])
def upload_da_file():
        return render_template('upload_old.html')

@app.route('/song_old.html', methods=['GET', 'POST'])
def song_page():
    if request.method == 'POST':
        info = request.form
        file = request.files['file']
        fin = file.filename.replace(" ", "-")
        res_p = os.path.join(app.config['UPLOAD_FOLDER'], fin)
        file.save(res_p)
        res_link = shorten('http://52.87.189.186:5000'+app.config['UPLOAD_FOLDER']+'/'+fin)
        return render_template('song_old.html', title=info['titleArea'], desc=info['descriptionArea'], pth=res_p, link=res_link)

@app.route('/home/ec2-user/AudioShare/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True, port=5000)
