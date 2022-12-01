from hashlib import md5

def h(s):
	return md5(s.encode()).hexdigest()

if __name__ == "__main__":
	s = input()

	i = 0
	while True:
		i += 1
		if h(s + str(i)).startswith("000000"):
			print(i)
			break
