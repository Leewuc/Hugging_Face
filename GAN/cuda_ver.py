import torch
print(torch.__version__)          # 2.2.1+cu121
print(torch.cuda.is_available())  # True 여야 함
print(torch.version.cuda)         # 12.1 출력 (실제 CUDA는 12.7이지만 호환 모드로 동작)