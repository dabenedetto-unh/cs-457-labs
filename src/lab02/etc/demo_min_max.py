# 3. test_min_max_scaler
def min_max_scaler(value, min_val, max_val):
    """
    Scales a value to a range between 0 and 1.
    Concept: Data Normalization.
    """
    # Handling edge case: Avoid division by zero if min and max are the same
    if max_val == min_val:
        return 0.0
    
    scaled_value = (value - min_val) / (max_val - min_val)
    return scaled_value

def inverse_min_max_scaler(scaled_value, min_val, max_val):
    """
    Reconstructs the original value from a min-max scaled value.
    """
    original_value = scaled_value * (max_val - min_val) + min_val
    return original_value

if __name__ == "__main__":
    values = [10, 20, 30, 40, 50]
    min_val = min(values)
    max_val = max(values)
    
    scaled_values = [min_max_scaler(v, min_val, max_val) for v in values]
    print(f"Original values: {values}")
    print(f"Scaled values: {scaled_values}")

    reconstructed_values = [inverse_min_max_scaler(scaled_value, min_val, max_val) for scaled_value in scaled_values]
    print(f"Reconstructed values: {reconstructed_values}")