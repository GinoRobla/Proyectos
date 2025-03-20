# SQL Procedures Application

This project is designed to provide a simple command-line interface for managing a sales system database. It allows users to interact with stored procedures for products, clients, and orders.

## Project Structure

```
sql-procedures-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── db
│   │   ├── __init__.py       # Marks the db directory as a package
│   │   └── connection.py      # Handles database connection logic
│   ├── procedures
│   │   ├── __init__.py       # Marks the procedures directory as a package
│   │   ├── products.py        # Functions for product management
│   │   ├── clients.py         # Functions for client management
│   │   └── orders.py          # Functions for order processing
├── requirements.txt           # Lists project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd sql-procedures-app
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Database Connection**:
   Update the `connection.py` file with your database credentials.

4. **Run the Application**:
   Execute the main script:
   ```bash
   python src/main.py
   ```

## Usage

Once the application is running, you will be presented with a menu to choose from various options to manage products, clients, and orders. Follow the prompts to execute the desired stored procedures.

## Contributing

Feel free to submit issues or pull requests for improvements or additional features.