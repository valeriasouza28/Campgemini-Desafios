escada1 = '     ' + '*'
print(escada1)
escada2 = '    ' + '**'
print(escada2)
escada3 = '   ' + '***'
print(escada3)
escada4 = '  ' + '****'
print(escada4)
escada5 = ' ' + '*****'
print(escada5)
escada6 = '******'
print(escada6)

Altura_da_escada = escada6[-1], escada5[-1], escada4[-1], escada3[-1], escada2[-1], escada1[-1]
print('\n A altura da escada é de ', len(Altura_da_escada))

base_da_escada = len(escada6)
print('\n A base da escada é de ', base_da_escada)

TemEspacoNaBase = escada6.find(' ', base_da_escada)
if TemEspacoNaBase == -1:
  print('\n', TemEspacoNaBase,' Não Tem Espaço Na Base da escada ✅')

#curiosidades
Tamanho_Escada6 = len(escada6)
print('\nO tamanho da escada de 6 * é de ', Tamanho_Escada6)
Tamanho_Escada5 = len(escada5)
print('O tamanho da escada de 5 * é de ', Tamanho_Escada5)

Tamanho_Escada4 = len(escada4)
print('O tamanho da escada de 4 * é de ', Tamanho_Escada4)

Tamanho_Escada3 = len(escada3) 
print('O tamanho da escada de 3 * é de ', Tamanho_Escada3)

Tamanho_Escada2 = len(escada2)
print('O tamanho da escada de 2 * é de ', Tamanho_Escada2)

Tamanho_Escada1 = len(escada1)
print('O tamanho da escada de 1 * é de ', Tamanho_Escada1)