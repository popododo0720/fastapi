import time
from core import message_hub

class CounterProgram:
    """카운터 프로그램"""
    def __init__(self):
        self.program_name = "program1"
        self.counter = 0
    
    def start(self):
        """프로그램 시작"""
        print("🔢 프로그램 1 시작 (카운터)")
        
        while True:
            # 메시지 확인
            message = message_hub.get_message(self.program_name)
            if message:
                print(f"🔢 프로그램 1: {message} - 현재 카운트: {self.counter}")
                self.counter += 1

def run():
    """프로그램 실행 함수"""
    program = CounterProgram()
    program.start()