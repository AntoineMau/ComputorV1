#!/usr/bin/python3
# !./.venv/bin/python3

from setting import Setting
from polynome import Polynome

def main():
	setting = Setting()
	poly = Polynome(*setting.tab, setting.verbose, setting.graph)
	poly.final()
	exit(0)

if __name__ == "__main__":
	main()