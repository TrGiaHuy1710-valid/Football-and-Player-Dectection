import torch

# Kiểm tra xem PyTorch có được build với CUDA không
print(f"PyTorch built with CUDA: {torch.cuda.is_available()}")

# Nếu có, in ra phiên bản CUDA mà PyTorch đang dùng
if torch.cuda.is_available():
    print(f"PyTorch CUDA version: {torch.version.cuda}")