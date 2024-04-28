from flask import Flask
from flask_restful import Api
from routes import PowerConsumption,PowerConsumptionBetween
from db import mongo_connection



app = Flask(__name__)
api = Api(app)
api.add_resource(PowerConsumption, '/power_consumption', '/power_consumption/<string:timestamp>')
api.add_resource(PowerConsumptionBetween, '/power_consumption_between/<string:timestamp1>/<string:timestamp2>')


if __name__ == '__main__':
    # print("->>> Running unit test")
    # power_log = PowerConsumptionLog(timestamp=get_current_time_tunisia(), power_consumption=1.5)
    # power_log.save()
    if not mongo_connection:
        quit() 
    app.run(host="0.0.0.0", debug=True, use_reloader=False )
