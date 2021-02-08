import matplotlib.pyplot as plt
from argparse import ArgumentParser

def parse_option():
	parser = ArgumentParser(usage="./%(prog)s [-h] [-v] [-g] poly")
	parser.add_argument("-v", "--verbose", action="store_true", default=False, \
		help="show detail operations performed")
	parser.add_argument("-g", "--graph", action="store_true", default=False, \
		help="show polynomial graph")
	parser.add_argument("poly", action="store", type=str, \
		help="polynom to process")
	return parser.parse_args()

def exe_graph(poly):
	ranges = range(-20, 21)
	if poly.degree == 0:
		tab = [poly.c for x in ranges]
		title = 'Straight line'
	elif poly.degree == 1:
		tab = [poly.b*x + poly.c for x in ranges]
		title = 'Straight line'
	else:
		tab = [poly.a*x**2 + poly.b*x + poly.c for x in ranges]
		title = 'Parabola'
	if poly.verbose:
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

def errno(nb_error, detail = None):
	msg_error = {
		"degree": "Polynomial degree: %s\nThe polynomial degree is stricly greater than 2, I can't solve." % detail,
		"bad poly": "Error: bad format of polynom. Ex: c * X^0 + b * X^1 - a * X^2 = d * X^0",
		"nb_params": "Error: bad number of arguments (%s). Need 1 polynom in argument" % detail,
	}
	print(msg_error[nb_error])
	exit(1)
