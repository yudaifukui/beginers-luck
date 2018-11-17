import math

def square(x):
	ans = x * x
	return ans

print("2つの数値の計算を行います")
menu = input("メニュー 1:足し算 2：引き算 3：掛け算 4：割り算 5：√ 6：二乗 >> ")
x    = input("数値1(整数) >> ")
y    = input("数値2(整数) >> ") 

print('\n結果')
if menu == '1':
	answer1 = int(x) + int(y)
	print(answer1)
elif menu == '2':
	print()
elif menu == '3':
	answer3 = int(x) * int(y)
	print(answer3)
elif menu == '4':
	print()
elif menu == '5':
	answer_x = math.sqrt(int(x))
	answer_y = math.sqrt(int(y))
	print('数値1:',answer_x)
	print('数値2:',answer_y)
elif menu == '6':
	answer_x = square(int(x))
	answer_y = square(int(y))
	print('数値1:',answer_x)
	print('数値2:',answer_y)
else:
	print("エラー：入力できる数値は1~5です")
