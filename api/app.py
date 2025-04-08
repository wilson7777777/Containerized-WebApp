from flask import Flask, jsonify, request
import psycopg2
import redis
import os

app = Flask(__name__)
db_conn = psycopg2.connect(
    host=os.environ.get('DB_HOST', 'db'),
    user=os.environ.get('DB_USER', 'postgres'),
    password=os.environ.get('DB_PASSWORD', 'postgres'),
    dbname=os.environ.get('DB_NAME', 'postgres')
)
redis_client = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'POST':
        item = request.get_json()['item']
        with db_conn.cursor() as cur:
            cur.execute("INSERT INTO items (name) VALUES (%s)", (item,))
            db_conn.commit()
        redis_client.delete('items')
        return jsonify({'message': 'Item added'})
    else:
        cached_items = redis_client.get('items')
        if cached_items:
            return jsonify(eval(cached_items.decode('utf-8')))
        with db_conn.cursor() as cur:
            cur.execute("SELECT name FROM items")
            items = [row[0] for row in cur.fetchall()]
        redis_client.set('items', str(items))
        return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
