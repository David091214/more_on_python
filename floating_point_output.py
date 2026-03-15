num_input = input().strip()
num_float = float(num_input)


first = f"{num_float:.6f}"

second = f"{num_float:.2f}"


third = f"{num_float:.8f}"

fourth = f"{num_float:e}"

if '.' in num_input:
    integer_part, decimal_part = num_input.split('.')
    fifth = f"{int(integer_part):,}.{decimal_part}"
else:
    fifth = f"{int(num_input):,}"

print(f"{first}/{second}/{third}/{fourth}/{fifth}")