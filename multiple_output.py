num = int(input())


binary = bin(num)[2:]  


octal = oct(num)[2:]   


octal_prefix = oct(num)  


hex_lower = hex(num)[2:] 

hex_lower_prefix = hex(num)  

hex_upper_prefix = hex(num).upper() 

print(f"{binary},{octal},{octal_prefix},{hex_lower},{hex_lower_prefix},{hex_upper_prefix}")