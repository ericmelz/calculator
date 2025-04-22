from src.app import add_numbers

def test_add_numbers():
    """Test the add_numbers function with various inputs."""
    # Test with integers
    assert add_numbers(1, 2) == 3
    
    # Test with floats
    assert add_numbers(2.5, 3.5) == 6.0
    
    # Test with negative numbers
    assert add_numbers(-1, -2) == -3
    
    # Test with zero
    assert add_numbers(0, 0) == 0
    
    # Test with mixed types
    assert add_numbers(1, 2.5) == 3.5
