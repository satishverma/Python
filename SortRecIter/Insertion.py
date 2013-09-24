from random import randrange

#Insertion Sort : First n-1 are sorted and insert the nth in the right place

def insertionSortRec(seq,i):
	if i==1: return
	else: insertionSortRec(seq,i-1)
	if i>1:
		curr=i-1
		index=i-2
		while index>=0:
			if seq[curr]<seq[index]:
				seq[curr],seq[index]=seq[index],seq[curr]
				curr = curr-1
				index= index-1
			else:
				index=index-1

		
		
		



if __name__=="__main__":
	seq = [randrange(100) for i in range(25)]
	seqCopy=seq
	print("Before Sort")
	print(seq)
	insertionSortRec(seq,len(seq))
	print("After Sort")
	print(seq)

	seqCopy.sort()
	#print("Correct")
	#print(seq)
