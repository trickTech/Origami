from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from origami.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bing=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from origami.deploy.model import Server, App
    Base.metadata.create_all(bind=engine)
