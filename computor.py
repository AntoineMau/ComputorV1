from setting import Setting
from polynome import Polynome

def main():
	setting = Setting()
	setting.parser()
	poly = Polynome(*setting.tab, setting.verbose, setting.graph)
	poly.process()
	poly.final()
	exit(0)

if __name__ == "__main__":
	main()