import threading
import time
import argparse
from api import run_server
from programs import run_program1, run_program2, run_program3, run_program4

def main():
    print("Hello from python-bind!")

    # parse args
    parser = argparse.ArgumentParser(description="python-bind")
    parser.add_argument("--mode", 
                       choices=["api", "programs", "both"], 
                       default="both",
                       help="select mode")
    parser.add_argument("--port", type=int, default=3312, help="API server port")
    args = parser.parse_args()
    
    # thread
    threads = []

    try:
        # programs
        if args.mode in ["programs", "both"]:
            print("start programs...")

            # prog1
            t1 = threading.Thread(target=run_program1, daemon=True, name="Program1")
            t1.start()
            threads.append(t1)

            # prog2
            t2 =threading.Thread(target=run_program2, daemon=True, name="Program2")
            t2.start()
            threads.append(t2)

            # prog3
            t3 = threading.Thread(target=run_program3, daemon=True, name="Program3")
            t3.start()
            threads.append(t3)

            # prog4
            t4 = threading.Thread(target=run_program4, daemon=True, name="Program4")
            t4.start()
            threads.append(t4)

            print("all program start complete")

        if args.mode in ["api", "both"]:
            print("start api...")

            # api
            api_thread = threading.Thread(
                target=run_server,
                kwargs={"host": "0.0.0.0", "port": args.port},
                daemon=True,
                name="APIServer"
            )
            api_thread.start()
            threads.append(api_thread)

            time.sleep(1)  # 서버 시작 대기
            print(f"✅ API 서버 실행 완료: http://localhost:{args.port}")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑shutdown...")

if __name__ == "__main__":
    main()
