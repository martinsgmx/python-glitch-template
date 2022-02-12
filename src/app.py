from os import environ
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template


load_dotenv() # get environment variables from .env


app = Flask(__name__)


@app.route("/")
def route_index() -> render_template:
  return render_template("index.html",
    utc_dt=datetime.utcnow()
  )


if __name__ == "__main__":
  app.run(
    port=environ.get("PORT"),
    debug=environ.get("IS_DEVELOPMENT")
  )
