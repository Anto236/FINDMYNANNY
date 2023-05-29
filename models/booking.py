#!/usr/bin/python
""" holds class Booking"""
import models
from models.base_model import BaseModel, Base
from models.family import Family
from models.nanny import Nanny
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime


class Booking(BaseModel, Base):
    """Representation of a booking"""

    __tablename__ = 'bookings'
    family_id = Column(String(60), ForeignKey('families.id'), nullable=False)
    nanny_id = Column(String(60), ForeignKey('nannies.id'), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    job_description = Column(String(1024), nullable=False)
    status = Column(String(60), nullable=False, default="pending")

    def __init__(self, *args, **kwargs):
        """Initializes booking"""
        super().__init__(*args, **kwargs)

    @property
    def state(self):
        """loads status options"""
        return self.status

    @state.setter
    def state(self, value):
        """sets status"""
        options = ["pending", "accepted", "rejected"]
        if value in options:
            self.state = value
