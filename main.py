import vigenere
import caesar
import numpy as np

##############################
# change values as needed
vig_text = "JJGE"
vig_alphabet = "ABCDEFGHIJ"

vig_a = np.array([
	[3, 2],
	[4, 3],
])
vig_b = np.array([6, 5])


csr_text = "qugtmz"
csr_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.'"

csr_a = 7
csr_b = 12
# end of values setting
##############################

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

print("\n\n---")

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
