class Bike(object):
	def __init__(self, price, max_speed):
			self.price = price
			self.max_speed = max_speed
			self.miles = 0


	def displayinfo(self):
			print 'Price is: $' + str(self.price)
			print 'Max Speed: ' + str(self.max_speed) + 'mph'
			print 'Total miles: ' + str(self.miles) + 'miles'


	def ride(self):
			print 'Riding'
			self.miles +=10

	def reverse(self):
			print 'Reversing'
			# no neg milage
			if self.miles >=5:
					self.miles -= 5


Bike1 = Bike(200, 30)
Bike1.ride()
Bike1.ride()
Bike1.ride()
Bike1.displayinfo()

Bike2 = Bike(440.59, 55)
Bike2.ride()
Bike2.ride()
Bike2.reverse()
Bike2.reverse()
Bike2.displayinfo()

Bike3 = Bike(49.99, 15)
Bike3.reverse()
Bike3.reverse()
Bike3.reverse()
Bike3.displayinfo()


