ek_dict = dict()

while True:
      stc_e = input("영어 단어 : ")
      stc_k = input("한글 단어 : ")
      if len(stc_e) > 0 or len(stc_k) >0:
            ek_dict[stc_e] = stc_k
            
      if len(stc_e) == 0 or len(stc_k) == 0:
            print(ek_dict)
            break
            
     

