import os, sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import cProfile
import json, urllib
from day import Day

dia = Day()
print(dia.retornation)
input(" press close to exit ")