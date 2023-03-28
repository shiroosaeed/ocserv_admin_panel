from flask import Flask, render_template, jsonify
import os
import json

from helpers import is_active

app = Flask(__name__)

app.config['template_engine'] = None


# load template section
@app.route('/')
def home():
    return render_template('index.html', is_active=is_active)


@app.route('/users_list')
def users_list():
    return render_template('users-list.html', is_active=is_active)


# api section
@app.route('/users')
def users():
    output = os.popen('sudo occtl -j show users').read()

    output = json.loads(output)

    final_users = []
    for user in output:
        users = []
        for i, u in user.items():
            newi = i.replace(" ", '-')
            users.append((newi, u))
        final_users.append(users)

    return final_users


# app runing
if __name__ == '__main__':
    app.run(debug=True)
