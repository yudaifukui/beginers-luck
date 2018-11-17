print("2つの数値の計算を行います")
menu = input("メニュー 1:足し算 2：引き算 3：掛け算 4：割り算 >>")
x    = input("数値1 >> ")
y    = input("数値2 >> ") 

if menu == '1':
	answer1 = int(x) + int(y)
	print(answer)
elif menu == '2':
	print()
elif menu == '3':

elif menu == '4':
	print()
else:
	print("エラー：入力できる数値は1~4です")
