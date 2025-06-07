# 📦 Inclu++ — Remote-Aware C++ Preprocessor

**Inclu++** (`inclupp`) is a command-line tool that enhances your C++ workflow by allowing you to `#include` header files **directly from URLs**, just like local files.

🔗 `#include "https://example.com/hello.hpp"`  
📥 Automatically downloaded and compiled with your source code.

---

## ✨ Features

- 🔍 Detects `#include` directives with URLs
- 💻 Works for both `C` and `C++` source files  
- 🌐 Downloads remote header files on the fly  
- 🗂 Stores them in a temporary directory  
- ⚙️ Compiles using `g++` behind the scenes  
- 🎨 Colorful CLI output with live status messages  
- ✅ Simple and lightweight — no setup needed  

---

## 🚀 Quick Start

```bash
pip install inclupp
```

```bash
inclupp main.cpp
```

---

## 🧪 Example

### `main.cpp`

```cpp
#include "https://example.com/hello.hpp"

int main() {
    hello();
    return 0;
}
```

```bash
inclupp main.cpp
```

```
🔧 Processing source file: main.cpp
🔄 Downloading: https://example.com/hello.hpp
✅ Saved to: /tmp/tmpabc123/hello.hpp
🔨 Compiling the processed file...
🎉 Compilation successful: main
```

---

## 🔧 Usage

```bash
inclupp --version
inclupp <source_file.c or .cpp>
```

---

## 📦 Requirements

- Python 3.6+
- `g++` in PATH
- Internet connection
- Python packages: `requests`, `colorama`

---

## 📘 License

MIT License  
© 2025 LautyDev
