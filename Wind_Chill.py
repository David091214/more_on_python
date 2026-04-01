# Ta = int(input())
# V = int(input())

# windchill  = 13.12 + (0.6215 * Ta) - (11.37* (V**0.16)) + (0.3965 * Ta * (V**0.16))
# print(f"{windchill}")

import math


wind_speed = float(input())
air_temp = float(input())

v = wind_speed 
Ta = air_temp

windchill  = 13.12 + (0.6215 * Ta) - (11.37* (v**0.16)) + (0.3965 * Ta * (v**0.16))

chill_index = round(windchill)


print(chill_index)