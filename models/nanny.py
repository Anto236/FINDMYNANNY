#!/usr/bin/python
""" holds class Nanny"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from hashlib import md5


class Nanny(BaseModel, Base):
    """Representation of a nanny"""

    __tablename__ = 'nannies'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    address = Column(String(128), nullable=False)
    contact_number = Column(String(20), nullable=False)
    hourly_rate = Column(String(128), nullable=False)
    years_of_experience = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    image = Column(LargeBinary)
    city = relationship("City")

    def __init__(self, *args, **kwargs):
        """Initializes nanny"""
        super().__init__(*args, **kwargs)

    def accept_booking(self, booking):
        """Accepts the specified booking"""
        booking.status = 'accepted'
        booking.save()

    def reject_booking(self, booking):
        """Rejects the specified booking"""
        booking.status = 'rejected'
        booking.save()

    def __setattr__(self, name, value):
        """Sets a password with md5 encryption"""
        if name == "password":
            value = md6(value.encode()).hexdigest()
        super().__setattr__(name, value)
