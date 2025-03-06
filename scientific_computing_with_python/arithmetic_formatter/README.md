# Arithmetic Arranger / Organizador Aritmético

This Python function formats arithmetic problems vertically and arranges them neatly. It supports addition and subtraction and can optionally display the results.

Esta função Python formata problemas aritméticos verticalmente e os organiza de forma clara. Ela suporta adição e subtração e pode opcionalmente exibir os resultados.

## Features / Funcionalidades
- Formats arithmetic problems vertically. / Formata problemas aritméticos verticalmente.
- Supports addition and subtraction. / Suporta adição e subtração.
- Optionally displays the results. / Exibe os resultados opcionalmente.
- Handles errors for invalid input. / Lida com erros de entrada inválida.

## How to Use / Como Usar
The function `arithmetic_arranger` takes two parameters:  
A função `arithmetic_arranger` recebe dois parâmetros:
1. `problems`: A list of arithmetic problems (e.g., `["32 + 698", "3801 - 2"]`).  
   Uma lista de problemas aritméticos (por exemplo, `["32 + 698", "3801 - 2"]`).
2. `show_answers` (optional): If `True`, the results are displayed.  
   Se `True`, os resultados são exibidos.

### Example / Exemplo
```python
from arithmetic_arranger import arithmetic_arranger

# Format problems and show answers
# Formata problemas e exibe os resultados
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
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
