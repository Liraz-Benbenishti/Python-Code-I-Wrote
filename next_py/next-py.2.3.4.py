class Pixel:
	"""
	_x - x coordinate
	_y - y coordinate
	_red - a value between 0 and 255
	_green - a value between 0 and 255
	_blue - a value between 0 and 255
	"""
	def __init__(self, x = 0, y = 0, red = 0, green = 0, blue = 0):
		self._x = x
		self._y = y
		self._red = red
		self._green = green
		self._blue = blue
		
	def set_coords(self, x, y):
		self._x = x
		self._y = y
		
	def set_grayscale(self):
		average_color = (self._red + self._green + self._blue) // 3
		self._red = average_color
		self._green = average_color
		self._blue = average_color
		
	def print_pixel_info(self):
		extra_color = ""
		if (self._red + self._green + self._blue == self._red and self._red > 50):
			extra_color = "Red"
		elif (self._red + self._green + self._blue == self._green and self._green > 50):
			extra_color = "Green"
		elif (self._red + self._green + self._blue == self._blue and self._blue > 50):
			extra_color = "Blue"
		
		print("X: %d, Y: %d, Color: (%d, %d, %d) %s" % (self._x, self._y, self._red, self._green, self._blue, extra_color))
		
def main():
	p = Pixel(5, 6, 250)
	p.print_pixel_info()
	p.set_grayscale()
	p.print_pixel_info()
	
if __name__ == "__main__":
	main()