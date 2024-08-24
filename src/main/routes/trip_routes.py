from flask import Blueprint, jsonify, request

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activity_finder import ActivityFinder
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder
from src.controllers.participant_confirmer import ParticipantConfirmer
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participants_creator import ParticipantsCreator
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_updater import TripUpdater
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

trip_routes_bp = Blueprint("trip_routes", __name__)


@trip_routes_bp.after_request
def after_request(response):
	header = response.headers
	header["Access-Control-Allow-Origin"] = "*"
	header["Access-Control-Allow-Headers"] = "Content-Type"

	return response


@trip_routes_bp.route("/trips", methods=["POST"])
def create_trip():
	conn = db_connection_handler.get_connection()
	trip_repository = TripsRepository(conn)
	emails_repository = EmailsToInviteRepository(conn)
	controller = TripCreator(trip_repository, emails_repository)

	response = controller.create(request.json)

	return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
	conn = db_connection_handler.get_connection()
	trip_repository = TripsRepository(conn)
	controller = TripFinder(trip_repository)

	response = controller.find_trip_detail(tripId)

	return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
	conn = db_connection_handler.get_connection()
	trip_repository = TripsRepository(conn)
	controller = TripConfirmer(trip_repository)

	response = controller.confirm(tripId)

	return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>/update_date_and_destination", methods=["POST"])
def update_trip_destination_and_date(tripId):
	conn = db_connection_handler.get_connection()
	trip_repository = TripsRepository(conn)
	controller = TripUpdater(trip_repository)

	response = controller.update(request.json, tripId)

	return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId):
	conn = db_connection_handler.get_connection()
	link_repository = LinksRepository(conn)
	controller = LinkCreator(link_repository)

	response = controller.create(request.json, tripId)

	return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId):
	conn = db_connection_handler.get_connection()
	link_repository = LinksRepository(conn)
	controller = LinkFinder(link_repository)

	response = controller.find(tripId)

	return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def create_participant(tripId):
	conn = db_connection_handler.get_connection()
	participant_repository = ParticipantsRepository(conn)
	emails_repository = EmailsToInviteRepository(conn)
	controller = ParticipantsCreator(participant_repository, emails_repository)

	response = controller.create(request.json, tripId)

	return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
	conn = db_connection_handler.get_connection()
	activity_repository = ActivitiesRepository(conn)
	controller = ActivityCreator(activity_repository)

	response = controller.create(request.json, tripId)

	return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def find_trip_participants(tripId):
	conn = db_connection_handler.get_connection()
	participants_repository = ParticipantsRepository(conn)

	controller = ParticipantFinder(participants_repository)

	response = controller.find(tripId)

	return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def find_trip_activities(tripId):
	conn = db_connection_handler.get_connection()
	participants_repository = ActivitiesRepository(conn)

	controller = ActivityFinder(participants_repository)

	response = controller.find(tripId)

	return jsonify(response["body"]), response["status_code"]


@trip_routes_bp.route(
	"/participants/<participantId>/participant_confirm", methods=["GET"]
)
def confirm_participant(participantId):
	conn = db_connection_handler.get_connection()
	trip_repository = ParticipantsRepository(conn)
	controller = ParticipantConfirmer(trip_repository)

	response = controller.confirm(participantId)

	return jsonify(response["body"]), response["status_code"]
