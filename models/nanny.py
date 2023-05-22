#!/usr/bin/python
""" holds class Nanny"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Nanny(BaseModel, Base):
    """Representation of a nanny"""

    __tablename__ = 'nannies'
    nanny_id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    address = Column(String(128), nullable=False)
    contact_number = Column(String(20), nullable=False)
    hourly_rate = Column(String(128), nullable=False)
    years_of_experience = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes nanny"""
        super().__init__(*args, **kwargs)
