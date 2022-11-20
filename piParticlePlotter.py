try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp

mp.dps = 1000  # set number of digits

value =mp.nstr((mp.mpf(mp.pi)),100)

my_list = []

for x in str(value):
    my_list.append(str(x))

print(my_list)