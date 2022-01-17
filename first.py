def print_two(*args):
  arg1,arg2=args
  print(f"arg1:{arg1}, arg2:{arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")

def print_ones(arg1):
    print(f"arg1:{arg1}")

def print_twos(arg2):
    print(f"arg2:{arg2}")

print_two("ch","prashanth")
print_two_again("ch","prashanth")
print_ones("first!")
print_twos("second!")