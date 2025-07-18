balance =  50000
receipts = []

while True:
    num=input("원하는 기능의 번호를 선택해주세요. 1.입금 2.출금 3.영수증 보기 4.종료: ")

    if num == '4': # 4번 종료기능
        break #while문 종료 
    if num == '1': #입금 기능 구현 -> feat/deposit 브랜치에서 작업
        deposit_amount = int(input('입금할 금액을 입력해주세요: '))
        balance += deposit_amount #balunce = balunce + deposit_amount 랑 같음
        print(f'입금하신 금액은 {deposit_amount}원 이고 현재 잔액은 {balance}원 입니다. ')
        receipts.append( ('입금', deposit_amount, balance) )

    if num == '2':
        withdrew_amount = int(input('출금할 금액을 입력해주세요. '))
        withdrew_amount = min(balance,withdrew_amount)
        balance -= withdrew_amount
        print(f'출금하신 금액은{withdrew_amount}원 이고 현재 잔액은 {balance}원 입니다. ') 
        receipts.append(( '출금',withdrew_amount,balance ))
    if num == '3':
        if receipts:
            for i in receipts:
                print(f"{i[0]}: {i[1]}원 | 잔액: {i[2]}")
        else:
            print("영수증 내역이 없습니다. ")
            
print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.')