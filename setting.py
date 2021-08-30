from argparse import ArgumentParser
from re import match, findall, sub

class Setting:
	def __init__(self):
		self.poly = str()
		self.graph = int()
		self.verbose = int()
		self.tab = {"0": 0, "1": 0, "2": 0}
		self.parser()

	def parser(self):
		self.parse_option()
		self.parse_poly()
		self.reduced_form("")

	def parse_option(self):
		parser = ArgumentParser()
		parser.add_argument("-v", "--verbose", action="store_true", default=False, help="show detail operations performed")
		parser.add_argument("-g", "--graph", action="store_true", default=False, help="show polynomial graph")
		parser.add_argument("poly", action="store", type=str, help="polynom to process")
		args = parser.parse_args()
		self.poly = args.poly
		self.graph = args.graph
		self.verbose = args.verbose

	def parse_poly(self):
		poly = self.poly.replace(" ", "")
		poly = sub(r"X(?!\^)", "X^1", poly)
		poly = sub(r"(?<!\*)X", "1*X", poly)
		poly = sub(r"(?<!\^\d)(?<=\d)(?![\*.\d])", "*X^0", poly)
		left, right = self.check_param(poly)
		regex = r"[-+]?\d*\.?\d*\*X\^?[-+]?\d*\.?\d*"
		self.tab = self.poly_to_dict(findall(regex, left), self.tab, True)
		self.tab = self.poly_to_dict(findall(regex, right), self.tab, False)

	def poly_to_dict(self, numbers, tab, add):
		for x in numbers:
			nb, exp = x.split("*X^")
			try:
				tab[exp] += float(nb) if add is True else -float(nb)
			except KeyError:
				tab[exp] = float(nb) if add is True else -float(nb)
		return(tab)

	def check_param(self, poly):
		try:
			left, right = poly.split("=")
		except ValueError:
			self.errno("bad poly")
		good_poly = r"^((\+|-|\^)?\d+(\.\d+)?\*X\^[\+-]?\d+(\.\d+)?)+$"
		try:
			assert(match(good_poly, left) or False)
			assert(match(good_poly, right) or False)
		except AssertionError:
			self.errno("bad poly")
		return(left, right)

	def reduced_form(self, Reduced_form):
		for exp, nb in self.tab.items():
			if nb == 0:
				pass
			elif exp == "0":
				Reduced_form += "%g " % nb
			elif exp == "1":
				Reduced_form += ("%+g * X " % nb).replace("1 * ", "")
			else:
				Reduced_form += ("%+g * X^%g " % (nb, int(exp))).replace("1 * ", "")
		if Reduced_form == "":
			Reduced_form = "0 "
		Reduced_form += "= 0"
		if Reduced_form.startswith("+"):
			Reduced_form = Reduced_form[1:]
		for exp in self.tab.keys():
			try:
				assert(int(exp) == 0 or int(exp) == 1 or int(exp) == 2)
			except:
				self.errno("degree", exp)
		self.tab = self.tab.values()
	
	def errno(nb_error, detail = None):
		msg_error = {
			"degree": "Polynomial degree: %s\nThe polynomial degree is stricly greater than 2, I can't solve." % detail,
			"bad poly": "Error: bad format of polynom. Ex: c * X^0 + b * X^1 - a * X^2 = d * X^0",
		}
		print(msg_error[nb_error])
		exit(1)
