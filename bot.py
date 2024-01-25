from flask import Flask, render_template
# from apscheduler.schedulers.background import BackgroundScheduler
# from openpyxl import Workbook, load_workbook
# import os


app = Flask(__name__, static_folder='static')


@app.route('/deposit/<deposit_id>')
def deposit(deposit_id):
    return render_template('index2.html', deposit_id=deposit_id)


if __name__ == '__main__':
    app.run(port=8000 , debug=True)