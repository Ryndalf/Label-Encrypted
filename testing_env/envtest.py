import concrete.numpy as cnp
from sklearn.metrics.pairwise import euclidean_distances
import torch
import torchvision
import torchvision.transforms as transforms
from torchvision.transforms.functional import to_pil_image
import numpy as np
import pandas as pd

print('Checking the package concrete...')
@cnp.compiler({"x": "encrypted", "y": "encrypted"})
def add(x, y):
    return x + y

inputset = [(2, 3), (0, 0), (1, 6), (7, 7), (7, 1), (3, 2), (6, 1), (1, 7), (4, 5), (5, 4)]
circuit = add.compile(inputset)
res = circuit.encrypt_run_decrypt(2, 6)

if res == 8:
    print('Package concrete has been installed successfully.')
    flag_concrete = 1
else:
    print('Package concrete fails to install')
    flag_concrete = 0

print('Checking the package torch ...')
a = torch.tensor(2)
b = torch.tensor(6)
result = a + b
if result.item() == 8:
    print('Package torch has been installed successfully.')
    flag_torch = 1
else:
    print('Package torch fails to install')
    flag_torch = 0

print('Checking the package torchvision ...')
random_image_tensor = torch.rand(1, 3, 224, 224)
transform = transforms.Compose([
    transforms.Resize((128, 128))
])
pil_image = to_pil_image(random_image_tensor.squeeze(0))
transformed_pil_image = transform(pil_image)
transformed_image_tensor = torchvision.transforms.functional.to_tensor(transformed_pil_image).unsqueeze(0)
if transformed_image_tensor.shape == (1, 3, 128, 128):
    print("Package torchvision has been installed successfully.")
    flag_torchvision = 1
else:
    print("Package torchvision fails to install")
    flag_torchvision = 0

print("Checking the package sklearn...")
point_1 = [[1]]
point_2 = [[2]]
distance = euclidean_distances(point_1, point_2)
if distance == 1:
    print("Package sklearn has been installed successfully")
    flag_sklearn = 1
else:
    print("Package sklearn fails to install")
    flag_sklearn = 0

print("Checking the package numpy and pandas ..")
np_result = np.array([1, 2]) + np.array([3, 4])
pd_result = pd.Series([1, 2]) + pd.Series([3, 4])
if np_result is not None and pd_result is not None:
    print("Package numpy and pandas has been installed successfully")
    flag_nppd = 1
else:
    print("Package numpy and pandas fail to install")
    flag_nppd = 0

if flag_nppd == flag_sklearn == flag_torchvision == flag_torch == flag_concrete == 1:
    print("All key packages have been installed successfully")
else:
    print("Not all key packages have been installed successfully")