from datetime import datetime, timedelta
import	pytest

from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

class TestParticipantsRepository:
    def test_registry_participants(self, trip_id, participant_id, email_id, result_participant):
        conn = db_connection_handler.get_connection()

        trip_repository = TripsRepository(conn)
        participants_repository = ParticipantsRepository(conn)
        emails_to_invite_repository = EmailsToInviteRepository(conn)

        trips_infos = {
			"id": trip_id,
			"destination": "Osasco",
			"start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
			"end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
			"owner_name": "Osvaldo",
			"owner_email": "osvaldo@email.com",
		}

        participant_infos = {
            "id":participant_id,
            "trip_id":trip_id,
            "emails_to_invite_id":email_id,
            "name":"Heraldo",
        }

        email_info = {
			"id": email_id,
			"trip_id": trip_id,
			"email": "heraldo@email.com",
		}

        trip_repository.create_trip(trips_infos=trips_infos)
        emails_to_invite_repository.registry_email(emails_infos=email_info)
        participants_repository.registry_participants(participant_info=participant_infos)
        participants = participants_repository.find_participants_from_trip(trip_id)
        
        assert result_participant == participants

    
    def test_find_participants_from_trip(self, trip_id, participant_id, email_id, result_participant):
        conn = db_connection_handler.get_connection()

        trip_repository = TripsRepository(conn)
        participants_repository = ParticipantsRepository(conn)
        emails_to_invite_repository = EmailsToInviteRepository(conn)

        trips_infos = {
            "id": trip_id,
            "destination": "Osasco",
            "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
            "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
            "owner_name": "Osvaldo",
            "owner_email": "osvaldo@email.com",
        }

        participant_infos = {
            "id":participant_id,
            "trip_id":trip_id,
            "emails_to_invite_id":email_id,
            "name":"Heraldo",
        }

        email_info = {
            "id": email_id,
            "trip_id": trip_id,
            "email": "heraldo@email.com",
        }

        trip_repository.create_trip(trips_infos=trips_infos)
        emails_to_invite_repository.registry_email(emails_infos=email_info)
        participants_repository.registry_participants(participant_info=participant_infos)
        participants = participants_repository.find_participants_from_trip(trip_id)

        assert isinstance(participants, list)
        assert isinstance(participants[0], tuple)
        assert result_participant == participants

    def test_cofirm_participant(self, trip_id, participant_id, email_id, result_confirmed_participant):
        conn = db_connection_handler.get_connection()

        trip_repository = TripsRepository(conn)
        participants_repository = ParticipantsRepository(conn)
        emails_to_invite_repository = EmailsToInviteRepository(conn)

        trips_infos = {
			"id": trip_id,
			"destination": "Osasco",
			"start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
			"end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
			"owner_name": "Osvaldo",
			"owner_email": "osvaldo@email.com",
		}

        participant_infos = {
            "id":participant_id,
            "trip_id":trip_id,
            "emails_to_invite_id":email_id,
            "name":"Heraldo",
        }

        email_info = {
			"id": email_id,
			"trip_id": trip_id,
			"email": "heraldo@email.com",
		}

        trip_repository.create_trip(trips_infos=trips_infos)
        emails_to_invite_repository.registry_email(emails_infos=email_info)
        participants_repository.registry_participants(participant_info=participant_infos)
        participants_repository.update_participant_status(participant_id)
        participants = participants_repository.find_participants_from_trip(trip_id)

        assert result_confirmed_participant == participants
