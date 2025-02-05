import torch
from diffusers import StableDiffusionPipeline

# 모델 로드
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16,
    use_auth_token=""
).to("cuda")

# 이미지 생성
image = pipe("a futuristic robot painting a sunset").images[0]
image.save("robot_painter.png")