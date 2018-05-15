numb = int(input("점수 : "))
deg_s = { 10:'A', 9:'A', 8:'B', 7:'C', 6:'D', 5:'F', 4:'F', 3:'F', 2:'F', 1:'F', 0:'F'}

if numb >= 0 and numb <= 100:
      num1 = numb//10
      x = deg_s[num1]
      print(x)
        
else:
      print("입력 가능한 점수 범위는 0~100입니다.")

