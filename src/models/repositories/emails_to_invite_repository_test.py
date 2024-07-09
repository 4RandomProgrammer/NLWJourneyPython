import pytest
import uuid
from datetime import datetime, timedelta
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = 'c36025dd-d00c-47a4-bae0-149da977fc7f'

@pytest.mark.skip(reason='Interação com o banco')
def test_registry_email():
	conn = db_connection_handler.get_connection()
	emails_to_invite_repository = EmailsToInviteRepository(conn)

	email_info = {
		"id": str(uuid.uuid4()),
		"trip_id": trip_id,
		"email": 'olamundo@email.com',
	}

	emails_to_invite_repository.registry_email(emails_infos=email_info)

@pytest.mark.skip(reason='Interação com o banco')
def test_find_emaisl_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    
    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print(emails)
