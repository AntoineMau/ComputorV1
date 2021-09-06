import matplotlib.pyplot as plt

class Polynome:
	def __init__(self, a, b, c, verbose, graph):
		self.a, self.b, self.c = a, b, c
		if a != 0:
			self.degree = 2
		elif b != 0:
			self.degree = 1
		else:
			self.degree = 0
		self.verbose, self.graph = verbose, graph

	def degree_0(self):
		if self.verbose:
			print("form: a = 0")
			print("a: %g\n" % self.c)
		return "All real numbers are solutions." if self.c == 0 else "it can't be solved"

	def degree_1(self):
		verbose = str()
		if self.verbose:
			print("form: a*x + b = 0")
			print("a: %g" % self.b)
			print("b: %g\n" % self.c)
			verbose += "x: -b/a\n"
			verbose += "x: %g/%g\n" % (-self.c, self.b)
		x = -self.c / self.b
		if x == 0:
			x = 0
		return "The solution is:\n" + verbose + "x: %g" % x

	def degree_2(self):
		if self.verbose:
			print("form: a*x^2 + b*x + c = 0")
			print("a: %g" % self.a)
			print("b: %g" % self.b)
			print("c: %g\n" % self.c)
		return self.get_solution()

	def process(self):
		tab_degree = [self.degree_0, self.degree_1, self.degree_2]
		self.solution = tab_degree[self.degree]()

	def discriminant_positive(self, discriminant):
		verboseX1, verboseX2 = str(), str()
		if self.verbose:
			verboseX1 += "x1: (-b - √Δ) / (2*a)\n"
			verboseX2 += "\nx2: (-b + √Δ) / (2*a)\n"
			self.b = -self.b
			verboseX1 += "x1: (%g - √%g) / (2*%g)\n" % (self.b, discriminant, self.a)
			verboseX2 += "x2: (%g + √%g) / (2*%g)\n" % (self.b, discriminant, self.a)
			discriminant = discriminant**0.5
			self.a = 2*self.a
			verboseX1 += "x1: (%g - %g) / %g\n" % (self.b, discriminant, self.a)
			verboseX2 += "x2: (%g + %g) / %g\n" % (self.b, discriminant, self.a)
			verboseX1 += "x1: %g / %g\n" % (self.b - discriminant, self.a)
			verboseX2 += "x2: %g / %g\n" % (self.b + discriminant, self.a)
		else:
			self.b = -self.b
			discriminant = discriminant**0.5
			self.a = 2*self.a
		x1 = (self.b - discriminant) / self.a
		x2 = (self.b + discriminant) / self.a
		if x1 == 0:
			x1 = 0
		if x2 == 0:
			x2 = 0
		return "Discriminant is strictly positive, the two solutions are:\n" + verboseX1 + "x1: %g\n" % x1 + verboseX2 + "x2: %g" % x2

	def discriminant_zero(self):
		verbose = str()
		if self.verbose:
			verbose += "x: -b / (2*a)\n"
			verbose += "x: %g / (2*%g)\n" % (-self.b, self.a)
			verbose += "x: %g / %g\n" % (-self.b, 2*self.a)
		x = -self.b / (2*self.a)
		if x == 0:
			x = 0
		return "Discriminant is null, the solution is\n" + verbose + "x: %g" % x

	def discriminant_negative(self, discriminant):
		verboseX1, verboseX2 = str(), str()
		if self.verbose:
			verboseX1 += "x1: (-b - i√-Δ) / (2*a)\n"
			verboseX2 += "\nx2: (-b + i√-Δ) / (2*a)\n"
			self.b = -self.b
			verboseX1 += "x1: (%g - i√%g) / (2*%g)\n" % (self.b, discriminant, self.a)
			verboseX2 += "x2: (%g + i√%g) / (2*%g)\n" % (self.b, discriminant, self.a)
		else:
			self.b = -self.b
		self.a = 2*self.a
		x1 = "x1: (%g - i√%g) / %g\n" % (self.b, discriminant, self.a)
		x2 = "x2: (%g + i√%g) / %g" % (self.b, discriminant, self.a)
		if x1 == 0:
			x1 = 0
		if x2 == 0:
			x2 = 0
		return "Discriminant is strictly negative, the two solutions are:\n" + verboseX1 + x1 + verboseX2 + x2

	def get_solution(self):
		discriminant = self.b**2 - 4*self.a*self.c
		if self.verbose:
			print("Δ: b^2 - 4*a*c")
			print("Δ: %g^2 - 4*%g*%g" % (self.b, self.a, self.c))
			print("Δ: %g - %g" % (self.b**2, 4*self.a*self.c))
			print("Δ: %g\n" % discriminant)
		if discriminant > 0:
			return self.discriminant_positive(discriminant)
		elif discriminant == 0:
			return self.discriminant_zero()
		else:
			return self.discriminant_negative(-discriminant)

	def exe_graph(self):
		ranges = range(-20, 21)
		title = 'Straight line'
		if self.degree == 0:
			tab = [self.c for x in ranges]
		elif self.degree == 1:
			tab = [self.b*x + self.c for x in ranges]
		else:
			title = 'Parabola'
			tab = [self.a*x**2 + self.b*x + self.c for x in ranges]
		if self.verbose:
			print("\nGraph:\n%3s: %10s" % ("x", "f(x)"))
			i = 0
			for x in ranges:
				print("%3d: %10g" % (x, tab[i]))
				i += 1
		plt.plot(ranges, tab)
		plt.xlabel('x')
		plt.ylabel('f(x)')
		plt.title(title)
		plt.show()

	def final(self):
		print("Polynomial degree: %d" % self.degree)
		print(self.solution)
		if self.graph:
			self.exe_graph()
