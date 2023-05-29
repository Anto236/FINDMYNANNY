#!/usr/bin/python3
""" holds class family """

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from hashlib import md5


class Family(BaseModel, Base):
    """Representation of a family"""

    __tablename__ = 'families'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    address = Column(String(128), nullable=False)
    contact_number = Column(String(20), nullable=False)
    preferred_payment_method = Column(String(128), nullable=False)
    reviews = relationship("Review")

    def __init__(self, *args, **kwargs):
        """Initializes family"""
        super().__init__(*args, **kwargs)

    def create_booking(self, nanny, start_date, end_date, job_description):
        """
        Creates a booking with the specified nanny,
        dates, and job description
        """
        from models.booking import Booking
        booking = Booking(start_date=start_date, end_date=end_date,
                          family=self, nanny=nanny,
                          job_description=job_description)
        booking.save()
        return booking

    def create_review(self, nanny, rating, comments, review_date):
        """Creates a review for the specified nanny"""
        from models.review import Review
        review = Review(family=self, nanny=nanny, rating=rating,
                        comments=None, review_date=None)

        if comments is not None:
            review.comments = comments

        if review_date is not None:
            review.review_date = review_date

        review.save()
        return review

    def __setattr__(self, name, value):
        """Sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
