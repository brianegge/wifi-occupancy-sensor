
from wifi_occupancy_sensor.controllers import database
from wifi_occupancy_sensor import models


class Leases(database.Table):

    name = 'leases'
    record_class = models.Lease
    schema = database.Table.schema % ('leases', 'id TEXT PRIMARY KEY NOT NULL, expir_ts TEXT, mac_address TEXT, ip TEXT, host_name TEXT')
