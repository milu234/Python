'''Write a Program condon.py that reads the first command line argument as a DNA sequence and prints the first
three condons one per line in uppercase letters
'''
import sys
sequence=sys.argv[1]
upper_sequence=sequence.upper()
print(upper_sequence[:3])
print(upper_sequence[3:6])
print(upper_sequence[6:9])