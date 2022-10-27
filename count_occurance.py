# Python code to count the number of occurrences
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count


# Driver Code
lst =list(map(int,input().split()))
x = int(input())
print('{} has occurred {} times'.format(x,
										countX(lst, x)))
