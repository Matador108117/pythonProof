from primos import is_primo
# generar la lista de numeros primos que existe entre 1 y 50
primos_50 = [n for n in range(1, 51) if is_primo(n)]
print (primos_50)
