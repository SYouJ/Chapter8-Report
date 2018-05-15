ek_dict = dict()

while True:
      stc_e = input("영어 단어 : ")
      if len(stc_e) == 0:
            print(ek_dict)
            break

      if len(stc_e) > 0 :
            if stc_e in ek_dict and ek_dict != dict():
                  print(stc_e,":",ek_dict[stc_e])
                  continue
      
      if ek_dict == dict():
            print("사전이 비어있습니다.")
            print("단어를 추가합니다")
            ek_dict[stc_e] = stc_e
      
      if len(stc_e) > 0 :
            if stc_e not in ek_dict:
                  print(stc_e,"단어가 등록되어 있지 않습니다.")
                  print("단어를 추가합니다.")
            ek_dict[stc_e] = stc_e

            
      stc_k = input("한글 단어 : ")
      
      if len(stc_k) >0:
            ek_dict[stc_e] = stc_k
            
     
            
     

