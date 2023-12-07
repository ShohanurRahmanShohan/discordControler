from flask import Flask, render_template
import pyautogui

app = Flask(__name__)

# Function to trigger mute using pyautogui
def trigger_mute():
    # Simulate pressing Ctrl + Shift + M
    pyautogui.hotkey('ctrl', 'shift', 'm')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mute', methods=['POST'])
def mute():
    trigger_mute()
    return '', 204  # Return an empty response with status code 204 (No Content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
