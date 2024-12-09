from flask import Flask, render_template

app = Flask(__name__)
application = app  # Required for AWS compatibility

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/quiz.html')
def quiz():
    return render_template('quiz.html')

@app.route('/flash.html')
def flashcards():
    return render_template('flash.html')

@app.route('/ai_chat.html')
def ai_chat():
    return render_template('ai_chat.html')

# Removing the app.run() call
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
