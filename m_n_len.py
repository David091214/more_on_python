
m = int(input().strip())  
n = int(input().strip())  


binary = bin(m)[2:]


padded_binary = binary.zfill(n)


print(padded_binary)