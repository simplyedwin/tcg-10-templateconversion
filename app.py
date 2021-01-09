from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/photo')
def photo():
    return render_template('photo.template.html')


@app.route('/video')
def video():
    return render_template('video.template.html')


@app.route('/about')
def about():
    return render_template('about.template.html')


@app.route('/contact')
def contact():
    return render_template('contact.template.html')


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
