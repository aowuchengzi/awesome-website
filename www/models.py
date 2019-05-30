import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return