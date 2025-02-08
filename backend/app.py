from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from models import db
from models.user import User
from models.game import Game
from models.customers import Customer
from models.loans import Loan



app = Flask(__name__)  # - create a flask instance
# - enable all routes, allow requests from anywhere (optional - not recommended for security)
CORS(app, resources={r"/*": {"origins": "*"}})


# Specifies the database connection URL. In this case, it's creating a SQLite database
# named 'library.db' in your project directory. The three slashes '///' indicate a
# relative path from the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)  # initializes the databsewith the flask application


# this is a decorator from the flask module to define a route for for adding a game, supporting POST requests.(check the decorator summary i sent you and also the exercises)
@app.route('/games', methods=['POST'])
def add_game():
    data = request.json  # this is parsing the JSON data from the request body
    print("Received data:", data)
    new_game = Game(
        title=data['title'],  # Set the title of the new game.
        price=data['price'],  # Set the author of the new game.
        Genre=data['Genre'],
        # Set the types(fantasy, thriller, etc...) of the new game.
        Quantity=data['Quantity']
        # add other if needed...
    )
    db.session.add(new_game)  # add the bew game to the database session
    db.session.commit()  # commit the session to save in the database
    return jsonify({'message': 'game added to database.'}), 201


# a decorator to Define a new route that handles GET requests
@app.route('/games', methods=['GET'])
def get_games():
    try:
        games = Game.query.all()                    # Get all the games from the database
        # Create empty list to store formatted game data we get from the database
        games_list = []

        for game in games:                         # Loop through each game from database
            game_data = {                          # Create a dictionary for each game
                'id': game.id,
                'title': game.title,
                'price': game.price,
                'Genre': game.Genre,
                'Quantity': game.Quantity
            }
            # Add the iterated game dictionary to our list
            games_list.append(game_data)

        return jsonify({                           # Return JSON response
            'message': 'games retrieved successfully',
            'games': games_list
        }), 200

    except Exception as e:
        return jsonify({
            'error': 'Failed to retrieve games',
            'message': str(e)
        }), 500


@app.route('/games', methods=['DELETE'])
def delete_game():
    try:
        title = request.args["title"]  # Get JSON data from request
        print("Received data:", title)

        # Ensure both fields exist
        if not title:
            return jsonify({'error': 'Title is required'}), 400

        # Check if username already exists
        my_game = Game.query.filter_by(title=title).first()
        if not my_game:
            return jsonify({'error': 'Title does not exist'}), 409  # 409 Conflict

        # Create and store the new customer
        db.session.delete(my_game)
        db.session.commit()

        return jsonify({'message': 'Game deleted successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete game', 'message': str(e)}), 500


@app.route('/customers', methods=['POST'])
def add_customer():
    try:
        data = request.json  # Get JSON data from request
        print("Received data:", data)

        username = data.get('username')
        email = data.get('email')
        phone_number = data.get('phone_number')
        # Ensure both fields exist
        if not username or not email or not phone_number:
            return jsonify({'error': 'All fields are required'}), 400

        # Check if username already exists
        if Customer.query.get(username):
            return jsonify({'error': 'Username already exists'}), 409  # 409 Conflict

        # Create and store the new customer
        new_customer = Customer(username=username,email=email,phone_number=phone_number)
        db.session.add(new_customer)
        db.session.commit()

        return jsonify({'message': 'Customer added successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to add customer', 'message': str(e)}), 500


@app.route('/customers', methods=['DELETE'])
def delete_customer():
    try:
        username = request.args["username"]  # Get JSON data from request
        print("Received data:", username)

        # Ensure both fields exist
        if not username:
            return jsonify({'error': 'Username is required'}), 400

        # Check if username already exists
        my_customer = Customer.query.get(username)
        if not my_customer:
            return jsonify({'error': 'Username does not exist'}), 409  # 409 Conflict

        # Create and store the new customer
        db.session.delete(my_customer)
        db.session.commit()

        return jsonify({'message': 'Customer deleted successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete customer', 'message': str(e)}), 500


@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()  # Fetch all customers

        customers_list = [
            {
                'username': customer.username,
                'email':customer.email,
                'phone_number' : customer.phone_number
            }
            for customer in customers
        ]

        return jsonify({
            'message': 'Customers retrieved successfully',
            'customers': customers_list
        }), 200

    except Exception as e:
        return jsonify({'error': 'Failed to retrieve customers', 'message': str(e)}), 500


