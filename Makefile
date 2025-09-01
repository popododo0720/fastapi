.PHONY: build-cpp clean run test

# C++ 모듈 빌드
build-cpp:
	@echo "🔧 Building C++ module..."
	cd programs/program4 && uv run python setup.py build_ext --inplace
	@echo "✅ C++ module build complete"

# 정리
clean:
	@echo "🧹 Cleaning build artifacts..."
	find . -name "*.so" -delete
	find . -name "build" -type d -exec rm -rf {} +
	find . -name "*.egg-info" -type d -exec rm -rf {} +
	find . -name "__pycache__" -type d -exec rm -rf {} +
	@echo "✅ Clean complete"

# 실행
run: build-cpp
	@echo "🚀 Starting application..."
	uv run python main.py

# API만 실행
run-api: build-cpp
	@echo "🌐 Starting API server..."
	uv run python main.py --mode api

# 프로그램만 실행
run-programs: build-cpp
	@echo "🔧 Starting programs..."
	uv run python main.py --mode programs

# 테스트
test: build-cpp
	@echo "🧪 Running tests..."
	uv run python -c "from programs.program4 import HelloWorldProgram; p = HelloWorldProgram(); print('Test passed!' if p.hello_module else 'Test failed!')"

help:
	@echo "Available commands:"
	@echo "  build-cpp     - Build C++ pybind11 module"
	@echo "  clean         - Clean build artifacts"
	@echo "  run           - Build and run full application"
	@echo "  run-api       - Build and run API server only"
	@echo "  run-programs  - Build and run programs only"
	@echo "  test          - Test C++ module loading"
	@echo "  help          - Show this help"