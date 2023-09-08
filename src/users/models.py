class User(Base):

    __tablename__: str = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)
    email = Column(String, primary_key=True, unique=True)
    name = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
