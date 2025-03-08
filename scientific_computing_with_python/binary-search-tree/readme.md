# Binary Search Tree (BST) / Árvore Binária de Busca (BST)

This Python implementation provides a Binary Search Tree (BST) with basic operations such as insertion, search, deletion, and inorder traversal.

Esta implementação em Python fornece uma Árvore Binária de Busca (BST) com operações básicas como inserção, busca, remoção e travessia em ordem.

## Features / Funcionalidades
- **Insertion:** Adds a new key to the BST. / Adiciona uma nova chave à BST.
- **Search:** Finds a key in the BST. / Encontra uma chave na BST.
- **Deletion:** Removes a key from the BST. / Remove uma chave da BST.
- **Inorder Traversal:** Returns the keys in ascending order. / Retorna as chaves em ordem crescente.

## How to Use / Como Usar

##  1. **Insertion:**
  
   ```python
   bst = BinarySearchTree()
   bst.insert(50)
   bst.insert(30)
   bst.insert(70)
   ```

  ## 2. Search:
```py
result = bst.search(30)
if result:
    print("Key found:", result.key)  # Output: Key found: 30
else:
    print("Key not found")
```

  ## 3. Deletion:

```py
bst.delete(30)
```

## Inorder Traversal:

```py
print(bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]
```

## Example / Exemplo
```py
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)

print('Search for 80:', bst.search(80))  # Output: 80
print("Inorder traversal:", bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]

bst.delete(40)
print("Search for 40:", bst.search(40))  # Output: None
print('Inorder traversal after deleting 40:', bst.inorder_traversal())  # Output: [20, 30, 50, 60, 70, 80]
```
## Requirements / Requisitos

```
Python 3.x
```

## How to Contribute / Como Contribuir
- Fork the repository. / Faça um fork do repositório.
- Create a branch for your feature: git checkout -b minha-feature. / Crie uma branch para sua feature.
- Commit your changes: git commit -m 'Adicionei uma nova feature'. / Commit suas mudanças.
- Push to the branch: git push origin minha-feature. / Push para a branch.
- Open a pull request and describe your changes. / Abra um pull request e descreva suas mudanças.

## License / Licença
This project is licensed under the MIT License. See the LICENSE file for details.

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
