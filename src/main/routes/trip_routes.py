from flask import jsonify, Blueprint

trip_routes_bp = Blueprint("trip_routes", __name__)


@trip_routes_bp.route("/trips", methods=["POST"])
def create_trip():
	return jsonify({"ola": "mundo"}), 200
