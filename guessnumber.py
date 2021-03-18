import random
r = random.randint(1,100)
answer = 25
while True:
	a = input('猜猜看數字是多少？')
	a = float(a)
	if a == answer:
		print('恭喜猜對了')
		break
	else:
		if a < 25:
			print('哈哈哈 妳猜錯了誒','比答案還小')
		if a > 25:
		    print('哈哈哈 妳猜錯了誒','比答案還大')