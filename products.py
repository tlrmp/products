data = []
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品，價格\n')
	for line in f:
		data.append(line)
print(data)

