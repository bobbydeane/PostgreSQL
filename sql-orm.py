from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinnook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

#opens an actual session by calling the Session() subclasss defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)



