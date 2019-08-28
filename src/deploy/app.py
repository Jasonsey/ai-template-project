# Dispatch Analysis
#
# Author: Lin, Max
# Email: max_lin1@dell.com
#
# =============================================================================
"""flask app"""
from flask import Flask, request, jsonify, redirect, url_for, render_template


app = Flask(__name__, template_folder='templates')    # template_folder提供的参数相对路径为相对app.py的相对路径


@app.route('/')
def home():
    return 'CIS WEB APP'


@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('home'))    # url_for 参数为函数名


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

