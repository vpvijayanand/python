from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    search_query = request.form.get('search')
    data = read_csv('countries.csv')
    if search_query:
        data = [row for row in data if row['country'].lower() == search_query.lower()]
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
