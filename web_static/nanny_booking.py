from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.booking import Booking

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'fmn_dev',
    'password': 'fmn_dev_pwd',
    'database': 'findmynanny'
}

engine = create_engine(
    'mysql+mysqldb://{user}:{password}@{host}/{database}'.format(**db_config))
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/booking_details', methods=['GET'])
def render_booking_details():
    # Fetch the booking details from the database
    booking = session.query(Booking).first()

    return render_template('booking_details.html', booking=booking)


@app.route('/accept', methods=['POST'])
def accept_booking():
    # Perform actions to accept the booking
    # You can access the booking_id using request.form.get('booking_id')
    # Update the status of the booking to 'Accepted'
    booking_id = request.form.get('booking_id')
    booking = session.query(Booking).filter_by(id=booking_id).first()
    if booking:
        booking.status = 'Accepted'
        session.commit()

    return redirect('/booking_details')


@app.route('/reject', methods=['POST'])
def reject_booking():
    # Perform actions to reject the booking
    # You can access the booking_id using request.form.get('booking_id')
    # Update the status of the booking to 'Rejected'
    booking_id = request.form.get('booking_id')
    booking = session.query(Booking).filter_by(id=booking_id).first()
    if booking:
        booking.status = 'Rejected'
        session.commit()

    return redirect('/booking_details')


if __name__ == '__main__':
    app.run()


# <!-- booking_details.html -->

# <!-- ... (previous HTML code) -->

# <section class="booking-creation">
#     <h2>Booking Details</h2>
#     <ul>
#         <li>Start Date: <span id="start_date">{{ booking.start_date }}</span></li>
#         <li>End Date: <span id="end_date">{{ booking.end_date }}</span></li>
#         <li>Job Description: <span id="job_description">{{ booking.job_description }}</span></li>
#         <li>Status: <span id="status">{{ booking.status if booking else 'Pending' }}</span></li>
#     </ul>

#     {% if booking and booking.status == 'Pending' %}
#     <div class="buttons">
#         <form action="/accept" method="post">
#             <input type="hidden" name="booking_id" value="{{ booking.id }}">
#             <button type="submit" id="accept_button">Accept</button>
#         </form>
#         <form action="/reject" method="post">
#             <input type="hidden" name="booking_id" value="{{ booking.id }}">
#             <button type="submit" id="reject_button">Reject</button>
#         </form>
#     </div>
#     {% endif %}
# </section>

# <!-- ... (remaining HTML code) -->
