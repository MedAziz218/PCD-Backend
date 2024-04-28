from flask import request
from flask_restful import Api, Resource
from models import PowerConsumptionLog
from utils import get_current_time_tunisia


class PowerConsumption(Resource):
    def get(self, timestamp):
        # Assuming timestamp is provided in ISO format, e.g., '2024-04-27T12:00:00'

        power_logs = PowerConsumptionLog.objects(timestamp=timestamp)
        if power_logs:
            return {timestamp: [log.power_consumption for log in power_logs]}
        else:
            return {"error": "No power consumption logs found for this timestamp"}, 404

    def put(self, timestamp=None):
        if request.is_json:
            data = request.get_json()
            if timestamp is None:
                timestamp = get_current_time_tunisia()
            power_log = PowerConsumptionLog(
                timestamp=timestamp, power_consumption=data.get("power_consumption")
            )
            power_log.save()
            return {str(timestamp): power_log.power_consumption}, 201
        else:
            return {"error": "Request must be JSON"}, 400


class PowerConsumptionBetween(Resource):
    def get(self, timestamp1, timestamp2=None):
        # Assuming timestamps are provided in ISO format, e.g., '2024-04-27T12:00:00'
        power_logs = PowerConsumptionLog.objects(
            timestamp__gte=timestamp1, timestamp__lte=timestamp2
        )
        if power_logs:
            return {
                log.timestamp.strftime("%Y-%m-%d %H:%M:%S"): log.power_consumption
                for log in power_logs
            }
        else:
            return {
                "error": "No power consumption logs found between these timestamps"
            }, 404

class PowerConsumptionBefore(Resource):
    def get(self, timestamp):
        # Assuming timestamps are provided in ISO format, e.g., '2024-04-27T12:00:00'
        power_logs = PowerConsumptionLog.objects(
             timestamp__lte=timestamp
        )
        if power_logs:
            return {
                log.timestamp.strftime("%Y-%m-%d %H:%M:%S"): log.power_consumption
                for log in power_logs
            }
        else:
            return {
                "error": "No power consumption logs found before this timestamp"
            }, 404

class PowerConsumptionAfter(Resource):
    def get(self, timestamp):
        # Assuming timestamps are provided in ISO format, e.g., '2024-04-27T12:00:00'
        power_logs = PowerConsumptionLog.objects(
            timestamp__gte=timestamp
        )
        if power_logs:
            return {
                log.timestamp.strftime("%Y-%m-%d %H:%M:%S"): log.power_consumption
                for log in power_logs
            }
        else:
            return {
                "error": "No power consumption logs found after this timestamp"
            }, 404


def routes_init(app):
    api = Api(app)
    
    api.add_resource(
        PowerConsumption, "/power_consumption", "/power_consumption/<string:timestamp>"
    )

    api.add_resource(
        PowerConsumptionBetween,
        "/power_consumption_between/<string:timestamp1>/<string:timestamp2>",
    )
    api.add_resource(
        PowerConsumptionBefore,
        "/power_consumption_before/<string:timestamp>",
    )
    api.add_resource(
        PowerConsumptionAfter,
        "/power_consumption_after/<string:timestamp>",
    )
    return api
