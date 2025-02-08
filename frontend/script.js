// function to get all games from the API
async function getGame() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/games');
        const gamesList = document.getElementById('games-list');
        gamesList.innerHTML = ''; // Clear existing list

        response.data.games.forEach(game => {
            gamesList.innerHTML += `
                <div class="game-card">
                    <h3>${game.title}</h3>
                    <p>Price: ${game.price}</p>
                    <p>Genre: ${game.Genre}</p>
                    <p>Quantity ${game.Quantity}</p>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching games:', error);
        alert('Failed to load games');
    }
}

// function to add a new game to the database
async function addGame() {
    const title = document.getElementById('game-title').value;
    const Genre = document.getElementById('game-Genre').value;
    const price = parseInt(document.getElementById('game-price').value);
    const Quantity = parseInt(document.getElementById('game-Quantity').value);

    try {
        await axios.post('http://127.0.0.1:5000/games', {
            title: title,
            Genre: Genre,
            price: price,
            Quantity: Quantity
        });

        // Clear form fields
        document.getElementById('game-title').value = '';
        document.getElementById('game-Genre').value = '';
        document.getElementById('game-price').value = '';
        document.getElementById('game-Quantity').value = '';

        // Refresh the games list
        getGame();

        alert('game added successfully!');
    } catch (error) {
        console.error('Error adding game:', error);
        console.log(error.response?.data);
        alert('Failed to add game');
    }
}
async function deleteGame() {
    const title = document.getElementById('game-title').value;

    try {
        await axios.delete('http://127.0.0.1:5000/games?title='+title);

        // Clear form fields
        document.getElementById('game-title').value = '';

        // Refresh the customers list
        getGame();

        alert('Game deleted successfully!');
    } catch (error) {
        console.error('Error deleting game:', error);
        console.log(error.response?.data);  // Log error details
        alert('Failed to delete game');
    }
}

async function addCustomer() {
    const username = document.getElementById('customer-username').value;
    const email = document.getElementById('customer-email').value;
    const phone_number = document.getElementById('customer-phone_number').value;


    try {
        await axios.post('http://127.0.0.1:5000/customers', {
            username: username,
            email : email,
            phone_number : phone_number

        });

        // Clear form fields
        document.getElementById('customer-username').value = '';
        document.getElementById('customer-email').value = '';
        document.getElementById('customer-phone_number').value = '';

        // Refresh the customers list
        getCustomers();

        alert('Customer added successfully!');
    } catch (error) {
        console.error('Error adding customer:', error);
        console.log(error.response?.data);  // Log error details
        alert('Failed to add customer');
    }
}

async function deleteCustomer() {
    const username = document.getElementById('customer-username').value;

    try {
        await axios.delete('http://127.0.0.1:5000/customers?username='+username);

        // Clear form fields
        document.getElementById('customer-username').value = '';
        document.getElementById('customer-email').value = '';
        document.getElementById('customer-phone_number').value = '';

        // Refresh the customers list
        getCustomers();

        alert('Customer deleted successfully!');
    } catch (error) {
        console.error('Error deleting customer:', error);
        console.log(error.response?.data);  // Log error details
        alert('Failed to delete customer');
    }
}

async function getCustomers() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/customers');  // Fetch customers from backend
        const customersList = document.getElementById('customer-list');  // Target the HTML element
        customersList.innerHTML = '';  // Clear existing list

        response.data.customers.forEach(customer => {
            customersList.innerHTML += `
                <div class="game-card">
                    <h3>Username: ${customer.username}</h3>
                    <h3>Email: ${customer.email}</h3>
                    <h3>Phone_Number: ${customer.phone_number}</h3>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching customers:', error);
        alert('Failed to load customers');
    }
}


async function addUser() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        await axios.post('http://127.0.0.1:5000/user', {
            username: username,
            password : password
        });

        // Clear form fields
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';

        alert('User added successfully!');
    } catch (error) {
        console.error('Error adding User:', error);
        console.log(error.response?.data);  // Log error details
        alert('Failed to add User');
    }
}

async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        await axios.post('http://127.0.0.1:5000/login', {
            username: username,
            password : password
        });

        // Clear form fields
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';

        document.getElementById('main-section').classList.remove("hidden");
        document.getElementById('auth-section').classList.add("hidden");

    } catch (error) {
        console.error('Error to log in User:', error);
        console.log(error.response?.data);  // Log error details
        alert('Failed to log in User');
    }
}

async function logout() {

        document.getElementById('auth-section').classList.remove("hidden");
        document.getElementById('main-section').classList.add("hidden");
}

async function addLoan() {
    const customer_username = document.getElementById('loan-customer').value;
    const game_title = document.getElementById('loan-game-title').value;
    const return_date = document.getElementById('loan-return-date').value;


    try {
        await axios.post('http://127.0.0.1:5000/loans', {
            customer_username: customer_username,
            game_title : game_title,
            return_date : return_date

        });

        // Clear form fields
        document.getElementById('loan-customer').value = '';
        document.getElementById('loan-game-title').value = '';
        document.getElementById('loan-return-date').value = '';

        // Refresh the customers list
        getLoans();
        getGame();

        alert('Loan added successfully!');
    } catch (error) {
        console.error('Error adding loan:', error);
        console.log(error.response?.data);  // Log error details
        alert('Failed to add loan');
    }
}

async function deleteLoan() {
    const customer_username = document.getElementById('loan-customer').value;
    const game_title = document.getElementById('loan-game-title').value;

    try {
        await axios.delete('http://127.0.0.1:5000/loans?customer_username='+customer_username+"&game_title="+game_title);

        // Clear form fields
        document.getElementById('loan-customer').value = '';
        document.getElementById('loan-game-title').value = '';

        // Refresh the customers list
        getLoans();
        getGame();

        alert('Loan deleted successfully!');
    } catch (error) {
        console.error('Error deleting loan:', error);
        console.log(error.response?.data);  // Log error details
        alert('Failed to delete loan');
    }
}

async function getLoans() {
    try {
        const response = await axios.get('http://127.0.0.1:5000/loans');  // Fetch customers from backend
        const loansList = document.getElementById('loaned-games-list');  // Target the HTML element
        loansList.innerHTML = '';  // Clear existing list

        response.data.loans.forEach(loan => {
            loansList.innerHTML += `
                <div class="game-card">
                    <h3>Customer: ${loan.customer_username}</h3>
                    <h3>Game: ${loan.game_title}</h3>
                    <h3>Loan Date: ${loan.loan_date}</h3>
                    <h3>Return Date: ${loan.return_date}</h3>
                </div>
            `;
        });
    } catch (error) {
        console.error('Error fetching loans:', error);
        alert('Failed to load loans');
    }
}

//קוראת ל URL של הפונקציות Views
// Load all games when page loads
document.addEventListener('DOMContentLoaded', getGame);
document.addEventListener('DOMContentLoaded', getCustomers);
document.addEventListener('DOMContentLoaded', getLoans);
