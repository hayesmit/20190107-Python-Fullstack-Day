# rot-cypher.py
alphabet = 'abcdefghijklmnopqrstuvwxyz'
rot13 	 = 'nopqrstuvwxyzabcdefghijklm'

def encode13(message):
	"""
	encodes message with ROT-13
	:message: str
	returns message rotated forwards by 13

	>>> encode13('abc def123')
	'nop qrs123'
	"""
	output = ''
	for char in message:
		if char in alphabet:
			idx = alphabet.index(char)
			encoded_char = rot13[idx]
			output += encoded_char
		else:
			output += char
		# # if you used dictionaries
		# output += rot13.get(char, char)
	return output 


def decode13(message):
	"""
	decodes message with ROT-13
	:message: str
	returns message rotated backwards by 13
	
	>>> decode13('nop qrs123')
	'abc def123'
	"""
	output = ''
	for char in message:
		if char in rot13:
			idx = rot13.index(char)
			decoded_char = alphabet[idx]
			output += decoded_char
		else:
			output += char
	return output 	 


def encode(message, n):
	"""
	encodes message with ROT-n
	:message: str
	:n: int to rotate by
	returns message rotated forwards by n

	>>> encode('abc', 1)
	'bcd'

	>>> encode('xyz', 1)
	'yza'
	"""
	output = ''
	for char in message:
		if char in alphabet:
			# encode by n
			idx = alphabet.index(char)
			encoded_char = alphabet[(idx+n)%26]
			output += encoded_char
		else:
			output += char
	return output


def decode(message, n):
	"""
	decodes message with ROT-n
	:message: str
	:n: int to rotate by
	returns message rotated backwards by n

	>>> decode('abc', 1)
	'zab'

	>>> decode('abc', 52)
	'abc'
	"""
	output = ''
	for char in message:
		if char in alphabet:
			idx = alphabet.index(char)
			decoded_char = alphabet[(idx-n) % 26]
			output += decoded_char
		else:
			output += char			
	return output

def main():
	print('Welcome to the ROT cypher')
	while True:
		while True: # validate operation 
			op = input('Do you want to (d)ecode or (e)ncode: ').lower().strip()
			if op in ['d', 'decode', 'e', 'encode']:
				break

		while True: # validate n
			try:
				n = int(input('Enter your rotation number: '))
				break
			except ValueError:
				pass

		message = input('Enter the message you want coded: ').lower().strip()

		if op.startswith('d'): # decode
			print(decode(message, n))
		else: # encode 
			print(encode(message, n))

		while True: # play again
			play_ag = input('Do you want to try again: ').lower().strip()
			if play_ag in ['y', 'yes', 'n', 'no']:
				break

		if play_ag.startswith('n'):
			break	

main()
