
R = int(input())/255
G = int(input())/255
B = int(input())/255



Max = max(R,G,B)
Min = min(R,G,B)



V = Max



if V == 0:
   S = 0
else :
    S= (Max - Min)/V




if (Max == R):
    H =60*(0+(G-B)/(Max-Min))
        
elif (Max == G):
   H = 60*(2+(B-R)/(Max-Min))
        
else :
    H = 60*(4+(R-G)/(Max-Min))
        

if H<0:
    H+=360
print(f"{H:.4f},{S:.4%},{V:.4%}")
