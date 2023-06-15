from flask import Flask, request, redirect
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel

app = Flask(__name__)

# Connect to the database
db_config = {
    'host': 'localhost',
    'user': 'fmn_dev',
    'password': 'fmn_dev_pwd',
    'database': 'findmynanny'
}
db = DBStorage(**db_config)
db.reload()


@app.route('/', methods=['POST'])
def authenticate():
    email = request.form.get('email')
    password = request.form.get('password')
    role = request.form.get('role')

    try:
        # Retrieve user from the database
        users = db.get_all(BaseModel)
        user = next((user for user in users if user.email ==
                    email and user.password == password and user.role == role), None)

        if user:
            # Authentication successful, redirect the user to the appropriate page based on the role
            if role == 'nanny':
                return redirect('/nanny_page')
            elif role == 'family':
                return redirect('/family_page')
        else:
            # If authentication fails, display an error message
            return "Authentication failed"

    except Exception as e:
        # Display error message
        return "Error: {}".format(e)


if __name__ == '__main__':
    app.run()
