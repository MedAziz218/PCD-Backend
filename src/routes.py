from flask import request
from flask_restful import Resource
from models import PowerConsumptionLog
from utils import get_current_time_tunisia



class PowerConsumption(Resource):
    def get(self, timestamp):
        # Assuming timestamp is provided in ISO format, e.g., '2024-04-27T12:00:00'
        
        power_logs = PowerConsumptionLog.objects(timestamp=timestamp)
        if power_logs:
            return {timestamp: [log.power_consumption for log in power_logs]}
        else:
            return {'error': 'No power consumption logs found for this timestamp'}, 404
    
    def put(self,*args):
        if request.is_json:
            data = request.get_json()
            timestamp = get_current_time_tunisia()
            power_log = PowerConsumptionLog(timestamp=timestamp, power_consumption=data.get('power_consumption'))
            # power_log = PowerConsumptionLog(timestamp=timestamp, power_consumption=1.5)
            
            power_log.save()
            return {str(timestamp): power_log.power_consumption}, 201
        else:
            return {'error': 'Request must be JSON'}, 400

class PowerConsumptionBetween(Resource):
    def get(self, timestamp1, timestamp2):
        # Assuming timestamps are provided in ISO format, e.g., '2024-04-27T12:00:00'
        power_logs = PowerConsumptionLog.objects(timestamp__gte=timestamp1, timestamp__lte=timestamp2)
        if power_logs:
            return {log.timestamp.strftime('%Y-%m-%d %H:%M:%S'): log.power_consumption for log in power_logs}
        else:
            return {'error': 'No power consumption logs found between these timestamps'}, 404
