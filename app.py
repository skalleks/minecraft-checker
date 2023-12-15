from flask import Flask, render_template, request, jsonify
import webbrowser
import threading
import os

app = Flask(__name__)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

def search_in_file(nickname):
    results = []
    if os.path.exists('base.txt'):
        with open('base.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if parts[0].lower() == nickname.lower():  
                    results.append(parts)
    return results


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    nickname = request.form['nickname']
    search_result = search_in_file(nickname)
    return jsonify(search_result)

if __name__ == '__main__':
    threading.Thread(target=open_browser).start()
    app.logger.disabled = True
    print("Скрипт запущен на http://127.0.0.1:5000/")
    app.run()