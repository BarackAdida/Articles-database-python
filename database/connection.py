from sqlalchemy import create_engine

# Define your database URL
DB_URL = 'sqlite:///path/to/your/database.db'

# Create the database engine
engine = create_engine(DB_URL, echo=True)  # Set echo=True for debugging

# Create a connection object
db = engine.connect()
