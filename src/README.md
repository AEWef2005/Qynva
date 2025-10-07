# Source Code

This directory contains the core source code for the Qynva GPU framework.

## Structure

- `api/` - API implementations and public interfaces
- `optimizers/` - Optimization algorithms and bio-inspired tensor modules
- `backends/` - Hardware-specific implementations
  - `nvidia/` - NVIDIA GPU backend (CUDA)
  - `amd/` - AMD GPU backend (ROCm/HIP)
  - `intel/` - Intel GPU backend (oneAPI/SYCL)