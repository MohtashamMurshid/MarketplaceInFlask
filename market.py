from flask import Flask , render_template


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
 return render_template("index.html")

@app.route('/market')
def market_place():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
        {'id': 4, 'name': 'Headphones', 'barcode': '843212299812', 'price': 200},
        {'id': 5, 'name': 'Monitor', 'barcode': '657483920384', 'price': 300},
        {'id': 6, 'name': 'Mouse', 'barcode': '129847654392', 'price': 50},
        {'id': 7, 'name': 'Tablet', 'barcode': '493212489731', 'price': 400},
        {'id': 8, 'name': 'Smartwatch', 'barcode': '785493120948', 'price': 250},
        {'id': 9, 'name': 'Camera', 'barcode': '294857301284', 'price': 800},
        {'id': 10, 'name': 'Printer', 'barcode': '758493028347', 'price': 150},
        {'id': 11, 'name': 'External Hard Drive', 'barcode': '983201948573', 'price': 100},
        {'id': 12, 'name': 'Speakers', 'barcode': '384750294738', 'price': 120},

    ]

    return render_template('market.html', items = items)


if __name__ == '__main__':
     app.run(host = '0.0.0.0' , debug=True)
