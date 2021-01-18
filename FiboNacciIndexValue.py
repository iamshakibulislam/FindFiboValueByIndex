class fibo:
	counter=2
	lastsum=1
	prev_sum=0
	
	


	def fib_val(self,index):
		
		

		fibo.lastsum,fibo.prev_sum = (fibo.lastsum+fibo.prev_sum),fibo.lastsum
		fibo.counter = fibo.counter+1

		if index == 1:
			return 0
		if index == 2:
			return 1


		if fibo.counter == index:
			return fibo.lastsum

		return fibo().fib_val(index)




check=fibo()
print(check.fib_val(10))

