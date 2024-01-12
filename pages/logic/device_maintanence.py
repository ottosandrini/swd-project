import os
from tinydb import TinyDB, Query
from serializer import serializer
from datetime import datetime
from devices import Device

class MaintenancePlan(Device):
    def __init__(self, device: Device, maintenance_date: str, details: str):
        self.device = device  
        self.maintenance_date = maintenance_date
        self.details = details