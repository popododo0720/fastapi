#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <string>
#include <vector>
#include <memory>

class HelloWorld {
public:
    HelloWorld() : message_("Hello World from C++20 with pybind11!") {}
    
    void print_hello() {
        std::cout << "🚀 " << message_ << std::endl;
    }
    
    std::string get_message() const {
        return message_;
    }
    
    std::string get_fancy_message() const {
        using namespace std::string_literals;
        auto prefix = "✨ Modern C++20: "s;
        auto content = "auto, lambdas, ranges, and more!"s;
        return prefix + content;
    }
    
    std::vector<std::string> get_messages() const {
        return {
            "Hello from C++20!",
            "pybind11 is awesome!",
            "No more extern C needed!"
        };
    }
    
private:
    std::string message_;
};

// 전역 함수들
void simple_hello() {
    std::cout << "Simple Hello from C++20!" << std::endl;
}

std::string get_cpp_info() {
    return "C++20 with pybind11 binding";
}

PYBIND11_MODULE(hello_cpp, m) {
    m.doc() = "Hello World C++20 pybind11 module";
    
    // 클래스 바인딩
    pybind11::class_<HelloWorld>(m, "HelloWorld")
        .def(pybind11::init<>())
        .def("print_hello", &HelloWorld::print_hello)
        .def("get_message", &HelloWorld::get_message)
        .def("get_fancy_message", &HelloWorld::get_fancy_message)
        .def("get_messages", &HelloWorld::get_messages);
    
    // 전역 함수 바인딩
    m.def("simple_hello", &simple_hello, "Print simple hello");
    m.def("get_cpp_info", &get_cpp_info, "Get C++ info");
}