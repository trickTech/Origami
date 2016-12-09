from sqlalchemy import Column, Integer, String

from database import Base


class Server(Base):
    """
    The machines table
    """
    __tablename__ = 'servers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    server_name = Column(String(64), )
    ip = Column(String(40))
    login_user = Column(String(30))
    hardware = Column(String(65535))

    def __repr__(self):
        return "<Machine %r, ip: %r, login_user: %r>" % (self.server_name, self.ip, self.login_user)
