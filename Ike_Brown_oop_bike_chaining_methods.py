class Bike(object):
	def __init__(self, price, max_speed):
			self.price = price
			self.max_speed = max_speed
			self.miles = 0

	def ride(self):
			print 'Ridden'
			self.miles +=0
			return self

	def reverse(self):
			print 'Reversing'
			# no neg milage
			if self.miles >=5:
					self.miles -= 5
					return self

	def displayinfo(self):
			print 'Price is: $' + str(self.price)
			print 'Max Speed: ' + str(self.max_speed) + 'mph'
			print 'Total miles: ' + str(self.miles) + 'miles'
			return self

Bike1 =  Bike(200, 30)
Bike1.ride().displayinfo()

Bike2 = Bike(440.59, 55)
Bike2.ride().reverse().displayinfo()

Bike3 = Bike(49.99, 15)
Bike3.reverse().displayinfo()