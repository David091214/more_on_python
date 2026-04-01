# import math


# lat1 = float(input())   
# lon1 = float(input())   
# lat2 = float(input())  
# lon2 = float(input())   


# R = 6371.0


# lat1_rad = math.radians(lat1)
# lon1_rad = math.radians(lon1)
# lat2_rad = math.radians(lat2)
# lon2_rad = math.radians(lon2)


# dlat = lat2_rad - lat1_rad
# dlon = lon2_rad - lon1_rad


# a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
# c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
# distance = R * c

# # Output with 4 decimal places
# print(f"{distance:.4f}")


import math


lat1 = float(input())   
lon1 = float(input())   
lat2 = float(input())  
lon2 = float(input())   


R = 6371


lat1_rad = math.radians(lat1)
lon1_rad = math.radians(lon1)
lat2_rad = math.radians(lat2)
lon2_rad = math.radians(lon2)


dlat = lat2_rad - lat1_rad
dlon = lon2_rad - lon1_rad



c = math.acos(math.sin(lat1_rad)*math.sin(lat2_rad)+math.cos(lat1_rad)*math.cos(lat2_rad)*math.cos(lon1_rad - lon2_rad) ) 
distance = R * c

print(f"{distance:.4f}", end ="km")