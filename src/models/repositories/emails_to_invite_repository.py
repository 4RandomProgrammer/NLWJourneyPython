from typing import List, Tuple

import psycopg2


class EmailsToInviteRepository:
	def __init__(self, conn: psycopg2.extensions.connection) -> None:
		self.__conn = conn

	def registry_email(self, emails_infos: dict) -> None:
		cursor = self.__conn.cursor()
		query = """
                INSERT INTO "NLWJourney".emails_to_invite
                    (id, trip_id, email)
                VALUES ('%(id)s', '%(trip_id)s','%(email)s')
        """ % (
			emails_infos
		)
		cursor.execute(query)
		self.__conn.commit()

	def find_emails_from_trip(self, trip_id: str) -> List[Tuple]:
		cursor = self.__conn.cursor()

		query = f"""SELECT * FROM "NLWJourney".emails_to_invite WHERE trip_id = '{trip_id}'"""
		cursor.execute(query)
		emails = cursor.fetchall()

		return emails
