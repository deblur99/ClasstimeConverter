'''
09:00 ~ 21:00이 1 ~ 18교시까지 30분 단위로, 19~24교시까지 50분 단위로 존재
1~24의 숫자 2개를 입력받고 09시~24시의 시간으로 변환하여 반환 후 출력
'''

day = ''
place = ''
quit_condition = [['q'], ['그만']]

def getTimeArray():
    
    while True:
        global day
        global place

        string = input('').split(' ')

        if string in quit_condition:
            return None

        try:
            day, getTime, place = string[0], string[1:3], string[3:]

            if len(getTime) < 2 or getTime[0] > getTime[-1]:
                print('잘못된 입력입니다. 다시 시도하세요.')
                continue

            for i in range(2): getTime[i] = int(getTime[i])

            if len(getTime) == 2:
                for i in getTime:
                    if i < 1 or i > 24:
                        raise ValueError
            else:
                raise ValueError
        
        except TypeError:
            print('3개 이상의 시간을 입력하셨거나, 입력 예시의 형식과 맞지 않습니다.')
            print('다시 시도하세요.')
            continue
        except ValueError:
            print('3개 이상의 시간을 입력하셨거나, 입력 예시의 형식과 맞지 않습니다.')
            print('다시 시도하세요.')
            continue

        return getTime

def getIsEveningClass(time):
    return time >= 19

#getTime[0] : 시작 시간, getTime[1] : 종료 시간
def calcTime(getTime):
    result = {}

    for time in getTime:
        # for문 내에서 쓰이는 변수 초기화
        rawTime = 0
        init_time = time
        
        # 변수 time의 값이 19교시 이상인지 확인하는 함수를 호출하여 얻은 부울값을 변수에 저장
        isEvening = getIsEveningClass(time)

        if isEvening == True:
            if getTime[0] == time:
                rawTime -= 20
            rawTime += 5 * (time - 19)
            rawTime += 50 * (time - 18)
            time = 18

        # 시작 시간을 연산하는 경우, 끝나는 시간이 아닌 시작하는 시간을 계산해야 하기에
        # classInterval의 값을 하나 덜 곱한다.
        if init_time == getTime[0]:
            rawTime += (time - 1) * 30
        else:
            rawTime += time * 30

        # 결과값을 출력하기 위해 실제 시간으로 계산하는 과정
        # 수업은 9시부터 시작하므로 기본값을 9로 초기화한 변수 actual_hour 선언
        # 분은 위에서 구한 rawTime의 값에서 60을 나눈 나머지 값으로 초기화
        hour = 9
        minute = rawTime % 60

        hour += rawTime // 60

        # 연산 결과를 result에 저장
        if init_time != getTime[-1]:
            result.setdefault('시작 시간', [hour, minute])    
        else:
            result.setdefault('종료 시간', [hour, minute]) 
            
    return result

def printConvertedTime(result):

    for key in result.keys():
        hour = result[key][0]
        minute = result[key][1]

        if (hour // 10) < 1:
            if minute >= 10:
                print(f'{key}: 0{hour}:{minute}')
            else:
                print(f'{key}: 0{hour}:0{minute}')
        else:
            if minute >= 10:
                print(f'{key}: {hour}:{minute}')
            else:
                print(f'{key}: {hour}:0{minute}')

def main():
    print('요일과 시간, 강의장소를 입력하세요.\n입력 예시) 목 12 14 국제210 국제608')
    print('사용이 끝났으면 \'q\' 혹은 \'그만\'을 입력하세요. (\'\' 기호 없이 입력)')

    while True:
        getTime = getTimeArray()
        if getTime != None:
            result = calcTime(getTime)
            printConvertedTime(result)
        else:
            return None

main()