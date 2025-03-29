def preencheBinario(binario):
	for i range(8-len(binario)):
		binario = str(0) + binario
	return binario

def decimalBinario(decimal):
	binario = ""
	while (decimal > 0):
		resto = decimal % 2
		binario = str (resto) + binario
		decimal = decimal // 2
	return binario

def dividirIP (ip): # para dividir o ip
	s = " " 
	lista = []
	for i in range(len(ip)):
		if (ip[ip] != "."):
			s = s + ip[i]
		else:
			l.append(int(s))
			s = " "
	l.append (int(s))
	return lista


def main(args):
	ip = "192.186.0.1"
	binario = []
	lista = dividirIP(ip)
	for i in range(len(lista)):
		binario.append(preencheZero(decimalBinario(lista[i])))
	print (lista)
	print (binario)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
