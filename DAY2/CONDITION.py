"""
조건문
<if/else>
js
if 오ole.log("우산쓰셈");
}else{
    console.log("걍가");
}
    if조건:
        창일때 실행할 코드
        else:
            거짓일때 실행할 코드
        -조건:true 또는 false로 답할 수 있는 질문

        <for>
        1번 for i in range(숫자):    
        print("실행할 코드")
        2번    
        for i in range(1,11):
                     이상,미만
            print(i)
        3번
        for i in range(시작,끝,증감):
            실행할 코드
            
        <중요한 부분>
        아래는 모두 같은 코드임
        1
        for i in range(5):
            print("파이썬")
        2
        for i in range(0,5):
                print("파이썬")
        3
        for i in range(0,5,1):
                print("파이썬")
    들여쓰기
    tab 또는 space를 의미
"""


# 오늘날씨 = "비"
# if 오늘날씨 == "비":
#     print("우산쓰셈")
# else:
#     print("그냥가셈")


# for i in range(25, 36):
#     print(i)

for i in range(0, 11, 2):
    print(i)
