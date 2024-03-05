S = 18 # 10010
idx = 4

if S & (1 << idx) :
	print("해당 idx : ", idx, "가 켜져있다")
else:
	print("해당 idx : ", idx, "가 꺼져있다")