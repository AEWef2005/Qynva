# Qynva

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