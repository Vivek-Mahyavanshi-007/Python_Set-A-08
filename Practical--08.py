fh=open('Output.txt','w')

#Ascending order

abc=list(input("Enter Numbers into the list : "))
fh.write('Ascending order ==> \n')
print("Before sorting",abc)
fh.write('Before Sorting'+str(abc))
abc.sort()
print("after sorting ",abc)
fh.write('\n')
fh.write('After Sorting'+str(abc))
fh.write('\n')

#Descending order 

abcd=list(input("Enter Numbers into the list : "))
fh.write('\nDescending order ==> \n')
print("before sorting , a= ",abcd)
fh.write('Before Sorting'+str(abcd))
fh.write('\n')
abcd.sort(reverse=True)
print("after sorting, a = ",abcd)
fh.write('After Sorting'+str(abcd))
fh.close()