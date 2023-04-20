from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref
from datetime import datetime
from enum import IntEnum
import bcrypt

Base = declarative_base()

class TypeTask(IntEnum):
    ZIP = 1
    TAR_GZ  = 2
    TAR_BZ2= 3

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer(), primary_key=True)
    type_task = Column(Integer(), nullable=False)
    status = Column(Boolean(), default=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    file_id = Column(Integer(), ForeignKey('file.id'))
    user_id = Column(Integer(), ForeignKey('user.id'))

class File(Base):
    __tablename__ = 'file'
    id = Column(Integer(), primary_key=True)
    path = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    dir = Column(String(), nullable=False)
    user_id = Column(Integer(), ForeignKey('user.id'))
    tasks = relationship('Task', backref='file')

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(), nullable=False)
    files = relationship('File', backref='user')
    tasks = relationship('Task', backref='user')

    def hash_password(self):
        self.password =  bcrypt.hashpw( self.password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))