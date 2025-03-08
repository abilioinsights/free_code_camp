# Budget App / Aplicativo de Orçamento

This Python project implements a budget application with categories for tracking expenses. It includes a `Category` class to manage deposits, withdrawals, and transfers, as well as a `create_spend_chart` function to generate a bar chart of expenses by category.

Este projeto Python implementa um aplicativo de orçamento com categorias para rastrear despesas. Ele inclui uma classe `Category` para gerenciar depósitos, retiradas e transferências, além de uma função `create_spend_chart` para gerar um gráfico de barras das despesas por categoria.

## Features / Funcionalidades
- **Category Management:** Create categories, deposit funds, withdraw funds, and transfer funds between categories. / Crie categorias, deposite fundos, retire fundos e transfira fundos entre categorias.
- **Expense Tracking:** Track expenses and calculate balances. / Acompanhe despesas e calcule saldos.
- **Spend Chart:** Generate a bar chart showing the percentage spent in each category. / Gere um gráfico de barras mostrando a porcentagem gasta em cada categoria.

## How to Use / Como Usar
## 1. **Create a Category:**
   ```py
   food = Category("Food")
   ```

## 2. Deposit Funds:
```py
food.deposit(1000, "deposit")
```

## 3. Withdraw Funds:
```py
food.withdraw(10.15, "groceries")
```
## 4. Transfer Funds:

```py
clothing = Category("Clothing")
food.transfer(50, clothing)
```

## 5. Generate Spend Chart:

```py
categories = [food, clothing]
print(create_spend_chart(categories))
```

## Example / Exemplo

```py
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
print(clothing)

categories = [food, clothing]
print(create_spend_chart(categories))
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
