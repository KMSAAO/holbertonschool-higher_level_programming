import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# دالة قراءة JSON
def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# دالة قراءة CSV
def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except FileNotFoundError:
        pass
    return products

# دالة قراءة SQL (الجديدة)
def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # لكي نحصل على النتائج كقاموس (Dictionary) بدلاً من Tuple
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        # تحويل الصفوف لقائمة قواميس لتناسب القالب
        products = [dict(row) for row in rows]
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    products = []

    # 1. اختيار مصدر البيانات
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    # 2. فلترة البيانات حسب الـ id إذا طلب المستخدم
    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)