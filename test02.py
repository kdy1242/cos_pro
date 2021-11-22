'''
A 쇼핑몰에서는 회원 등급에 따라 할인 서비스를 제공합니다. 회원 등급에 따른 할인율은 다음과 같습니다. (S = 실버, G =골드, V = VIP)

등급      할인율
"S"      5%
"G"      10%
"V"      15%

상품의 가격 price 와 구매자의 회원 등급을 나타내는 문자열 grade 가 매개변수로 주어질 때,
할인 서비스를 적용한 가격을 return 하도록 solution 함수를 완성해주세요.

매개변수 설명
상품의 가격 price 와 회원 등급 grade 가 매개변수로 주어집니다.
* price 는 100 이상 100,000 이하의 100단위 자연수입니다.
* grade 는 "S", "G", "V" 세 가지 중 하나입니다.

return 값 설명
할인한 가격을 return 하도록 solution 함수를 작성해주세요.

예시 및 설명
price     grade    return
2500       "V"      2125
96900      "S"      92055

예시 #1 2500원의 15%는 375원 입니다. 2500 - 375 = 2125 입니다.
예시 #2 96900원의 5%는 4845원 입니다. 96900 - 4845 = 92055 입니다.
'''


# 다음과 같이 import를 사용할 수 있습니다.
# import math


# 여기에 코드를 작성해주세요.
def solution(price, grade):
    answer = 0

    if grade == "S":
        answer = int(price * 0.95)
    if grade == "G":
        answer = int(price * 0.9)
    if grade == "V":
        answer = int(price * 0.85)

    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")