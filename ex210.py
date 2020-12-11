#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 210
def message1():            # A를 출력하는 것을 message1이라는 함수로 지정한다
    print("A")             # 
    
def message2():            # B를 출력하는 것을 message2라는 함수로 지정한다.
    print("B")             # 

def message3():            # message3이라는 함수를 지정-------------------------ㅣ
    for i in range(3):     # 3번 반복하는 변수 i를 지정 -------ㅡㅣ            ㅣ
        message2()          # message2() --> B를 출력            ㅣ--> for문   ㅣ--> message3의 함수
        print("C")          # C를 출력하라 ---------------------ㅣ            ㅣ
    message1()              # message1() --> A를 출력------------------------ㅣ

message3()                  # message3() --> (B C) * 3 A

