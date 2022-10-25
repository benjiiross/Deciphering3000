import numpy as np

# Computes the inverse of a 2x2 matrix in an equivalence class Z/nZ
def inv(matrix, base):
	det = int(np.linalg.det(matrix))
	if det == 0:
		raise ValueError("Determinant is 0")

	det %= base

	new_matrix = np.array([
		[matrix[1][1], -matrix[0][1]],
		[-matrix[1][0], matrix[0][0]],
	])

	det = pow(det, -1, base)
	new_matrix *= (det % base)

	for i in range(2):
		for j in range(2):
			new_matrix[i][j] %= base

	return new_matrix

def cipher(a, b, plain_text, alphabet):
	key_map = {alphabet[i]: i for i in range(len(alphabet))}
	inversed_key_map = {v: k for k, v in key_map.items()}

	pgram = len(b)

	plain_text = plain_text.upper()

	chunks = [plain_text[i:i+pgram] for i in range(0, len(plain_text), pgram)]

	result_str = ""
	for chunk in chunks:
		char_matrix = np.array([key_map[char] for char in chunk])
		result = np.dot(a, char_matrix) + b
		result_str += "".join([inversed_key_map[int(i % len(alphabet))] for i in result])

	return result_str

def decipher(a, b, ciphered_text, alphabet):
	key_map = {alphabet[i]: i for i in range(len(alphabet))}
	inversed_key_map = {v: k for k, v in key_map.items()}

	pgram = len(b)

	ciphered_text = ciphered_text.upper()

	ainv = inv(a, len(alphabet))

	# Calculates - (A^-1 * B)
	second_part = np.dot(-ainv, b) % len(alphabet)

	# Splits the input message into p-grams (multiples messages)
	chunks = [ciphered_text[i:i+pgram] for i in range(0, len(ciphered_text), pgram)]

	result_str = ""
	for chunk in chunks:
		char_matrix = np.array([key_map[char] for char in chunk])

		result_vector = np.dot(ainv, char_matrix) + second_part

		codes = [inversed_key_map[int(code % len(alphabet))] for code in result_vector]
		result_str += "".join(codes)

	return result_str