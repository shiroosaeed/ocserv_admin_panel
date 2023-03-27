from flask import Flask, render_template,jsonify
import os
import json
app = Flask(__name__)

app.config['template_engine'] = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users')
def users():
    output = os.popen('sudo occtl -j show users').read()
    
    output = json.loads(output)
    
    return output
    
    
    
if __name__ == '__main__':
    app.run()
