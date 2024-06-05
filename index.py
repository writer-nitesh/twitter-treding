from flask import Flask, render_template
from scrap_twitter import get_ip, get_trends, login_twitter
from pymongo.mongo_client import MongoClient

app = Flask(__name__)

uri = "mongodb+srv://test:test@url-shortner.feghp9s.mongodb.net/?retryWrites=true&w=majority&appName=url-shortner"
client = MongoClient(uri)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/trends")
def trend():
    try:
        bot = login_twitter()
        trends = get_trends(bot)
        ip = get_ip()

        db = client.get_database("trending_x")
        trends_collection = db.get_collection("trend")

        data = {
            'ip': ip,
            'trends': trends,
        }

        trends_collection.insert_one(data)


        db_data = trends_collection.find({})

        to_show = {
            'db_data': db_data,
            'ip': ip,
            'trends': trends
        }

        return render_template('trend.html', data=to_show)
    except Exception as e:
        return f'<p>{e}</p>'


if __name__ == '__main__':
    app.run(debug=True)
