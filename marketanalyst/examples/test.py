#!/usr/bin/env python3

import numpy as np
import pandas as pd
import pandas_datareader as pdr


gld = pdr.get_data_google('GLD','2016-11-08')
