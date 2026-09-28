import numpy as np
import matplotlib.pyplot as plt

imagem = np.array([
    [0, 50, 100, 150],
    [25, 75, 125, 175],
    [50, 100, 150, 200],
    [75, 125, 200, 255]
    ], dtype=np.uint8)

print("Imagem: ")
print(imagem)

print("\nShape: ", imagem.shape)
print("Numero de dimensões: ", imagem.ndim)
print("Tipo dos dados: ",imagem.dtype)
print("Menor intensidade: ", imagem.min())
print("Maior intensidade: ", imagem.max())

print("\nPixel [1,2]: ", imagem[1,2])

plt.imshow(imagem, cmap="gray", vmin=0, vmax=255)
plt.colorbar()
plt.show()
