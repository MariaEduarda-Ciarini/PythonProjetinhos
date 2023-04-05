from pandas import DataFrame

# dict

dt = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
      'Ano': [2004, 2005, 2006, 2007, 2008],
      'Taxa de Desemprego': [0.5, 2.5, 3.5, 5.0, 1.5]}
print(dt)

# Convertendo dict em DataFrame

Dfrm = DataFrame(dt)
print(Dfrm.head())

print(type(Dfrm))

# Organizando as columns

print(DataFrame(dt, columns= ['Estado', 'Taxa de Desemprego', 'Ano']))

print(Dfrm.dtypes)

# Criando outro dataframe

Newdt2 = DataFrame(dt,
                 columns = ['Estado', 'Taxa de Desemprego', 'IDH', 'Ano'],
                 index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])
print(Newdt2)

print(Newdt2.dtypes)
print(Newdt2.columns)
print(Newdt2.values)

#  Chama uma coluna do Data Frame

print(Newdt2['IDH'])

# Imprimindo duas colunas

print(Newdt2[['Ano', 'Taxa de Desemprego']])

# Filtrando

print(Newdt2.filter(items= ['Estado'], axis = 1))

print(Newdt2.filter(items= ['estado3'], axis = 0))


