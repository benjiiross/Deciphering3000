import numpy as np

def cipher(a, b, plain_text, alphabet):
	key_map = {alphabet[i]: i for i in range(len(alphabet))}
	inversed_key_map = {v: k for k, v in key_map.items()}

	plain_text = plain_text.upper()

	cipher_text = ""

	for char in plain_text:
		code = a * key_map[char] + b
		cipher_text += inversed_key_map[code % len(alphabet)]

	return cipher_text


def decipher(a, b, cipher_text, alphabet):
	key_map = {alphabet[i]: i for i in range(len(alphabet))}
	inversed_key_map = {v: k for k, v in key_map.items()}

	cipher_text = cipher_text.upper()

	plain_text = ""

	for char in cipher_text:
		ainv = pow(a, -1, len(alphabet))
		code = ainv * key_map[char] - ainv * b
		plain_text += inversed_key_map[code % len(alphabet)]

	return plain_text
