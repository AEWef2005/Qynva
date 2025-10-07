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