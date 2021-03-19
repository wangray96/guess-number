import random
start = input('請決定猜數字遊戲開始的數字：')
end = input('請決定猜數字遊戲結束的數字:')
start = float(start)
end = float(end)

r = random.randint(start,end)
count = 0
while True:
	count = count + 1
	num = input('請決定一個數字')
	num = float(num)
	if num == r:
		print('這是你猜的第', count, '次了')
		print('猜了那麼久 你終於猜對啦 下次加油好嗎')
		break
	elif num > r:
		print('笨蛋猜錯啦 沒事猜那麼大幹嘛啦')
	elif num < r:
		print('白癡喔猜很久誒 沒事不要猜麽小可以嗎')
	print('這是你猜的第', count, '次了')




