products = []

while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	p = []

	"""
	第1種：
	p.append(name)
	p.append(price)
	products.append(p)
	"""

	"""
	# 第2中
	p = [name, price]
	products.append(p)
	"""
	# 第3中
	products.append([name, price])
	
	
print(products)
# 存取二維list
print(products[0][0])


for p in products: 
	print(p)# 列印出清單中每一個小清單
	print(p[0]) # 每一個小清單的第0個index
	print(p[0], '的價格是', p[1])