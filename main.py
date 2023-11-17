#Amirreza_Soheili_97463133
def dist(X, Y):
	(m, n) = (len(X), len(Y))

	T = [[0 for x in range(n + 1)] for y in range(m + 1)]

	for i in range(1, m + 1):
		T[i][0] = i

	for j in range(1, n + 1):
		T[0][j] = j

	for i in range(1, m + 1):

		for j in range(1, n + 1):
			if X[i - 1] == Y[j - 1]:
				cost = 0
			else:
				cost = 1

			T[i][j] = min(T[i - 1][j] + 1,  	# deletion
						T[i][j - 1] + 1,		# insertion
						T[i - 1][j - 1] + cost) # replace

	return T[m][n]

X = input("Enter your first string : ")
Y = input("Enter your second string : ")

print("\nYour first input is : /",X,"/")
print("Your second input is : /",Y,"/")

if __name__ == '__main__':
	print("And The Levenshtein distance is ", dist(X, Y)," .")
if dist(X, Y) == 0:
		print("They are the same.")