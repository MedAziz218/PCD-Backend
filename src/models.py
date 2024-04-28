import mongoengine as mg
class PowerConsumptionLog(mg.Document):
    timestamp = mg.DateTimeField(required=True)
    power_consumption = mg.FloatField(required=True)
