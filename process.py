from utils import errno

def reduced_form(tab, Reduced_form):
	for exp, nb in tab.items():
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
	print(" ".join(["Reduced form:", Reduced_form\
		.replace(" -", " - ").replace(" +", " + ")]))
	for exp in tab.keys():
		try:
			assert(int(exp) == 0 or int(exp) == 1 or int(exp) == 2)
		except:
			errno("degree", exp)
	return tab.values()

def discriminant_positive(poly, sqrt_disc):
	if poly.verbose:
		print("x1: (-b - √Δ) / (2*a)\nx2: (-b + √Δ) / (2*a)\n")
	x1 = (-poly.b - sqrt_disc) / (2*poly.a)
	x2 = (-poly.b + sqrt_disc) / (2*poly.a)
	if x1 == 0:
		x1 = 0
	if x2 == 0:
		x2 = 0
	return ("Discriminant is strictly positive, the two solutions are:\n%g\n%g"
		% (x1, x2))

def discriminant_zero(poly):
	if poly.verbose:
		print("x: -b / (2*a)\n")
	x = -poly.b / 2*poly.a
	if x == 0:
		x = 0
	return "Discriminant is null, the solution is %g" % x

def get_solution(poly):
	discriminant = poly.b**2 - 4*poly.a*poly.c
	if poly.verbose:
		print("Δ: b^2 - 4*a*c = %g\n" % discriminant)
	if discriminant > 0:
		solution = discriminant_positive(poly, discriminant ** 0.5)
	elif discriminant == 0:
		solution = discriminant_zero(poly)
	else:
		solution = "Discriminant is strictly negative, no real solution exist."
	return(solution)
