import time
from core import message_hub

class TimeProgram:
    """시간 출력 프로그램"""
    def __init__(self):
        self.program_name = "program2"
    
    def start(self):
        """프로그램 시작"""
        print("⏰ 프로그램 2 시작 (시간 출력기)")
        
        while True:
            # 메시지 확인
            message = message_hub.get_message(self.program_name)
            if message:
                current_time = time.strftime("%H:%M:%S")
                print(f"⏰ 프로그램 2: {message} - 현재 시간: {current_time}")
            
def run():
    """프로그램 실행 함수"""
    program = TimeProgram()
    program.start()