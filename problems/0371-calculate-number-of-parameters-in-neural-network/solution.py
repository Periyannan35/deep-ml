def calculate_parameters(layers: list[dict]) -> int:
    """
    Calculate the total number of trainable parameters in a neural network.

    Args:
        layers: List of dictionaries, each describing a layer.

    Returns:
        Total number of trainable parameters (int).
    """
    # Your code here
    sum=0
    for layer in layers:
        if layer['type']=='dense':
            sum+=layer["input_size"]*layer["output_size"] + (layer["output_size"] if layer.get('bias',True) else 0)
        elif layer['type']=='conv2d':
            sum+=layer["in_channels"]*layer["out_channels"]*(layer['kernel_size']**2) + (layer["out_channels"] if layer.get("bias",True) else 0)
    return sum
    pass