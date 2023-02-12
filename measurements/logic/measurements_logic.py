from variables.models import Variable
from .. models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    return measurement

def update_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    measurement = create_measurement(new_measurement)
    measurement.pk = measurement_pk
    measurement.save()
    return measurement

def create_measurement(measurement):
    varibles_pk = Variable.objects.get(pk=measurement["variable"])
    measurement = Measurement(variable=varibles_pk, value=measurement["value"], unit=measurement["unit"], place=measurement["place"], dateTime=measurement["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(measurement_pk):
    measurement = get_measurement(measurement_pk)
    measurement.delete()

