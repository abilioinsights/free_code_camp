# Vector Operations / Operações com Vetores

This Python project implements classes for 2D, 3D, and n-dimensional vectors, with common vector operations such as addition, subtraction, dot product, cross product (for 3D vectors), normalization, and angle calculation.

Este projeto Python implementa classes para vetores 2D, 3D e n-dimensionais, com operações comuns de vetores, como adição, subtração, produto escalar, produto vetorial (para vetores 3D), normalização e cálculo de ângulo.

## Features / Funcionalidades
- **2D Vector (R2Vector):** Represents a 2D vector with components x and y. / Representa um vetor 2D com componentes x e y.
- **3D Vector (R3Vector):** Represents a 3D vector with components x, y, and z, inheriting from R2Vector. / Representa um vetor 3D com componentes x, y e z, herdando de R2Vector.
- **n-Dimensional Vector (RNVector):** Represents an n-dimensional vector with arbitrary components. / Representa um vetor n-dimensional com componentes arbitrários.
- **Operations:** Addition, subtraction, dot product, cross product (3D only), normalization, and angle calculation. / Operações: Adição, subtração, produto escalar, produto vetorial (apenas 3D), normalização e cálculo de ângulo.

## How to Use / Como Usar

1. Create a 2D Vector: / Criando um vetor 2D:
```py
v1 = R2Vector(x=2, y=3)
```

2. Create a 3D Vector: / Criando um vetor 3D:

```py
v2 = R3Vector(x=1, y=2, z=3)
```

3. Create an n-Dimensional Vector: / Criando um n-dimensional V(n)

```py
v3 = RNVector(1, 2, 3, 4)
```

4. Perform Operations: / Operações de execuções:

```py
v_sum = v1 + v2  # Vector addition / Adição de vetores
v_diff = v1 - v2  # Vector subtraction / Subtração de vetores
dot_product = v1 * v2  # Dot product / Produto escalar
cross_product = v2.cross(v3)  # Cross product (3D only) / Produto vetorial (apenas 3D)
norm = v1.norm()  # Vector norm / Norma do vetor
unit_vector = v1.normalize()  # Normalized vector / Vetor normalizado
angle = v1.angle(v2)  # Angle between vectors / Ângulo entre vetores
```

## Example / Exemplo

```py
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)

print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')

v4 = v1 - v2
print(f'v1 - v2 = {v4}')

v5 = v1 * v2
print(f'v1 * v2 = {v5}')

v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')

v7 = RNVector(1, 2, 3, 4)

v8 = RNVector(2, 3, 4, 5)
print(f'v7 = {v7}')
print(f'v8 = {v8}')

v9 = v7 + v8
print(f'v7 + v8 = {v9}')

v10 = v7 * v8
print(f'v7 * v8 = {v10}')
```

## Requirements / Requisitos
Python 3.x

## How to Contribute / Como Contribuir
- Fork the repository. / Faça um fork do repositório.
- Create a branch for your feature: git checkout -b minha-feature. / Crie uma branch para sua feature.
- Commit your changes: git commit -m 'Adicionei uma nova feature'. / Commit suas mudanças.
- Push to the branch: git push origin minha-feature. / Push para a branch.
- Open a pull request and describe your changes. / Abra um pull request e descreva suas mudanças.

## License / Licença
This project is licensed under the MIT License. See the LICENSE file for details.

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
