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