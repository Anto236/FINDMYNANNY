#!/usr/bin/python
""" holds class Nanny"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from models.booking import Booking
from models.city import City


class Nanny(BaseModel, Base):
    """Representation of a nanny"""

    __tablename__ = 'nannies'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    address = Column(String(128), nullable=False)
    contact_number = Column(String(20), nullable=False)
    hourly_rate = Column(String(128), nullable=False)
    years_of_experience = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
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
