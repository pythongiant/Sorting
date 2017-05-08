arr=[32,3,1,2,3,4,1,2,3]
sorted_arr=[]
x=len(arr)
while len(sorted_arr) is not x:
	sorted_arr.append(min(arr))
	arr.remove(min(arr))
print (sorted_arr)