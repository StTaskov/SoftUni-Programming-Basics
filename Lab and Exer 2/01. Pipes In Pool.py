v_to_pool = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p = (p1 + p2) * h

if p < v_to_pool:
    print(f"The pool is {(p/100):.2f}% full. Pipe 1: {((p1*h)/100):.2f}%. Pipe 2: {((p2*h)/100):.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {(p-v_to_pool):.2f} liters.")