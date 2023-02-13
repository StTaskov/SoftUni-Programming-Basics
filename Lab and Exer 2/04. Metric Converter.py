number = float(input())
input_unit = input()
output_unit = input()

if input_unit == 'mm' and output_unit == 'cm':
    print(f'{number/10:.3f}')
elif input_unit == "cm" and output_unit == "mm":
    print(f'{number*10:.3f}')
elif input_unit == 'cm' and output_unit == "m":
    print(f"{number/100:.3f}")
elif input_unit =="m" and output_unit == "cm":
     print(f"{number*100:.3f}")
elif input_unit == "m" and output_unit == "mm":
    print(f"{number*1000:.3f}")
elif input_unit == "mm" and output_unit == "m":
    print(f"{number/1000:.3f}")
