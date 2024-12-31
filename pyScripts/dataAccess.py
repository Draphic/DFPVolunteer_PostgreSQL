import os
import psycopg2

#Function to load env from .env
def load_env(file_path):
    with open(file_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

load_env('DFPostgres.env')

postgres_user = 'postgres'
postgres_password = os.getenv('POSTGRES_PASSWORD')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="volunteering",
    user=postgres_user,
    password=postgres_password,
    host="localhost",
    port="5401"
)
cur = conn.cursor()


# List all tables in the 'volunteering' schema
cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'volunteering';
""")

# Fetch and print each table in volunteering
tables = cur.fetchall()
print("Tables in the 'volunteering' schema:")
for table in tables:
    print(table[0])


# Fetch and print data from each table
for table in tables:
    print(f"\nData in table {table[0]}:")
    cur.execute(f"SELECT * FROM volunteering.{table[0]};")
    rows = cur.fetchall()
    for row in rows:
        print(row)

print()

# Insert new volunteer data (optional)
cur.execute("""
    INSERT INTO volunteering.volunteers (
        sign_up_time, first_name, last_name, email, phone_number, organization
    ) VALUES (
        '2024-12-09 20:00:00', 'John', 'Doe', 'john.doe@example.com', 1234567890, 'Example Org'
    ) RETURNING volunteer_id;
""")
volunteer_id = cur.fetchone()[0]
cur.execute("""
    INSERT INTO volunteering.sign_in_responses (
        volunteer_id, sign_in, sign_out
    ) VALUES (
        %s, '2024-12-09 21:00:00', '2024-12-09 22:00:00'
    );
""", (volunteer_id,))
conn.commit()

print("Fetching data again after insertion")

for table in tables:
    print(f"\nData in table {table[0]}:")
    cur.execute(f"SELECT * FROM volunteering.{table[0]};")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Close the connection
cur.close()
conn.close()
