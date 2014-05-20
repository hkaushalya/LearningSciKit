# -*- coding: utf-8 -*-
"""
@author: samantha
3.3.2 Structured data types
"""
import numpy as np

# sendor_code = 4 chr
# position    = float
# values      = float

samples = np.zeros( (6,),
         dtype=[('sensor_code', 'S4'),
               ('position', float),
                ('value', float)]
            )
samples.ndim
samples.shape
samples.dtype.names
samples[:] = [('ALFA',  1, 0.37), ('BETA', 1, 0.11), ('TAU',  1,  0.13),
                ('ALFA',  1.5, 0.37), ('ALFA', 3, 0.11), ('TAU',  1.2,  0.13)]
samples['sensor_code']
samples['value']
samples[0]
samples[0]['sensor_code'] = 'TAU'
samples[0]
# multiple fields at once
samples[['position', 'value']]