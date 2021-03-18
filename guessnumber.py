import random
r = random.randint(1,100)
answer = 63
count = 0
while True:
	count += 1
	a = input('猜猜看數字是多少？')
	a = float(a)
	if a == answer:
		print('恭喜猜對了')
		print('這是你猜的第', count ,'次了 請再接再厲')
		break
	else:
		if a < 63:
			print('哈哈 兄弟給力點 你猜錯了 猜那麼小幹嘛')
		if a > 63:
		    print('哈哈 你猜錯了 是想猜幾次啊 沒事別猜那麼大可以嗎')
	print('這是你猜的第', count ,'次了誒加油好嘛')