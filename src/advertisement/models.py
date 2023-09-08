class Ad(Base):

    __tablename__: str = 'ads'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    title = Column(String)
    description = Column(String)
    price = Column(Integer)
    is_active = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow())
