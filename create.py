import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATION "] = False
db.init_app(app)

def main():
    db.create_all()
    flight = Flight(id=253, origin="delhi", destination="vizag", duration=200)
    db.session.add(flight)
    db.session.commit()
    flights = Flight.query.filter().all()
    print(len(flights))
    
if __name__ == '__main__':
    with app.app_context():
        main()
