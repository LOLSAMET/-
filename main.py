from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    shutdown_computer()
    return "Webpage loaded and computer is shutting down..."

def shutdown_computer():
    try:
        os.system("shutdown /s /t 0")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)
