class thifrtel():
	def sh(thifr):
		thifr = str(thifr)
		slo = ""
		for s in thifr:
			if s == "x":
				slo += "а"
			elif s == "м":
				slo += "б"
			elif s == "й":
				slo += "в"
			elif s == "у":
				slo += "г"
			elif s == "ё":
				slo += "д"	
			elif s == "п":
				slo += "е"
			elif s == "в":
				slo += "ё"
			elif s == "b":
				slo += "ж"
			elif s == "щ":
				slo += "з"
			elif s == "d":
				slo += "и"
			elif s == "з":
				slo += "й"	
			elif s == "ж":
				slo += "к"
			elif s == "о":
				slo += "л"
			elif s == "3":
				slo += "м"
			elif s == "4":
				slo += "н"
			elif s == "к":
				slo += "о"
			elif s == "л":
				slo += "п"	
			elif s == "p":
				slo += "р"
			elif s == "ш":
				slo += "с"
			elif s == "э":
				slo += "т"
			elif s == "&":
				slo += "у"
			elif s == "и":
				slo += "ф"
			elif s == "ь":
				slo += "х"	
			elif s == "с":
				slo += "ц"
			elif s == "ф":
				slo += "ч"
			elif s == "х":
				slo += "ш"
			elif s == "а":
				slo += "щ"
			elif s == "ы":
				slo += "ъ"
			elif s == ":":
				slo += "ы"	
			elif s == "ц":
				slo += "ь"
			elif s == "н":
				slo += "э"
			elif s == "т":
				slo += "ю"
			elif s == "1":
				slo += "я"
			elif s == "2":
				slo += "1"
			elif s == "i":
				slo += "2"	
			elif s == "б":
				slo += "3"
			elif s == "ъ":
				slo += "4"
			elif s == "k":
				slo += "5"
			elif s == "ю":
				slo += "6"
			elif s == "c":
				slo += "7"
			elif s == "f":
				slo += "8"	
			elif s == "р":
				slo += "9"
			elif s == "8":
				slo += "0"	
			elif s == "6":
				slo += "a"
			elif s == "я":
				slo += "b"	
			elif s == "n":
				slo += "c"
			elif s == "a":
				slo += "d"	
			elif s == "e":
				slo += "e"
			elif s == "7":
				slo += "f"
			elif s == "9":
				slo += "g"
			elif s == "t":
				slo += "h"	
			elif s == "g":
				slo += "i"
			elif s == "ч":
				slo += "j"	
			elif s == "j":
				slo += "k"	
			elif s == "y":
				slo += "l"
			elif s == "s":
				slo += "m"	
			elif s == "д":
				slo += "n"
			elif s == "0":
				slo += "o"
			elif s == "m":
				slo += "p"	
			elif s == "h":
				slo += "q"	
			elif s == "l":
				slo += "r"
			elif s == "q":
				slo += "s"	
			elif s == "%":
				slo += "t"	
			elif s == "z":
				slo += "u"
			elif s == "г":
				slo += "v"	
			elif s == "^":
				slo += "w"
			elif s == "е":
				slo += "x"
			elif s == "o":
				slo += "y"	
			elif s == "5":
				slo += "z"
			elif s == ")":
				slo += "!"
			elif s == "v":
				slo += "@"
			elif s == "r":
				slo += "$"
			elif s == "=":
				slo += "%"
			elif s == "№":
				slo += "^"
			elif s == "w":
				slo += "&"
			elif s == "+":
				slo += "*"
			elif s == "-":
				slo += "("
			elif s == "#":
				slo += ")"
			elif s == "/":
				slo += "_"
			elif s == "|":
				slo += "+"
			elif s == "_":
				slo += "="
			elif s == "<":
				slo += "-"
			elif s == ";":
				slo += "?"
			elif s == "@":
				slo += ":"
			elif s == "(":
				slo += "№"
			elif s == "?":
				slo += '"'	
			elif s == ",":
				slo += "/"
			elif s == "!":
				slo += ","	
			elif s == "$":
				slo += " "
			elif s == "[":
				slo += "."
		return(slo)

	def thif(fraz):
		spis = ""
		for j in fraz:
			if j == "а":
				spis += "x"
			elif j == "б":
				spis += "м"
			elif j == "в":
				spis += "й"
			elif j == "г":
				spis += "у"
			elif j == "д":
				spis += "ё"
			elif j == "е":
				spis += "п"
			elif j == "ё":
				spis += "в"
			elif j == "ж":
				spis += "b"
			elif j == "з":
				spis += "щ"
			elif j == "и":
				spis += "d"
			elif j == "й":
				spis += "з"
			elif j == "к":
				spis += "ж"
			elif j == "л":
				spis += "о"
			elif j == "м":
				spis += "3"
			elif j == "н":
				spis += "4"
			elif j == "о":
				spis += "к"
			elif j == "п":
				spis += "л"
			elif j == "р":
				spis += "p"
			elif j == "с":
				spis += "ш"
			elif j == "т":
				spis += "э"
			elif j == "у":
				spis += "&"
			elif j == "ф":
				spis += "и"
			elif j == "х":
				spis += "ь"
			elif j == "ц":
				spis += "с"
			elif j == "ч":
				spis += "ф"
			elif j == "ш":
				spis += "х"
			elif j == "щ":
				spis += "а"
			elif j == "ъ":
				spis += "ы"
			elif j == "ы":
				spis += ":"
			elif j == "ь":
				spis += "ц"
			elif j == "э":
				spis += "н"
			elif j == "ю":
				spis += "т"
			elif j == "я":
				spis += "1"
			elif j == "1":
				spis += "2"
			elif j == "2":
				spis += "i"
			elif j == "3":
				spis += "б"
			elif j == "4":
				spis += "ъ"
			elif j == "5":
				spis += "k"
			elif j == "6":
				spis += "ю"
			elif j == "7":
				spis += "c"
			elif j == "8":
				spis += "f"
			elif j == "9":
				spis += "р"
			elif j == "0":
				spis += "8"
			elif j == "a":
				spis += "6"
			elif j == "b":
				spis += "я"
			elif j == "c":
				spis += "n"
			elif j == "d":
				spis += "a"
			elif j == "e":
				spis += "e"
			elif j == "f":
				spis += "7"
			elif j == "g":
				spis += "9"
			elif j == "h":
				spis += "t"
			elif j == "i":
				spis += "g"
			elif j == "j":
				spis += "ч"
			elif j == "k":
				spis += "j"
			elif j == "l":
				spis += "y"
			elif j == "m":
				spis += "s"
			elif j == "n":
				spis += "д"
			elif j == "o":
				spis += "0"
			elif j == "p":
				spis += "m"
			elif j == "q":
				spis += "h"
			elif j == "r":
				spis += "l"
			elif j == "s":
				spis += "q"
			elif j == "t":
				spis += "%"
			elif j == "u":
				spis += "z"
			elif j == "v":
				spis += "г"
			elif j == "w":
				spis += "^"
			elif j == "x":
				spis += "е"
			elif j == "y":
				spis += "o"
			elif j == "z":
				spis += "5"
			elif j == "!":
				spis += ")"
			elif j == "@":
				spis += "v"
			elif j == "$":
				spis += "r"
			elif j == "%":
				spis += "="
			elif j == "^":
				spis += "№"
			elif j == "&":
				spis += "w"
			elif j == "*":
				spis += "+"
			elif j == "(":
				spis += "-"
			elif j == ")":
				spis += "#"
			elif j == "_":
				spis += "/"
			elif j == "+":
				spis += "|"
			elif j == "=":
				spis += "_"
			elif j == "-":
				spis += "<"
			elif j == "?":
				spis += ";"
			elif j == ":":
				spis += "@"
			elif j == "№":
				spis += "("
			elif j == '"':
				spis += "?"
			elif j == "/":
				spis += ","
			elif j == ",":
				spis += "!"
			elif j == " ":
				spis += "$"
			elif j == ".":
				spis += "["
		return(spis)
