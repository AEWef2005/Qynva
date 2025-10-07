# Qynva

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