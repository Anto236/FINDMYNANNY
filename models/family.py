#!/usr/bin/python3
""" holds class family """

import models
from models.base_model import BaseModel, Base
from models.user import User
from models.booking import Booking
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Family(BaseModel, Base):
    """Representation of a family"""

    __tablename__ = 'families'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
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
        booking = Booking(start_date=start_date, end_date=end_date,
                          family=self, nanny=nanny,
                          job_description=job_description)
        booking.save()
        return booking

    def create_review(self, nanny, rating, comments, review_date):
        """Creates a review for the specified nanny"""
        review = Review(family=self, nanny=nanny, rating=rating,
                        comments=None, review_date=None)

        if comments is not None:
            review.comments = comments

        if review_date is not None:
            review.review_date = review_date

        review.save()
        return review
