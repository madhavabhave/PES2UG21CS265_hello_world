from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Madhava Bhave"
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = subprocess.getoutput("top -bn1 | head -20")

    return f"""
    <html>
    <head><title>/htop Endpoint</title></head>
    <body>
        <h1>Name: {name}</h1>
        <h2>Username: {username}</h2>
        <h3>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

