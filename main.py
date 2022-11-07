import vigenere
import caesar
import rsa
import numpy as np

##############################
# change values as needed

# Selection of program
program = "rsa" # "caesar", "vigenere", "rsa"

# --- CAESAR ---
csr_text = "qugtmz"
csr_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.'"

csr_a = 7
csr_b = 12


# --- VIGENERE ---
vig_text = "JJGE"
vig_alphabet = "ABCDEFGHIJ"

vig_a = np.array([
    [3, 2],
    [4, 3],
])
vig_b = np.array([6, 5])


# --- RSA ---
rsa_num = 50
# Set RSA keys by either calling get_keys with p and q, or by giving the [(eB, nB), (dA, nA)] pair
# rsa_keys = rsa.get_keys(11, 13)
rsa_keys = ((7, 143), (27, 55))
# rsa_keys = ((77, 187), (29, 133))

rsa_keys_to_check = ((3, 55), (27, 55))
rsa_e_n_to_find_d = (7, 143)

##############################

if program == "caesar":
	csr_ciphered = caesar.cipher(csr_a, csr_b, csr_text, csr_alphabet)
	csr_deciphered = caesar.decipher(csr_a, csr_b, csr_text, csr_alphabet)
	csr_roundtrip = caesar.decipher(csr_a, csr_b, csr_ciphered, csr_alphabet)

	print("\nCaesar ciphering of text: " + csr_text)
	print("==> '" + csr_ciphered + "'")

	print("\nCaesar deciphering of text: " + csr_text)
	print("==> '" + csr_deciphered + "'")

	print("\nCaesar full round-trip ciphering of text: " + csr_text)
	print("==> '" + csr_roundtrip + "'")
	print("==> Same: " + str(csr_roundtrip == csr_text))


if program == "vigenere":
	vig_ciphered = vigenere.cipher(vig_a, vig_b, vig_text, vig_alphabet)
	vig_deciphered = vigenere.decipher(vig_a, vig_b, vig_text, vig_alphabet)
	vig_roundtrip = vigenere.decipher(vig_a, vig_b, vig_ciphered, vig_alphabet)

	print("\nVigenere ciphering of text: " + vig_text)
	print("==> '" + vig_ciphered + "'")

	print("\nVigenere deciphering of text: " + vig_text)
	print("==> '" + vig_deciphered + "'")

	print("\nVigenere full round-trip ciphering of text: " + vig_text)
	print("==> '" + vig_roundtrip + "'")
	print("==> Same: " + str(vig_roundtrip == vig_text))


if program == "rsa":
	rsa_encrypted = rsa.encrypt(rsa_num, rsa_keys[0])
	rsa_decrypted = rsa.decrypt(rsa_num, rsa_keys[1])
	rsa_check = rsa.check_keys(rsa_keys_to_check)
	rsa_missing_d = rsa.find_d(*rsa_e_n_to_find_d)

	print("\nRSA encryption of text: " + str(rsa_num))
	print("==> '" + str(rsa_encrypted) + "'")

	print("\nRSA decryption of text: " + str(rsa_num))
	print("==> '" + str(rsa_decrypted) + "'")

	print("\nRSA check keys: " + ("Success" if rsa_check[0] else ("Fail (" + rsa_check[1] + ")")))

	print("\nMissing d: " + str(rsa_missing_d))
