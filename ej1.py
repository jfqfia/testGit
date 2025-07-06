# Python factorial

def f(n):
	if n <= 1:
		return n
	else:
		return n * f(n-1)


n = input("Introduce un valor: ")
fn = f(int(n))
print(f"{n}! = {fn}")
