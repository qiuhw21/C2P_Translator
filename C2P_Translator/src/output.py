def calculate(s):
	result = 0
	num = 0
	sign = 1
	i = 0
	while i < len(s):
		c = s[i]
		if c >= '0' and c <= '9':
			tmp = 0
			if c == '0':
				tmp = 0
			if c == '1':
				tmp = 1
			if c == '2':
				tmp = 2
			if c == '3':
				tmp = 3
			if c == '4':
				tmp = 4
			if c == '5':
				tmp = 5
			if c == '6':
				tmp = 6
			if c == '7':
				tmp = 7
			if c == '8':
				tmp = 8
			if c == '9':
				tmp = 9
			num = 10 * num + tmp
		if c == '+':
			result = result + sign * num
			num = 0
			sign = 1
		if c == '-':
			result = result + sign * num
			num = 0
			sign = - 1
		i += 1
	result = result + sign * num
	return result
def main():
	expression = "1 + 2 - 3"
	print("Result: %d\n", calculate(expression))
	return 0
if __name__ == '__main__':
	main()
