from bottle import route, run
from datetime import datetime as dt
import os


@route("/")
def index():
  now = dt.now()
  return {
    "Проверка Heroku": "OK3",
    "date": f"{now.day} {now.month} {now.year}"
  }

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)