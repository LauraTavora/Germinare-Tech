jef = {'swift', 'picpay', 'original', 'jbs', 'friboi', 'J&F'}
jbs = {'swift', 'friboi', 'seara', 'rezende', 'delícia', 'primor', 'doriana', 'massaleve', 'marba'}
unidos = jef | jbs


print(f'Existem {len(jef)} cadastradas no grupo jef')
print(f'existem {len(jbs)} cadastradas no grupo jbs')
print(f'A intersecção entre os dois é: {sorted(unidos)}')
print(f'Os valores que são diferentes é igual a: {sorted(jef.difference(jbs))}')
