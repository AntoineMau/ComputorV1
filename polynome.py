import matplotlib.pyplot as plt

class Polynome:
	def __init__(self, a, b, c, verbose, graph):
		self.a, self.b, self.c = a, b, c
		self.degree = 2 if a != 0 else 1 if b != 0 else 0
		self.verbose, self.graph = verbose, graph
		self.solution = self.process()

	def degree_0(self):
		if self.verbose:
			print("form: a = 0\na: %g\n" % self.c)
		return "All real numbers are solutions." if self.c == 0 else "it can't be solved"

	def degree_1(self):
		if self.verbose:
			print("form: a*x + b = 0\na: %g\nb: %g\nx: -b/a\n" % (self.b, self.c))
		x = -self.c / self.b
		if x == 0:
			x = 0
		return "The solution is:\n%g" % x

	def degree_2(self):
		if self.verbose:
			print("form: a*x^2 + b*x + c = 0\na: %g\nb: %g\nc: %g\n" % (self.a, self.b, self.c))
		return self.get_solution()

	def process(self):
		tab_degree = [self.degree_0, self.degree_1, self.degree_2]
		return tab_degree[self.degree]()

	def discriminant_positive(self, sqrt_disc):
		if self.verbose:
			print("x1: (-b - √Δ) / (2*a)\nx2: (-b + √Δ) / (2*a)\n")
		x1 = (-self.b - sqrt_disc) / (2*self.a)
		x2 = (-self.b + sqrt_disc) / (2*self.a)
		if x1 == 0:
			x1 = 0
		if x2 == 0:
			x2 = 0
		return "Discriminant is strictly positive, the two solutions are:\nx1: %g\nx2: %g" % (x1, x2)

	def discriminant_zero(self):
		if self.verbose:
			print("x: -b / (2*a)\n")
		x = -self.b / 2*self.a
		if x == 0:
			x = 0
		return "Discriminant is null, the solution is %g" % x

	def discriminant_negative(self, discriminant):
		if self.verbose:
			print("x1: (-b - i√Δ) / (2*a)\nx2: (-b + i√Δ) / (2*a)\n")
		x1 = "(%g - i√%g) / %g" % (-self.b, discriminant, 2*self.a)
		x2 = "(%g + i√%g) / %g" % (-self.b, discriminant, 2*self.a)
		if x1 == 0:
			x1 = 0
		if x2 == 0:
			x2 = 0
		return "Discriminant is strictly negative, the two solutions are:\nx1: %s\nx2: %s" % (x1, x2)

	def get_solution(self):
		discriminant = self.b**2 - 4*self.a*self.c
		if self.verbose:
			print("Δ: b^2 - 4*a*c = %g\n" % discriminant)
		if discriminant > 0:
			solution = self.discriminant_positive(discriminant ** 0.5)
		elif discriminant == 0:
			solution = self.discriminant_zero()
		else:
			solution = self.discriminant_negative(-discriminant)
		return solution

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
		print("Polynomial degree: {self.degree}\n{self.solution}".format(self=self))
		if self.graph:
			self.exe_graph()
