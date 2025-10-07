# Qynva

[![Build and Test](https://github.com/AEWef2005/Qynva/actions/workflows/build.yml/badge.svg)](https://github.com/AEWef2005/Qynva/actions/workflows/build.yml)
[![Linting](https://github.com/AEWef2005/Qynva/actions/workflows/lint.yml/badge.svg)](https://github.com/AEWef2005/Qynva/actions/workflows/lint.yml)
[![Cross-Platform Testing](https://github.com/AEWef2005/Qynva/actions/workflows/test.yml/badge.svg)](https://github.com/AEWef2005/Qynva/actions/workflows/test.yml)
[![GPU Validation](https://github.com/AEWef2005/Qynva/actions/workflows/gpu-validation.yml/badge.svg)](https://github.com/AEWef2005/Qynva/actions/workflows/gpu-validation.yml)

## CI/CD Pipeline

This repository includes comprehensive CI/CD workflows:

### 🏗️ Build and Test (`build.yml`)
- **Multi-OS Support**: Ubuntu Latest and Ubuntu 20.04
- **GPU Matrix**: NVIDIA, AMD, and CPU-only configurations
- **GPU Drivers**: Automatic installation of NVIDIA Docker and ROCm support
- **Build Artifacts**: Generated and uploaded for each configuration

### 🔍 Linting (`lint.yml`)
- **Multi-Language**: Python, JavaScript/TypeScript, Shell, YAML, Markdown
- **Tools**: flake8, black, isort, mypy, ESLint, Prettier, ShellCheck, yamllint
- **Security**: File permission and structure validation

### ✅ Cross-Platform Testing (`test.yml`)
- **Operating Systems**: Ubuntu, Windows, macOS
- **Python Versions**: 3.8, 3.9, 3.10, 3.11
- **Node.js Versions**: 16, 18, 20
- **Test Types**: Unit tests, integration tests, security scans
- **Coverage**: Codecov integration

### 🚀 GPU Validation (`gpu-validation.yml`)
- **GPU Types**: NVIDIA CUDA and AMD ROCm
- **CUDA Versions**: 11.8, 12.0
- **ROCm Versions**: 5.4.3, 5.5.1
- **Performance**: Benchmarking and compatibility testing
- **Frameworks**: PyTorch, TensorFlow support validation

## Features

- **GPU Acceleration**: Support for both NVIDIA and AMD GPUs
- **Cross-Platform**: Compatible with Linux, Windows, and macOS
- **Comprehensive Testing**: Automated testing across multiple environments
- **Code Quality**: Automated linting and formatting checks
- **Security**: Built-in security scanning and validation
**Agentic LLM Framework for Automated Development**

Qynva is an advanced development framework that leverages AI agents to automate 70-80% of the software development workflow. Our intelligent agents collaborate to plan, code, test, and review implementations, dramatically accelerating development while maintaining high code quality.

## 🤖 AI-Powered Development

Qynva employs specialized AI agents that work together to handle complex development tasks:

- **🧠 Planner Agent**: Analyzes requirements and creates detailed development plans
- **⚡ Coder Agent**: Generates production-ready code in multiple languages  
- **🧪 Tester Agent**: Creates comprehensive test suites with high coverage
- **🔄 Router Agent**: Orchestrates workflows and manages agent coordination

## ✨ Key Features

- **Automated Workflow**: Complete plan → code → test → review cycles
- **Multi-LLM Support**: Works with Grok, GPT-4, Claude, and other providers
- **Language Agnostic**: Supports Python, JavaScript, Rust, C++, and more
- **Quality Assurance**: Built-in code review and testing standards
- **GitHub Integration**: Seamless integration with GitHub workflows
- **Community Driven**: Open source with comprehensive contribution guidelines

## 🚀 Quick Start

### 1. Setup

```bash
# Clone the repository
git clone https://github.com/AEWef2005/Qynva.git
cd Qynva

# Run the setup script
python setup_agents.py
```

### 2. Configure API Keys

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API keys
GROK_API_KEY=your-grok-api-key
OPENAI_API_KEY=your-openai-api-key  
CLAUDE_API_KEY=your-claude-api-key
```

### 3. Run Your First Workflow

```bash
# Execute a complete development workflow
python agents/router.py workflow "Create a REST API for user management" --language python

# Or use individual agents
python agents/planner.py "Design a microservice architecture"
python agents/coder.py "Implement JWT authentication" --language python
python agents/tester.py src/auth.py --type unit
```

## 📖 Documentation

- **[Complete Workflow Guide](docs/llm-workflow.md)** - Detailed documentation of the agentic framework
- **[Agent Reference](agents/)** - Individual agent documentation and usage
- **[Configuration Guide](agents/configs/)** - Setup and configuration options
- **[Contributing Guidelines](.github/ISSUE_TEMPLATE/)** - How to contribute to the project

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Planner Agent  │────│  Coder Agent    │────│  Tester Agent   │
│  📋 Planning    │    │  ⚡ Coding      │    │  🧪 Testing     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │  Router Agent   │
                    │  🔄 Orchestration│
                    └─────────────────┘
```

## 🛠️ Development Workflow

1. **Plan**: Describe your task in natural language
2. **Generate**: AI agents create code, tests, and documentation
3. **Review**: Human-in-the-loop validation and approval
4. **Deploy**: Automated integration with version control

### Example Workflow

```bash
# Complete automated workflow
python agents/router.py workflow "Build a chat application with real-time messaging"

# This will:
# 1. 📋 Plan the application architecture
# 2. ⚡ Generate backend and frontend code  
# 3. 🧪 Create comprehensive tests
# 4. 📝 Generate documentation
# 5. 🔄 Stage changes for review
```

## 🎯 Use Cases

- **Rapid Prototyping**: Go from idea to working prototype in minutes
- **Code Generation**: Generate boilerplate and complex implementations
- **Test Automation**: Create comprehensive test suites automatically
- **Documentation**: Generate and maintain up-to-date documentation
- **Code Review**: Automated code quality analysis and suggestions

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

- 🐛 [Report bugs](/.github/ISSUE_TEMPLATE/bug_report.md)
- ✨ [Request features](/.github/ISSUE_TEMPLATE/feature_request.md)  
- 🤖 [Improve agents](/.github/ISSUE_TEMPLATE/agent_improvement.md)
- 📖 Improve documentation
- 🧪 Add test coverage

## 📊 Project Status

- **MVP**: ✅ Basic agent framework implemented
- **Beta**: 🔄 Cross-platform support and advanced features
- **Release 1.0**: 🎯 Production-ready with full documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Community

- ⭐ Star the repository to show your support
- 🐦 Follow updates on our social channels
- 💬 Join discussions in GitHub Issues
- 🤝 Connect with other developers using Qynva

---

**Powered by AI Agents** 🤖 | **Built for Developers** 👩‍💻👨‍💻 | **Open Source** 🌍
A C++ project focused on bio-tensor optimization and helical tensor structures.

## Branching Strategy (Git Flow)

This project follows the Git Flow branching model:

### Branch Structure

- **`main`**: Stable releases only. All code on main should be production-ready.
- **`develop`**: Integration branch for features. New features are merged here for testing.
- **Feature branches**: Use the pattern `feature/<descriptive-name>` (e.g., `feature/bio-tensor-opt`, `feature/helical-tensor-structure`).

### Branch Protection

The `main` branch is protected and requires:
- Pull request reviews before merging
- Status checks to pass
- Up-to-date branches before merging

## Workflow

### Creating a New Feature

```bash
# Start from develop branch
git checkout develop
git pull origin develop

# Create a new feature branch
git checkout -b feature/your-feature-name

# Work on your feature...
# Make commits following conventional commit format

# Push your feature branch
git push origin feature/your-feature-name

# Create a Pull Request to merge into develop
```

### Example Feature Branch

```bash
git checkout develop
git checkout -b feature/bio-tensor-opt
# Work on bio-tensor optimization
git push origin feature/bio-tensor-opt
```

## Commit Best Practices

Use **Conventional Commits** for semantic versioning and clear history:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Commit Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Build process or auxiliary tool changes

### Examples

```bash
git commit -m "feat: Add helical tensor structure implementation"
git commit -m "fix: Resolve memory leak in bio-tensor optimization"
git commit -m "docs: Update API documentation for tensor operations"
git commit -m "refactor: Simplify tensor calculation algorithm"
```

## Build System

This project uses **CMake** for build management.

### Dependencies

Dependencies are fetched at build time using CMake's `FetchContent`. Do not commit binaries or third-party libraries to the repository.

### Building

```bash
# Create build directory
mkdir build && cd build

# Configure with CMake
cmake ..

# Build the project
cmake --build .

# Run tests
ctest
```

### Build Configuration

- **Debug build**: `cmake -DCMAKE_BUILD_TYPE=Debug ..`
- **Release build**: `cmake -DCMAKE_BUILD_TYPE=Release ..`

## Project Structure

```
Qynva/
├── CMakeLists.txt          # Main CMake configuration
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── include/                # Header files
├── src/                    # Source files
├── tests/                  # Test files
└── build/                  # Build output (not committed)
```

## Development Guidelines

1. **Small, focused commits**: Each commit should represent a single logical change
2. **Clear commit messages**: Use conventional commit format
3. **Test your changes**: Ensure all tests pass before pushing
4. **Code review**: All changes to `main` require pull request review
5. **Keep dependencies minimal**: Only add dependencies that are essential

## Getting Started

1. Clone the repository
2. Switch to the `develop` branch: `git checkout develop`
3. Create your feature branch: `git checkout -b feature/your-feature`
4. Build the project: `mkdir build && cd build && cmake .. && cmake --build .`
5. Make your changes and commit using conventional commit format
6. Push and create a pull request
