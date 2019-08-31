from contextlib import contextmanager

from flask import Flask
from flask import render_template
from flask import request

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# dialect+driver://username:password@host:port/database
engine = create_engine('postgresql+psycopg2://aolop:notexposedongithub@db:5432/paolosdb', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)


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

    # todo: Add unique constraint on name probably

    id = Column(Integer, primary_key=True)
    name = Column(String)
    verysecretsecret = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    birthday = Column(Integer)

Base.metadata.create_all(engine)



app = Flask(__name__)


@app.route('/')
def paolo_is_here():
    return render_template('hello.html')

@app.route('/log', methods=['GET', 'POST'])
def write_log():
    if request.method == 'POST':
        if request.is_json:
            print(request.json)
        else:
            print(request.data)
        return "What am I doing\n"
    else:
        return "Only POST for now...\n"



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
        latitude=41.795363,
        longitude=-87.578011,
    )

    with session_scope() as session:
        session.add_all([flamingo, cove, tadpoles])

add_some_stuff()
print("Tada")
