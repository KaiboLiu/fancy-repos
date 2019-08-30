import torch
from torch.autograd import Variable

N, D = 3, 4

x = Variable(torch.randn(N, D).cuda(), requires_grad=True)
y = Variable(torch.randn(N, D).cuda(), requires_grad=True)
z = Variable(torch.randn(N, D).cuda(), requires_grad=True)


a = x * y
b = a + z
c = torch.sum(b)

c.backward()

print(x, x.grad.data)
print(y, y.grad.data)
print(z, z.grad.data)

print(a, a.grad.data)
print(b, b.grad.data)
print(c, c.grad.data)