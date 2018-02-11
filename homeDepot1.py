

class Solution:
	def anagramIsExpected(self):
		foundChars = {}

		for i in self.expected:
			if foundChars.get(i):
				foundChars[i] += 1
			else:
				foundChars[i] = 1

		for i in self.anagram:
			if(foundChars.get(i)):	
				foundChars[i] -=1
				if(foundChars[i] == 0):
					del foundChars[i]
			else:
				return False

		if(len(foundChars) >0):
			return False
		else:
			return True

	def __init__(self, expected, anagram):
		self.expected = expected
		self.anagram = anagram

def main():
	import sys

	while 1:
		try:
			print("enter expected")
			line = sys.stdin.readline()
			print("Enter anagram")
			line2 = sys.stdin.readline()
			sol = Solution(line,line2)
			ret = sol.anagramIsExpected()
			print(ret)
		except KeyboardInterrupt:
			break
		if not line:
			break

main()