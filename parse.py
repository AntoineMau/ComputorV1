from re import match, findall, sub
from utils import errno

def reduced_form(numbers, tab, add):
	for x in numbers:
		nb, exp = x.split("*X^")
		try:
			tab[exp] += float(nb) if add is True else -float(nb)
		except KeyError:
			tab[exp] = float(nb) if add is True else -float(nb)
	return tab

def check_param(poly):
	try:
		left, right = poly.split("=")
	except ValueError:
		errno("bad poly")
	good_poly = r"^((\+|-|\^)?\d+(\.\d+)?\*X\^[\+-]?\d+(\.\d+)?)+$"
	try:
		assert(match(good_poly, left) or False)
		assert(match(good_poly, right) or False)
	except AssertionError:
		errno("bad poly")
	return(left, right)

def parse(poly):
	poly = poly.replace(" ", "")
	poly = sub(r"X(?!\^)", "X^1", poly)
	poly = sub(r"(?<!\*)X", "1*X", poly)
	poly = sub(r"(?<!\^\d)(?<=\d)(?![\*.\d])", "*X^0", poly)
	left, right = check_param(poly)
	regex = r"[-+]?\d*\.?\d*\*X\^?[-+]?\d*\.?\d*"
	tab = {"0": 0, "1": 0, "2": 0}
	tab = reduced_form(findall(regex, left), tab, True)
	tab = reduced_form(findall(regex, right), tab, False)
	return tab
