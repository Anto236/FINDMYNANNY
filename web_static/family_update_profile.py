import hashlib
from flask import Flask, request, redirect
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from models.family import Family

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
    preferred_payment_method = request.form.get('preferred_payment_method')

    try:
        # Hash the password using MD5
        password_hash = hashlib.md5(password.encode()).hexdigest()

        # Retrieve the Family object by email
        family = session.query(Family).filter_by(email=email).first()

        # Update Family object with the new data
        family.password = password_hash
        family.first_name = first_name
        family.last_name = last_name
        family.address = address
        family.contact_number = contact_number
        family.preferred_payment_method = preferred_payment_method

        session.commit()

        # Redirect to family_page.html upon successful update
        return redirect('/family_page.html')

    except exc.SQLAlchemyError as e:
        # Display error message
        error_message = "Update failed, please try again."
        return error_message


if __name__ == '__main__':
    app.run()
