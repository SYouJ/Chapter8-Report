deg_i = {"라면":650, "우유":1100, "콜라":1200, "캔커피":500, "과자":700}
dsum = 0

while True:
      stc = input("제품명 : ")
      if stc in deg_i:
            d = deg_i[stc]
            dsum += d
            print("[",stc,":",d,"] >",dsum)
            
      elif stc not in deg_i:
            if len(stc) == 0 :
                  print("총 금액 :", dsum)
                  break
            else:
                  print(stc,"는 미등록 제품입니다.")
            
     

