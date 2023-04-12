def main():
	n = input("Enter a number: ")
	largest = 1
	for x in range(1, int(n)):
		if (isPrime(x)):
			largest = x
   
	print("Largest prime number <=", n, ":", largest)

def isPrime(n):
	# Corner case
	if (n <= 1):
		return False

	# Check from 2 to sqrt(n)
	for i in range(2, int(n ** 0.5)+1):
		if (n % i == 0):
			return False
	return True
  
if __name__ == "__main__":
  	main()