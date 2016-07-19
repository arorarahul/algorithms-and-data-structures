def karatsuba_multiplication(first_number, second_number):
	
	#checking if length is equal to one commute it using regular 3rd grade algorithm taught in schools
	if(len(str(first_number)) == 1 or len(str(second_number)) == 1):
		
		return first_number*second_number
	
	else:

		n = max(len(str(first_number)),len(str(second_number)))

		n_by_2 = n/2

		a = int(first_number / 10**(n_by_2))

		b = first_number % 10**(n_by_2)

		c = int(second_number / 10**(n_by_2))

		d = second_number % 10**(n_by_2)

		#calling function recursively to break length further till it reaches 1
		ac = karatsuba_multiplication(a, c) 
		bd = karatsuba_multiplication(b, d)

		ad_plus_bc = karatsuba_multiplication(a+b, c+d) - ac - bd

		#karatsuba formula as a function of n
		final_answer = ac*10**(2*(n_by_2)) + ad_plus_bc*10**(n_by_2) + bd

		return final_answer


x = int(raw_input("enter first number"))
y = int(raw_input("enter second number"))

final = karatsuba_multiplication(x,y);

print final