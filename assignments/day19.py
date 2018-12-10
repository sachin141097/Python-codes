Maths={1,2,3,5,7,9}
Physics={2,4,6,9}
Chemistry={1,3,5,9}
M=set(Maths)
P=set(Physics)
C=set(Chemistry)
print("Students studying Maths and Physics:",M&P)
print("Students studying Physics and Chemistry:",P&C)
print("Students studying Maths and Chemistry:",M&C)
print("Students studying exactly one of the three subjects:",M | P | C )

