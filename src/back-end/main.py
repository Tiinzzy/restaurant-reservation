from reservation import Reservation

print('this will be my entry to the back-end service!')

r1 = Reservation()
r2 = Reservation()

r1.load(10)
r2.load(11)

print(r1.get_id())
print(r2.get_id())

