import time
import sys
import os
from core import message_hub

class HelloWorldProgram:
    """pybind11을 사용한 C++20 Hello World 프로그램"""
    def __init__(self):
        self.program_name = "program4"
        self.hello_module = None
        self.hello_world_obj = None
        self._load_cpp_module()
    
    def _load_cpp_module(self):
        """C++ pybind11 모듈 로드"""
        try:
            # 모듈 경로 추가
            current_dir = os.path.dirname(os.path.abspath(__file__))
            module_dir = os.path.join(current_dir, "program4")
            if module_dir not in sys.path:
                sys.path.insert(0, module_dir)
            
            # pybind11 모듈 임포트
            import hello_cpp
            self.hello_module = hello_cpp
            self.hello_world_obj = hello_cpp.HelloWorld()
            
            print("✅ C++ pybind11 모듈 로드 성공")
            print(f"📋 모듈 정보: {hello_cpp.get_cpp_info()}")
            
        except ImportError as e:
            print(f"❌ C++ 모듈 로드 실패: {e}")
            print("컴파일이 필요합니다:")
            print("pip install pybind11")
            print("또는 수동 컴파일:")
            print("g++ -O3 -Wall -shared -std=c++20 -fPIC `python3 -m pybind11 --includes` programs/program4/hello.cc -o programs/program4/hello_cpp`python3-config --extension-suffix`")
            self.hello_module = None
    
    def start(self):
        """프로그램 시작"""
        print("🚀 프로그램 4 시작 (C++20 pybind11 Hello World)")
        
        if not self.hello_module:
            print("❌ C++ 모듈이 로드되지 않았습니다.")
            return
        
        while True:
            # 메시지 확인
            message = message_hub.get_message(self.program_name)
            if message:
                print(f"🚀 프로그램 4: {message}")
                
                # C++ 객체 메서드 호출
                self.hello_world_obj.print_hello()
                
                # 다양한 C++ 함수 호출
                cpp_message = self.hello_world_obj.get_message()
                print(f"📨 C++에서 받은 메시지: {cpp_message}")
                
                fancy_message = self.hello_world_obj.get_fancy_message()
                print(f"✨ 고급 메시지: {fancy_message}")
                
                # 벡터 반환 테스트
                messages = self.hello_world_obj.get_messages()
                print("📋 여러 메시지들:")
                for i, msg in enumerate(messages, 1):
                    print(f"  {i}. {msg}")
                
                # 전역 함수 호출
                self.hello_module.simple_hello()
            
            time.sleep(0.1)  # CPU 사용률 조절

def run():
    """프로그램 실행 함수"""
    program = HelloWorldProgram()
    program.start()