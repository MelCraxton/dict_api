from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<word>')
def about(word):
    result_dict = {
        'Definition': word.upper(),
        'Word': word
    }
    return result_dict

if __name__ == '__main__':
    app.run(debug=True, port=5001)