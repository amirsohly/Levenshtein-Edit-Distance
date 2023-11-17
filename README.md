# Levenshtein-Edit-Distance
This code calculates the Levenshtein distance between two input strings.

![Screenshot](https://github.com/amirsohly/Levenshtein-Edit-Distance/assets/47668516/b76f2d56-703b-41e2-a574-0d473694e92d)


## 1
The dist function takes two input strings, X and Y, and calculates their Levenshtein distance. The Levenshtein distance is the minimum number of operations (insertion, deletion, or substitution) required to transform one string into another.
## 2
The function initializes a matrix T with dimensions (m + 1) x (n + 1), where m and n are the lengths of strings X and Y, respectively. Each element T[i][j] represents the Levenshtein distance between the substrings X[0:i] and Y[0:j].
## 3
The function fills in the first row and column of T with incremental values from 0 to m and 0 to n, respectively. These values represent the minimum number of operations required to transform an empty string into the corresponding substring.
## 4
The function iterates over the remaining elements of T and calculates the minimum cost of transforming X[0:i] into Y[0:j]. The cost is 0 if the corresponding characters in X and Y are the same, and 1 otherwise. The minimum cost is determined by taking the minimum of three operations: deletion (T[i-1][j] + 1), insertion (T[i][j-1] + 1), and replacement (T[i-1][j-1] + cost).
## 5
Finally, the function returns the Levenshtein distance between the two input strings, which is stored in T[m][n].
## 6
The code prompts the user to enter two strings, X and Y, and then calls the dist function to calculate their Levenshtein distance.
## 7
The code prints the input strings and the calculated Levenshtein distance.
## 8
If the Levenshtein distance is 0, indicating that the two strings are identical, the code prints a message stating that they are the same.
