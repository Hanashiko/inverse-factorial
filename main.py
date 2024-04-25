import sys
sys.set_int_max_str_digits(6000)
def inverse_fact(input):
    prod = 1
    i = 1
    while True:
        if input % i == 0: 
            prod *= i
            if prod == input:
                return i
        else:
            return 0
        i += 1
        
        
print(inverse_fact(int(input())))
