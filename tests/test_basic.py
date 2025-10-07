#!/usr/bin/env python3
"""
Basic test suite for Qynva project.
These tests validate the CI/CD pipeline and basic functionality.
"""

import unittest
import sys
import os


class TestBasicFunctionality(unittest.TestCase):
    """Test basic functionality and environment setup."""

    def test_python_version(self):
        """Test that Python version is supported."""
        self.assertGreaterEqual(sys.version_info.major, 3)
        self.assertGreaterEqual(sys.version_info.minor, 8)

    def test_basic_arithmetic(self):
        """Test basic arithmetic operations."""
        self.assertEqual(1 + 1, 2)
        self.assertEqual(2 * 3, 6)
        self.assertEqual(10 / 2, 5.0)

    def test_environment_variables(self):
        """Test that required environment variables are accessible."""
        # These should always be available
        self.assertIsNotNone(os.environ.get('PATH'))
        self.assertIsNotNone(os.getcwd())

    def test_imports(self):
        """Test that standard library imports work."""
        import json
        import datetime
        import collections
        
        # Test JSON functionality
        test_data = {"test": "value", "number": 42}
        json_str = json.dumps(test_data)
        self.assertIsInstance(json_str, str)
        
        # Test datetime
        now = datetime.datetime.now()
        self.assertIsInstance(now, datetime.datetime)

    def test_file_operations(self):
        """Test basic file operations."""
        test_file = "/tmp/test_qynva.txt"
        test_content = "Hello, Qynva CI/CD!"
        
        # Write test file
        with open(test_file, 'w') as f:
            f.write(test_content)
        
        # Read test file
        with open(test_file, 'r') as f:
            content = f.read()
        
        self.assertEqual(content, test_content)
        
        # Clean up
        os.remove(test_file)


class TestCIPipelineCompatibility(unittest.TestCase):
    """Test CI pipeline compatibility."""

    def test_exit_codes(self):
        """Test that proper exit codes are used."""
        # Success case
        result = os.system('true')
        self.assertEqual(result, 0)

    def test_directory_structure(self):
        """Test that expected directory structure exists."""
        # Check for important directories
        self.assertTrue(os.path.exists('.github'))
        self.assertTrue(os.path.exists('.github/workflows'))
        
        # Check for workflow files
        workflow_files = [
            '.github/workflows/build.yml',
            '.github/workflows/test.yml',
            '.github/workflows/lint.yml',
            '.github/workflows/gpu-validation.yml'
        ]
        
        for workflow_file in workflow_files:
            self.assertTrue(os.path.exists(workflow_file), 
                          f"Workflow file {workflow_file} should exist")

    def test_readme_exists(self):
        """Test that README.md exists and has content."""
        self.assertTrue(os.path.exists('README.md'))
        
        with open('README.md', 'r') as f:
            content = f.read()
        
        self.assertGreater(len(content), 0)
        self.assertIn('Qynva', content)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)