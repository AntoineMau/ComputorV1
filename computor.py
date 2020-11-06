#!./.venv/bin/python3

from parse import parse
from utils import errno, exe_graph, parse_option
from process import get_solution, reduced_form

def degree_0(poly):
	return "All real numbers are solutions." if poly.c == 0 \
		else "it can't be solved"

def degree_1(poly):
	if poly.verbose:
		print("form: a*x + b = 0\na: %g\nb: %g\nx: -b/c\n" % (poly.b, poly.c))
	x = -poly.c / poly.b
	if x == 0:
		x = 0
	return("The solution is:\n%g" % x)

def degree_2(poly):
	if poly.verbose:
		print("form: a*x^2 + b*x + c = 0\na: %g\nb: %g\nc: %g\n" \
			% (poly.a, poly.b, poly.c))
	return get_solution(poly)

class Polynome:
	def __init__(self, c, b, a, verbose, graph):
		self.a, self.b, self.c = a, b, c
		self.degree = 2 if a != 0 else 1 if b != 0 else 0
		self.verbose, self.graph = verbose, graph

	def process(self):
		tab_degree = [degree_0, degree_1, degree_2]
		return tab_degree[self.degree](poly)

	def __str__(self):
		return "Polynomial degree: {self.degree}\n{self.solution}"\
			.format(self=self)

if __name__ == "__main__":
	(options, args) = parse_option()
	if len(args) != 1:
		errno("nb_params", len(args))
	tab = reduced_form(parse(args[0]), "")
	poly = Polynome(*tab, **vars(options))
	poly.solution = poly.process()
	print(poly)
	if poly.graph:
		exe_graph(poly)
	exit(0)
