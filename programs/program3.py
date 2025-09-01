import time
import random
from core import message_hub

class RandomProgram:
    """랜덤 숫자 생성 프로그램"""
    def __init__(self):
        self.program_name = "program3"
    
    def start(self):
        """프로그램 시작"""
        print("🎲 프로그램 3 시작 (랜덤 숫자 생성기)")
        
        while True:
            # 메시지 확인
            message = message_hub.get_message(self.program_name)
            if message:
                random_num = random.randint(1, 100)
                print(f"🎲 프로그램 3: {message} - 생성된 숫자: {random_num}")
            
def run():
    """프로그램 실행 함수"""
    program = RandomProgram()
    program.start()