"""
자판기를 만드시오:
자판기에는 총 3개의 음료가 있습니다.
솔의 눈(10원), 민트초코 라떼(8원), 데자와(11원)
각 음료는 2개씩의 재고가 남아 있습니다.
사용자는 1000원의 돈을 가지고 있습니다.
자판기는 한 번에 하나의 음료만을 뽑을 수 있습니다.
프로그램은 특정 종료 명령 혹은 음료가 다 떨어졌을 때 종료됩니다.

종료 명령 ex) ‘exit’ 입력 시 프로그램 종료

* 음료가 복사되거나 없는 곳으로부터 생성되지 않습니다. 없는 음료가 투출되지 않습니다. 돈을 따따블로 수금해가지 않습니다. 어느 종류의 오류도 허용되지 않습니다.
"""
vending_Machine_menu = ["솔의 눈", "민트초코 라떼", "데자와"]
vending_Machine_remain = {vending_Machine_menu[0]: 2, vending_Machine_menu[1]: 2, vending_Machine_menu[2]: 2}
vending_Machine_price = {vending_Machine_menu[0]: 10, vending_Machine_menu[1]: 8, vending_Machine_menu[2]: 11}
vending_Machine_remain_total = len(vending_Machine_remain) * 2  # 재고가 2개씩 이라는 설정에 기반한 수식

customer_wallet = 1000
customer_input = ""  # string 설정

while(vending_Machine_remain_total != 0) :
    print("\n현재 당신의 보유 금액: " + str(customer_wallet))
    print("솔의 눈(" + str(vending_Machine_remain[vending_Machine_menu[0]]) + "개, 가격: " + str(vending_Machine_price[vending_Machine_menu[0]]) +
          "), 민트초코 라떼(" + str(vending_Machine_remain[vending_Machine_menu[1]]) + "개, 가격: " + str(vending_Machine_price[vending_Machine_menu[1]]) +
          "), 데자와(" + str(vending_Machine_remain[vending_Machine_menu[2]]) + "개, 가격: " + str(vending_Machine_price[vending_Machine_menu[1]]) + ")")
    customer_input = input("자판기에서 뽑을 음료를 선택하세요(exit 입력으로 종료): ")
    if(customer_input == 'exit'):
        break
    elif(customer_input == vending_Machine_menu[0] or customer_input == vending_Machine_menu[1] or customer_input == vending_Machine_menu[2]):
        if(vending_Machine_remain[customer_input] != 0 and customer_wallet >= vending_Machine_price[customer_input]):
            vending_Machine_remain[customer_input] -= 1
            vending_Machine_remain_total -= 1
            customer_wallet -= vending_Machine_price[customer_input]
            print("성공적으로 구매했습니다.")
        else:
            print("재고 부족")
    else:
        print("입력에 오류가 있습니다.")
print("\n이용해주셔서 감사합니다.\n")
