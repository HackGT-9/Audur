import os
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\sthelluri1\\Desktop\\HackGT2022\\uploads'
@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/about.html', methods=['GET', 'POST'])
def hello_from_about():
	return render_template("about.html")

@app.route('/index.html')
def return_here():
	return render_template('index.html')

@app.route('/upload.html', methods=['GET', 'POST'])
def upload_da_file():
	return render_template('upload.html')

@app.route('/song.html', methods=['GET', 'POST'])
def song_page():
    if request.method == 'POST':
        info = request.form
        file = request.files['file']
        fin = file.filename
        res_p = os.path.join(app.config['UPLOAD_FOLDER'], (fin).replace("/", "\\\\"))
        res_p = res_p.replace("/", "\\")
        #rep = "\\"+fin
        #res_p = res_p.replace(rep, "\\\\"+fin)
        file.save(res_p)
        #print(res_p, fin)
        #rep = "\\"+fin
        #res_p = res_p.replace(rep, "\\\\"+fin)
        stuff = res_p.split("\\")
        paath = stuff[-2]+"\\\\\\\\"+stuff[-1]
        return render_template('song.html', title=info['titleArea'], desc=info['descriptionArea'], pth=".\\\\"+paath)
@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_file(app.config['UPLOAD_FOLDER']+'\\'+filename)
    #return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)

