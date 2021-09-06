from argparse import ArgumentParser
from re import match, findall, sub

class Setting:
	def __init__(self):
		self.poly = str()
		self.graph = int()
		self.verbose = int()
		self.tab = {"2": float(), "1": float(), "0": float()}

	def parser(self):
		self.parse_option()
		self.parse_poly()
		self.reduced_form()

	def parse_option(self):
		parser = ArgumentParser()
		parser.add_argument("-v", "--verbose", action="store_true", default=False, help="show detail operations performed")
		parser.add_argument("-g", "--graph", action="store_true", default=False, help="show polynomial graph")
		parser.add_argument("poly", action="store", type=str, help="equation to process")
		args = parser.parse_args()
		self.poly = args.poly
		self.graph = args.graph
		self.verbose = args.verbose

	def poly_to_dict(self, numbers, tab, add):
		for x in numbers:
			nb, exp = x.split("*X^")
			nb = float(nb)
			if nb == 0:
				continue
			try:
				tab[exp] += nb if add is True else -nb
			except KeyError:
				tab[exp] = nb if add is True else -nb
		return tab

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

	def parse_poly(self):
		poly = self.poly.replace(" ", "")
		poly = sub(r"X(?!\^)", "X^1", poly)
		poly = sub(r"(?<!\*)X", "1*X", poly)
		poly = sub(r"(?<!\^\d)(?<=\d)(?![\*.\d])", "*X^0", poly)
		left, right = self.check_param(poly)
		regex = r"[-+]?\d*\.?\d*\*X\^?[-+]?\d*\.?\d*"
		self.tab = self.poly_to_dict(findall(regex, left), self.tab, True)
		self.tab = self.poly_to_dict(findall(regex, right), self.tab, False)

	def reduced_form(self):
		reduced_form = str()
		for exp, nb in self.tab.items():
			if nb == 0:
				continue
			if nb == 1:
				reduced_form += "+X " if exp == "1" else "+X^%d " % int(exp) if exp != "0" else "%+g " % nb
			else :
				reduced_form += "%+g " % nb
				reduced_form += "* X " if exp == "1" else "* X^%d " % int(exp) if exp != "0" else ""
		if reduced_form == "":
			reduced_form = "0 "
		reduced_form += "= 0"
		if reduced_form.startswith("+"):
			reduced_form = reduced_form[1:]
		print(" ".join(["Reduced form:", reduced_form.replace(" -", " - ").replace(" +", " + ")]))
		for exp in self.tab.keys():
			try:
				assert(int(exp) == 0 or int(exp) == 1 or int(exp) == 2)
			except:
				self.errno("degree", exp)
		self.tab = self.tab.values()
	
	def errno(self, nb_error, detail = None):
		msg_error = {
			"degree": "Polynomial degree: %s\nThe polynomial degree is stricly greater than 2, I can't solve." % detail,
			"bad poly": "Error: bad format of polynom. Ex: a * X^2 + b * X^1 - c * X^0 = d * X^0",
		}
		print(msg_error[nb_error])
		exit(1)
