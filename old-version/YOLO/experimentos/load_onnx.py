def load_onnx(fname:str="model_test/weights/best.onnx"):
    import onnx

    # Load the ONNX model
    model = onnx.load(fname)
    
    return model



