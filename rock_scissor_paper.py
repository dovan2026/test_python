import random

while True:
    result = input('가위, 바위, 보 중 하나를 입력하세요 (종료하려면 "그만"): ')
    
    # [수정] 컴퓨터가 낼 리스트와 랜덤 선택 코드를 추가합니다.
    list_a = ['가위', '바위', '보']
    a = random.choice(list_a) # 이제 a가 무엇인지 파이썬이 알게 됩니다!

    if result == "그만":
        print("게임을 종료합니다.")
        break

    if result not in list_a:
        print("잘못된 입력입니다. '가위, 바위, 보' 중에 다시 입력하세요.")
        continue # 다시 입력받으러 위로 올라갑니다.

    # 가위인 경우
    if result == "가위":
        print(f'컴퓨터의 선택: {a}')
        if a == "가위":
            print('비겼습니다!')
        elif a == "바위":
            print('컴퓨터가 이겼습니다!')
        else:
            print('당신이 이겼습니다!')
            
    # 바위인 경우
    elif result == "바위":
        print(f'컴퓨터의 선택: {a}')
        if a == "가위":
            print('당신이 이겼습니다!')
        elif a == "바위":
            print('비겼습니다!')
        else:
            print('컴퓨터가 이겼습니다!')
            
    # 보인 경우
    else:
        print(f'컴퓨터의 선택: {a}')
        if a == '가위':
            print('컴퓨터가 이겼습니다!')
        elif a == '바위':
            print('당신이 이겼습니다!')
        else:
            print('비겼습니다.')