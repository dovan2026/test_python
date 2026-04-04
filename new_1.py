#베스킨 라빈스 31 게임 만들기
print("게임 시작!")
#coun1에 0을 세팅하고 시작해야함
count1 = 0
while True:
    # input에 숫자만 넣을 것
    result = input('숫자 몇 개를 부를 건가요? (1~3):')
    # input에 게임 규칙인 1, 2, 3만 반영되도록 설정
    if result not in ["1","2","3"]:
        print("오류입니다. 1~3을 입력하세요.")
        continue # 넘어가기
    else:
        for i in range(0, int(result)): # int로 하지 않으면 input의 결과 str이 그대로 반영됨
            count1 += 1 # for loop로 count1이 계속 1씩 증가하도록 설정
            print(count1, "!") # 외치는 느낌의 !도 삽입
            if count1 >= 31: # 순번이 31이 되면 break
                break
    if count1 >= 31: # else break 후 순번을 그대로 넘겨받아 31이 되었는지 확인 후 print 실행
        print("벌칙 당첨!!")
        break