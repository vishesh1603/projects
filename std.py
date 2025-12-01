import numpy as np

def calculate(data):
    """
    Calculates the mean, variance, standard deviation, max, min, and sum 
    of the rows, columns, and elements in a 3x3 matrix.

    Args:
        data (list): A list containing 9 digits.

    Returns:
        dict: A dictionary containing the statistical results.
    """
    
    # --- Input Validation ---
    if len(data) != 9:
        raise ValueError("List must contain nine numbers.")

    # --- Data Preparation ---
    # Convert the list into a 3x3 NumPy array
    matrix = np.array(data).reshape(3, 3)

    # --- Calculations ---
    # Axis 0 (Columns), Axis 1 (Rows), and Flattened (All elements)
    
    # Mean
    mean_axis1 = matrix.mean(axis=0).tolist()
    mean_axis2 = matrix.mean(axis=1).tolist()
    mean_flattened = matrix.mean().tolist()
    
    # Variance
    variance_axis1 = matrix.var(axis=0).tolist()
    variance_axis2 = matrix.var(axis=1).tolist()
    variance_flattened = matrix.var().tolist()
    
    # Standard Deviation
    std_axis1 = matrix.std(axis=0).tolist()
    std_axis2 = matrix.std(axis=1).tolist()
    std_flattened = matrix.std().tolist()
    
    # Max
    max_axis1 = matrix.max(axis=0).tolist()
    max_axis2 = matrix.max(axis=1).tolist()
    max_flattened = matrix.max().tolist()
    
    # Min
    min_axis1 = matrix.min(axis=0).tolist()
    min_axis2 = matrix.min(axis=1).tolist()
    min_flattened = matrix.min().tolist()
    
    # Sum
    sum_axis1 = matrix.sum(axis=0).tolist()
    sum_axis2 = matrix.sum(axis=1).tolist()
    sum_flattened = matrix.sum().tolist()

    # --- Result Formatting ---
    # The results are stored in a dictionary following the specified format
    calculations = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [variance_axis1, variance_axis2, variance_flattened],
        'standard deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }
    
    return calculations


# calculate([0,1,2,3,4,5,6,7,8])


if __name__ == '__main__':
    example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    try:
        results = calculate(example_list)
        print("Input List:", example_list)
        print("\n3x3 Matrix:")
        print(np.array(example_list).reshape(3, 3))
        print("\nCalculations:")
        print(results)
    except ValueError as e:
        print(f"Error: {e}")