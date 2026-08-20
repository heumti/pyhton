# 2) 패키지 내 모듈 미리 임포트
from.graphic.render import render_test
from .sound.echo import echo_test
# 1) 패키지 변수 및 함수 정의
VERSION = 3.5

def print_version_info():
    print(f"THE version of this game is {VERSION}.")

# 3) 패키지 초기화
# 패키지를 처음 import할 떄 초기화 코드가 실행 된다.
print("Initializing game...")