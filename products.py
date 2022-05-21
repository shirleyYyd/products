products = []

# 讀取檔案
with open('products.csv', 'r') as f:
	for line in f:
		# 想要跳過欄位名稱的字串
		if '商品, 價格' in line:
			#都只能在迴圈裡 break-跳出迴圈 ，continue-跳掉下一迴
			continue
		# 字串後面有'\n'，使用stirp()出掉換行符號（\n）
		name, price = line.strip().split(',') #split 切割 
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = int(input('請輸入商品價格： ') )
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
	

# 印出所有購買記錄	
print(products)
# 存取二維list
print(products[0][0])

# 寫入檔案
for p in products: 
	print(p)# 列印出清單中每一個小清單
	print(p[0]) # 每一個小清單的第0個index
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品, 價格\n')#加欄位名稱
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n' ) #4個字串合併在一起為一個字串
		#csv檔若沒有,區隔會變成1格