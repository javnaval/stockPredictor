import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import cProfile
import json, urllib
import "../day.py"


dia = Day()
dia.f()
input(" press close to exit ")