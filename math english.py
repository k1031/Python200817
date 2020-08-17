a=float(input("英文成績:"))
b=float(input("數學成績:"))
if a>=0 and a<=100 and b>=0 and b<=100:
    if a >=90 and b>=90:
        print("有獎品")
    elif a <=60 or b<=60:
        print('加油')
    elif a <=60 and b<=60:
        print('有處罰')
    else:
        print('no')
else:
    print("輸入錯誤")