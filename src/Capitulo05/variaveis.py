var_global = 10

def multiplica_numeros(num1, num2):
    var_global = num1 * num2
    print(var_global)
    var_local = 9+4

multiplica_numeros(10, 20)

print(var_global)

#Erro pq ela é local da função
print(var_local)