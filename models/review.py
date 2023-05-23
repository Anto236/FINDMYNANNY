#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Representation of a review"""

    __tablename__ = 'reviews'
    review_id = Column(String(60), primary_key=True)
    family_id = Column(String(60), ForeignKey('families.id'), nullable=False)
    nanny_id = Column(String(60), ForeignKey('nannies.id'), nullable=False)
    rating = Column(String(10), nullable=False)
    comments = Column(String(1024), nullable=False)
    review_date = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes review"""
        super().__init__(*args, **kwargs)
