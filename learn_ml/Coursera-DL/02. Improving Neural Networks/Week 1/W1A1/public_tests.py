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


def initialize_parameters_zeros_test(target):
    layer_dims = [3,2,1]
    expected_output = {'W1': np.array([[0., 0., 0.],
        [0., 0., 0.]]),
 'b1': np.array([[0.],
        [0.]]),
 'W2': np.array([[0., 0.]]),
 'b2': np.array([[0.]])}
    
    test_cases = [
        {
            "name":"datatype_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error":"Datatype mismatch"
        },
        {
            "name": "shape_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong shape"
        },
        {
            "name": "equation_output_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong output"
        }
    ]
    
    multiple_test(test_cases, target)
    
def initialize_parameters_random_test(target):
    layer_dims = [3,2,1]
    expected_output = {'W1': np.array([[ 17.88628473,   4.36509851,   0.96497468],
        [-18.63492703,  -2.77388203,  -3.54758979]]),
 'b1': np.array([[0.],
        [0.]]),
 'W2': np.array([[-0.82741481, -6.27000677]]),
 'b2': np.array([[0.]])}
    
    test_cases = [
        {
            "name":"datatype_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error":"Datatype mismatch"
        },
        {
            "name": "shape_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong shape"
        },
        {
            "name": "equation_output_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong output"
        }
    ]
    
    multiple_test(test_cases, target)
    
def initialize_parameters_he_test(target):
    
    layer_dims = [3, 1, 2]
    expected_output = {'W1': np.array([[1.46040903, 0.3564088 , 0.07878985]]), 
                       'b1': np.array([[0.]]), 
                       'W2': np.array([[-2.63537665], [-0.39228616]]), 
                       'b2': np.array([[0.],[0.]])}
    
    
    test_cases = [
        {
            "name":"datatype_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error":"Datatype mismatch"
        },
        {
            "name": "shape_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong shape"
        },
        {
            "name": "equation_output_check",
            "input": [layer_dims],
            "expected": expected_output,
            "error": "Wrong output"
        }
    ]
    
    multiple_test(test_cases, target)