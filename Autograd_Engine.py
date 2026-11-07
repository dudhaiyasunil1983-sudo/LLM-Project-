import torch

x=torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y=x*x+3*x

print(y)