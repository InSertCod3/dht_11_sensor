from distutils.core import setup, Extension
setup(name='dht_sensor', version='1.0',
      ext_modules=[Extension('dht_sensor', ['sensor_dht.c'],
                             libraries=['wiringPi', 'pthread'])])
