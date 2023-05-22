#!/usr/bin/python3
""" holds class family """

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Family(BaseModel, Base):
    """Representation of a family"""

    __tablename__ = 'families'
    family_id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    address = Column(String(128), nullable=False)
    contact_number = Column(String(20), nullable=False)
    preferred_payment_method = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes family"""
        super().__init__(*args, **kwargs)
