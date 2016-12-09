from sqlalchemy import Column, Integer, String

from database import Base


class App(Base):
    """
    The Apps table
    """
    __tablename__ = "apps"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True)
    # owner = Column(Integer)
    # owner_name = Column(String(64))
    git_url = Column(String(255))
    running_on = Column(Integer)
    running_user = Column(String(255))
    deploy_path = Column(String(255), unique=True)
