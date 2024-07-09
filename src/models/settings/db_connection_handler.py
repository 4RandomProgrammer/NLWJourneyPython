import psycopg2


class DbConnectionHandler:
	def __init__(self) -> None:
		self.__connection_string = "postgres"
		self.__conn = None

	def connect(self) -> None:
		conn = psycopg2.connect(
			database=self.__connection_string,
			user="postgres",
			password="root",
			host="localhost",
			port="5432",
		)
		self.__conn = conn

	def get_connection(self) -> psycopg2.extensions.connection:
		return self.__conn


db_connection_handler = DbConnectionHandler()
