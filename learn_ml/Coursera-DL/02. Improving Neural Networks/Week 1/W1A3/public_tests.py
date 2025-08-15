import numpy as np

def single_test(test_case, target):
    """Helper function to run a single test case"""
    try:
        result = target(*test_case["input"])
        if test_case["name"] == "datatype_check":
            assert type(result) == type(test_case["expected"]), test_case["error"]
        elif test_case["name"] == "shape_check":
            assert result.shape == test_case["expected"].shape, test_case["error"]
        elif test_case["name"] == "equation_output_check":
            assert np.allclose(result, test_case["expected"], rtol=1e-7), test_case["error"]
        print(f"\033[92m✓ {test_case['name']} passed!")
        return True
    except Exception as e:
        print(f"\033[91m✗ {test_case['name']} failed: {e}")
        return False

def multiple_test(test_cases, target):
    """Helper function to run multiple test cases"""
    passed = 0
    total = len(test_cases)
    for test_case in test_cases:
        if single_test(test_case, target):
            passed += 1
    
    print(f"\n\033[94m{passed}/{total} tests passed!")
    if passed == total:
        print("\033[92mAll tests passed!")
    else:
        print("\033[91mSome tests failed!")

def forward_propagation_test(target):
    x, theta = 2, 4
    expected_output = 8
    test_cases = [
        {
            "name": "equation_output_check",
            "input": [x, theta],
            "expected": expected_output,
            "error": "Wrong output"
        } 
    ]
    
    single_test(test_cases, target) 
        
def backward_propagation_test(target):
    x, theta = 3, 4
    expected_output = 3
    test_cases = [
        {
            "name": "equation_output_check",
            "input": [x, theta],
            "expected": expected_output,
            "error": "Wrong output"
        } 
    ]
    
    single_test(test_cases, target)

def gradient_check_test(target, difference):
    x, theta = 3, 4
    expected_output = 7.814075313343006e-11
    
    tolerance = 1e-12
    assert np.abs(expected_output - difference) < tolerance, "You are not using np.linalg.norm for numerator or denominator"
    
    test_cases = [
        {
            "name": "equation_output_check",
            "input": [x, theta],
            "expected": expected_output,
            "error": "Wrong output"
        } 
    ]
    
    single_test(test_cases, target)
    
    
def predict_test(target):
    np.random.seed(1)
    X = np.random.randn(2, 3)
    parameters = {'W1': np.array([[-0.00615039,  0.0169021 ],
        [-0.02311792,  0.03137121],
        [-0.0169217 , -0.01752545],
        [ 0.00935436, -0.05018221]]),
     'W2': np.array([[-0.0104319 , -0.04019007,  0.01607211,  0.04440255]]),
     'b1': np.array([[ -8.97523455e-07],
        [  8.15562092e-06],
        [  6.04810633e-07],
        [ -2.54560700e-06]]),
     'b2': np.array([[  9.14954378e-05]])}
    expected_output = np.array([[True, False, True]])

    test_cases = [
        {
            "name":"datatype_check",
            "input": [parameters, X],
            "expected": expected_output,
            "error":"Data type mismatch"
        },
        {
            "name": "shape_check",
            "input": [parameters, X],
            "expected": expected_output,
            "error": "Wrong shape"
        },
        {
            "name": "equation_output_check",
            "input": [parameters, X],
            "expected": expected_output,
            "error": "Wrong output"
        } 
    ]
    
    single_test(test_cases, target)

    
