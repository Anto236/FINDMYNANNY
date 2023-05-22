#!/usr/bin/python
""" holds class jobs"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Job(BaseModel, Base):
    """Representation of a job posting"""

    __tablename__ = 'jobs'
    job_id = Column(String(60), primary_key=True)
    family_id = Column(String(60), ForeignKey('families.id'), nullable=False)
    nanny_id = Column(String(60), ForeignKey('nannies.id'), nullable=False)
    start_date = Column(String(60), nullable=False)
    end_date = Column(String(60), nullable=False)
    job_description = Column(String(1024), nullable=False)
    is_accepted = Column(String(10), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes job"""
        super().__init__(*args, **kwargs)
