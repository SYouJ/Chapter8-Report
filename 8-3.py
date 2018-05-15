numb = int(input("점수 : "))

if numb >= 0 and numb <= 100:
      if numb >= 90 and numb <= 100:
            print(numb,":","A")
      elif numb >= 80 and numb <= 89:
            print(numb,":","B")
      elif numb >= 70 and numb <= 79:
            print(numb,":","C")
      elif numb >= 60 and numb <= 69:
            print(numb,":","D")
      elif numb >= 0 and numb <= 59:
            print(numb,":","F")
else:
      print("입력 가능한 점수 범위는 0~100입니다.")
