import torch
if torch.backends.mps.is_available():
    print("Success! AutoSentry can use the M1 GPU via MPS.")
else:
    print("MPS not found. Using CPU.")