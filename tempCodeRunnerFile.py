import random as 무작위

class 랜덤(무작위.Random):
    def 범위(self, 시작, 끝=None, 간격=1):
        if 끝 is None:
            시작, 끝 = 0, 시작
        return self.randrange(시작, 끝, 간격)

def 출력(문자열):
    print(문자열)
def 길이(리스트):
    return len(리스트)

뽑기 = 랜덤()

낭만에미친놈들 = ['태권', '도현', '동환', '주영', '우형']
숫자 = 뽑기.범위(길이(낭만에미친놈들))
출력(낭만에미친놈들[숫자])