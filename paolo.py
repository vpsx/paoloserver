from contextlib import contextmanager
import logging

from flask import Flask
from flask import render_template
from flask import request
from flask import json

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# dialect+driver://username:password@host:port/database
engine = create_engine('postgresql+psycopg2://aolop@db:5432/paolosdb', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

logging.basicConfig(
    #filename='logs.txt',
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s: \n    %(message)s\n',
    datefmt='%a %Y-%b-%d %H:%M:%S %Z',
)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

class Paolo(Base):
    __tablename__ = 'paolos'

    name = Column(String, primary_key=True)
    verysecretsecret = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    birthday = Column(Integer)
    lastseen = Column(String)

Base.metadata.create_all(engine)



app = Flask(__name__)


@app.route('/')
def paolo_is_here():
    return render_template('hello.html')

@app.route('/log', methods=['GET', 'POST'])
def write_log():
    if request.method == 'POST':
        if request.is_json:
            logging.info(
                "Log endpoint, json. Received: {json}"
                .format(json=request.json)
            )
            return request.json
        else:
            logging.info(
                "Log endpoint, not json. Received: {data}"
                .format(data=request.data)
            )
            return request.data
    else:
        return "Only POST for now...\n"

@app.route('/givelocation', methods=['POST'])
def give_location():
    # I THINK this could do with some codes MAYBE
    if request.method != 'POST':
        return "Only POST for now...\n"
    if not request.is_json:
        return "Plz give json...\n"
    try:
        name = request.json["Name"]
        timestamp = request.json["Timestamp"]
        latitude = request.json["Latitude"]
        longitude = request.json["Longitude"]
    except: # This is not even the MVP, okay?
        return "U give bad json...\n"
    with session_scope() as session:
        person = session.query(Paolo).filter(Paolo.name==name).one_or_none()
        if not person:
            newperson = Paolo(
                name=name,
                lastseen=timestamp,
                latitude=latitude,
                longitude=longitude,
            )
            session.add(newperson)
            return "U not exist... I creat.\n"
        person.latitude = latitude
        person.longitude = longitude
        person.lastseen = timestamp
    return "OK, ...probably\n"

@app.route('/getlocation', methods=['GET'])
def get_location():
    # codes
    name = request.args.get('name', None)
    if not name:
        return "Plz give name\n"
    with session_scope() as session:
        person = session.query(Paolo).filter(Paolo.name==name).one_or_none()
        if not person:
            return "This person not exist\n"
        return json.jsonify(
            name=person.name,
            lastseen=person.lastseen,
            latitude=person.latitude,
            longitude=person.longitude,
        )


def add_some_stuff():

    flamingo = Paolo(
        name='flamingo',
        verysecretsecret='onthelake',
        latitude=41.794722,
        longitude=-87.580833,
        birthday=19270000,
    )

    cove = Paolo(
        name='cove',
        latitude=41.79543,
        longitude=-87.5819805,
    )

    tadpoles = Paolo(
        name='tadpoles',
        latitude=41.795351,
        longitude=-87.577861,
    )

    with session_scope() as session:
        session.add_all([flamingo, cove, tadpoles])

try:
    add_some_stuff()
except:
    logging.info("Didn't add random stuff to db")
