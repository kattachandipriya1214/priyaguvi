str=raw_input()
if str in('a' 'e' 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U'):
	print("Vowel")
elif((str>='a' and str<='z') or (str>='A' and str='Z')):
	print("Invalid")
else:
	print("Consonant")
