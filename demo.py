a = 1 # int
b = 1.1 # float
c = 'a' # char(명시적)
d = "string" # string
e = True # bool

a = 20
#print(a ** 3)
a **= 2
#print(a)

a = 2
k = 10

a = k

#print(str(a))
p = 2
t = ['안녕하세요', '반갑습니다']
t[0] = ['안녕하지 않네요','저는']

t.append("죄송합니다")
t.remove(['안녕하지 않네요','저는'])

print(t)

t2 = [
    [1, 4],
    [2, 3]
]
#print(t2[1][0])

#print(t[1])
#print((t[0])[1])
#print(t[0] + ' ' + t[1])

#print(a > k)
#print(a < k)
#print(a <= k)
#print(a >= k)
#print(a == k)

a = (b, c)
#a[0], a[1]


d = {a: '다람쥐', '비문학': '지옥'}

a = '다람쥐'

#print(d[a])

str1 = "wiryeHanbit"

#print(str1.upper()) # str에 저장되지 않은 채 str의 값 중 소문자를 대문자로 변환
#print(str1.lower()) # str에 저장되지 않은 채 str의 값 중 대문자를 소문자로 변환
#print(str1) # 즉, 휘발성 함수


#print(len(str))

#a = input("현민이는: ")
#str1 = input("학교는: ")
#print(a == '다람쥐' and str1 == '4')
#print(int(str1) + 1)
#k = int(str1)
#print(str(k) + '1')

#
# if a == '다람쥐' or a == '하늘다람쥐' :
#     print("진리")
#     if str1 == "wiryeHanbit" :
#         print("또다른 진리")
#
# elif a == '물고기' :
#     print('거짓')
#
# else :
#     print('또다른 거짓')
#

a = 1
while (a == 3) :
    print(a)
    a += 1