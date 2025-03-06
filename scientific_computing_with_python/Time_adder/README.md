# Time Adder / Adicionador de Horas

This Python function adds a duration to a start time in 12-hour format. It also handles conversion between 12-hour and 24-hour formats, calculates additional days, and returns the resulting day of the week if provided.

Esta função Python adiciona uma duração a um horário inicial no formato de 12 horas. Ela também lida com a conversão entre os formatos de 12 e 24 horas, calcula os dias adicionais e retorna o dia da semana resultante, se fornecido.

## Features / Funcionalidades
- Adds a duration to a start time. / Adiciona uma duração a um horário inicial.
- Converts between 12-hour and 24-hour formats. / Converte entre os formatos de 12 e 24 horas.
- Calculates additional days and the resulting day of the week. / Calcula os dias adicionais e o dia da semana resultante.
- Formats the result clearly and legibly. / Formata o resultado de forma clara e legível.

## How to Use / Como Usar
The function `add_time` takes three parameters:  
A função `add_time` recebe três parâmetros:
1. `start`: The start time in "HH:MM AM/PM" format. / O horário inicial no formato "HH:MM AM/PM".
2. `duration`: The duration to add in "HH:MM" format. / A duração a ser adicionada no formato "HH:MM".
3. `day_of_week` (optional): The starting day of the week (e.g., "Monday"). / O dia da semana inicial (por exemplo, "Monday").

### Example / Exemplo
```python
from time_adder import add_time

# Add 2 hours and 30 minutes to 3:00 PM
# Adicionar 2 horas e 30 minutos a 3:00 PM
print(add_time('3:00 PM', '2:30'))  # Output: 5:30 PM / Saída: 5:30 PM

# Add 24 hours to 11:30 AM, starting on Monday
# Adicionar 24 horas a 11:30 AM, começando na segunda-feira
print(add_time('11:30 AM', '24:00', 'Monday'))  # Output: 11:30 AM, Tuesday (next day) / Saída: 11:30 AM, Tuesday (next day)
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
