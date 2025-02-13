from ..models import Measurement
from ..models import Variable
def get_measurements():
    measurements = Measurement.objects.all()
    return measurements
def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement
def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.variable = new_var["variable"]
    measurement.value = new_var["value"]
    measurement.unit = new_var["unit"]
    measurement.place = new_var["place"]
    measurement.dateTime = new_var["dateTime"]
    measurement.save()
    return measurement
def create_measurement(var):
    measurement = Measurement(Variable.objects.get(pk=var["variable"]))
    measurement.save()
    measurement = Measurement(value=var["value"])
    measurement.save()
    measurement = Measurement(unit=var["unit"])
    measurement.save()
    measurement = Measurement(place= var["place"])
    measurement.save()
    measurement = Measurement(datetime= var["dateTime"])
    measurement.save()
    return measurement
def delete_measurements(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    measurement.delete()
    return measurement