@app.route('/user', methods=['POST'])
def add_user():
    try:
        data = request.json  # Get JSON data from request
        print("Received data:", data)

        username = data.get('username')
        password = data.get('password')
        # Ensure both fields exist
        if not username or not password:
            return jsonify({'error': 'All fields are required'}), 400

        # Check if username already exists
        if User.query.get(username):
            return jsonify({'error': 'Username already exists'}), 409  # 409 Conflict

        # Create and store the new customer
        new_user = User(username=username,password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User added successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to add User', 'message': str(e)}), 500


@app.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json  # Get JSON data from request
        print("Received data:", data)

        username = data.get('username')
        password = data.get('password')
        # Ensure both fields exist
        if not username or not password:
            return jsonify({'error': 'All fields are required'}), 400

        # Check if username already exists
        user = User.query.filter_by(username=username).first()
        # Check if user exists and verify password
        if not user or not user.password == password:
            return jsonify({'error': 'Invalid username or password'}), 401  # 401 Unauthorized


        return jsonify({'message': 'User logged in successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to log in User', 'message': str(e)}), 500


@app.route('/loans', methods=['POST'])
def add_loan():
    try:
        data = request.json  # Get JSON data from request
        print("Received data:", data)

        customer_username = data.get('customer_username')
        game_title = data.get('game_title')
        return_date = data.get('return_date')

        # Ensure all fields exist
        if not customer_username or not game_title or not return_date:
            return jsonify({'error': 'All fields are required'}), 400

        # Convert return_date to datetime
        try:
            return_date = datetime.strptime(return_date, "%Y-%m-%d")
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

        # Get current timestamp for loan date
        loan_date = datetime.now()

        # Check if the game exists and has available copies
        game = Game.query.filter_by(title=game_title).first()
        if not game:
            return jsonify({'error': 'Game not found'}), 404  # Not Found

        if game.Quantity <= 0:
            return jsonify({'error': 'No copies available for loan'}), 409  # Conflict

        # Loan the game and decrease quantity
        new_loan = Loan(
            customer_username=customer_username,
            game_title=game_title,
            loan_date=loan_date,  # Store current timestamp
            return_date=return_date
        )
        game.Quantity -= 1  # Reduce available copies

        db.session.add(new_loan)
        db.session.commit()

        return jsonify({'message': 'Loan added successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to add loan', 'message': str(e)}), 500


@app.route('/loans', methods=['DELETE'])
def delete_loan():
    try:
        customer_username = request.args.get("customer_username")
        game_title = request.args.get("game_title")

        # Ensure both fields exist
        if not customer_username or not game_title:
            return jsonify({'error': 'Both customer_username and game_title are required'}), 400

        # Find the loan
        print("**********", customer_username , " , ",game_title )
        loan = Loan.query.filter_by(customer_username=customer_username, game_title=game_title).first()
        if not loan:
            return jsonify({'error': 'Loan not found'}), 404  # Not Found

        # Find the game and increase quantity
        game = Game.query.filter_by(title=game_title).first()
        if game:
            game.Quantity += 1  # Increase quantity when returned

        # Delete the loan record
        db.session.delete(loan)
        db.session.commit()

        return jsonify({'message': 'Loan returned successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to return loan', 'message': str(e)}), 500


@app.route('/loans', methods=['GET'])
def get_loans():
    try:
        loans = Loan.query.all()  # Fetch all loans

        loans_list = [
            {
                'customer_username': loan.customer_username,
                'game_title': loan.game_title,
                'loan_date': loan.loan_date.strftime("%Y-%m-%d %H:%M:%S"),  # Format datetime
                'return_date': loan.return_date.strftime("%Y-%m-%d %H:%M:%S")  # Format datetime
            }
            for loan in loans
        ]

        return jsonify({
            'message': 'Loans retrieved successfully',
            'loans': loans_list
        }), 200

    except Exception as e:
        return jsonify({'error': 'Failed to retrieve loans', 'message': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():

        db.reflect()  # Reflect existing tables
        db.metadata.drop_all(bind=db.engine)  # Drop all tables
        db.session.commit()
        db.create_all()
    app.run(debug=True)  # start the flask application in debug mode

