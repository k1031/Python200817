s=int(input('請輸入成績:'))
if s>=0 and s<=100:
    if s >=90:
        print("等級A")
    elif s >=80:
        print("等級B")
    elif s >=70:
        print("等級C")
    elif s >=60:
        print("等級D")   
    else:
        print("等級E")
else:
    print("輸入錯誤")