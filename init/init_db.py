import psycopg2

conn = psycopg2.connect(
    database='postgres',
    user="postgres",
    password="root",
    host="localhost",
    port="5432",
)

conn.autocommit = True

cursor = conn.cursor()

CREATE_SCHEMA = 'CREATE SCHEMA IF NOT EXISTS "NLWJourney";'
MONTH_CONFIG = '''SET "NLWJourney".datestyle = 'ISO, MDY';'''

# Open and read the file as a single buffer
fd = open('schema.sql', 'r')
sqlFile = fd.read()
fd.close()

sqlCommands = sqlFile.split(';')

cursor.execute(CREATE_SCHEMA)
cursor.execute(MONTH_CONFIG)

# Execute every command from the input file
for command in sqlCommands:
    try:
        cursor.execute(command)
    except Exception as e:
        print("Command skipped: ", str(e))

conn.close()