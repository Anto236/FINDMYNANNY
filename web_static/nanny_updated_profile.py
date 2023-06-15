from flask import Flask, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.nanny import Nanny
from hashlib import md5

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'fmn_dev',
    'password': 'fmn_dev_pwd',
    'database': 'findmynanny'
}

# Create SQLAlchemy engine and session
engine = create_engine(
    'mysql+mysqldb://{user}:{password}@{host}/{database}'.format(**db_config))
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/', methods=['POST'])
def update_data():
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    address = request.form.get('address')
    contact_number = request.form.get('contact_number')
    hourly_rate = request.form.get('hourly_rate')
    years_of_experience = request.form.get('years_of_experience')
    city = request.form.get('city')

    try:
        # Retrieve the Nanny object by email
        nanny = session.query(Nanny).filter_by(email=email).first()

        # Update Nanny object with the new data
        nanny.password = md5(password.encode()).hexdigest()
        nanny.first_name = first_name
        nanny.last_name = last_name
        nanny.address = address
        nanny.contact_number = contact_number
        nanny.hourly_rate = hourly_rate
        nanny.years_of_experience = years_of_experience
        nanny.city = city

        session.commit()

        # Redirect to nanny_page.html upon successful update
        return redirect('/nanny_page.html')

    except Exception as e:
        # Display error message
        error_message = "Update failed, please try again."
        return error_message


if __name__ == '__main__':
    app.run()
