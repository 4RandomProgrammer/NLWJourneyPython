from typing import Dict, List, Tuple
import psycopg2


class ParticipantsRepository:
	def __init__(self, conn: psycopg2.extensions.connection) -> None:
		self.__conn = conn

	def registry_participants(self, participant_info: Dict) -> None:
		cursor = self.__conn.cursor()
		query = """
                INSERT INTO "NLWJourney".participants
                    (id, trip_id, emails_to_invite_id, name)
                VALUES ('%(id)s', '%(trip_id)s','%(emails_to_invite_id)s', '%(name)s')
        """ % (
			participant_info
		)

		cursor.execute(query)
		self.__conn.commit()

	def find_participants_from_trip(self, trip_id: str) -> List[Tuple]:
		cursor = self.__conn.cursor()

		query = f"""
            SELECT p.id, p.name, p.is_confirmed, e.email
            FROM "NLWJourney".participants as p
            JOIN "NLWJourney".emails_to_invite as e
            ON p.emails_to_invite_id = e.id
            WHERE p.trip_id = '{trip_id}'
        """
		cursor.execute(query)
		participants = cursor.fetchall()

		return participants

	def update_participant_status(self, participant_id: str) -> None:
		cursor = self.__conn.cursor()

		query = f"""
            UPDATE "NLWJourney".participants 
                SET is_confirmed = 1
            WHERE 
                id = '{participant_id}'
        """
		cursor.execute(query)

		self.__conn.commit()
