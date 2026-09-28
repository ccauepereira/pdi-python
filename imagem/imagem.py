import numpy as np
import matplotlib.pyplot as plt

imagem = np.array([
    [10,40,80,120],
    [20, 60, 100, 140],
    [30, 80, 120, 180],
    [50, 90, 160, 255]
], dtype=np.uint8)

#q2 alterar pixel
imagem[2,3] = 255
plt.imshow(imagem, cmap = "gray",vmin = 0,vmax = 255)
plt.colorbar()
plt.show()

print("\nShape: ", imagem.shape) #1x4x4
print("\nDimensões: ", imagem.ndim) #2
print("\nTipo: ", imagem.dtype) #uint 8
print("\nMinimo: ", imagem.vmin()) #10
print("\nMaximo: ",imagem.vmax()) # 255
print("\nImagem 2 por 3: ",imagem[2, 3]) # linha 2 e coluna 3 - 180

