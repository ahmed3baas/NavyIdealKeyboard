from flask import Flask, render_template
#https://www.codecademy.com/learn/learn-flask/modules/flask-templates-and-forms/cheatsheet
app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Scientist',
    'location': 'giza,egypt',
    'salary': '15,000 le'
}, {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'cairo,egypt',
    'salary': '10,000 le'
}, {
    'id': 3,
    'title': 'Back-End dev',
    'location': 'alxe,egypt',
}, {
    'id': 4,
    'title': 'Front-End dev',
    'location': 'mansura,egypt',
    'salary': '18,000 le'
}]


@app.route('/')
def index():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Ahmed')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
