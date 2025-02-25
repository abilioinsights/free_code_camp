<h1>Card Validator Generator</h1>
<p>A Python-based tool to generate and validate credit card numbers using the Luhn algorithm. This project helps developers create valid credit card numbers for testing environments and check the validity of provided card numbers across various card brands.</p>

<h2>Features</h2>
<ul>
<li>Card Number Generation: Generate valid credit card numbers that pass the Luhn check.</li>
<li>Card Number Validation: Validate whether a given credit card number is valid or not.</li>
<li>Supported Card Brands: Visa, MasterCard, American Express, Diners Club, Discover, and JCB.</li></ul>

<h2>Installation</h2>
<p>Clone the repository and navigate to the project directory:</p>

```bash
git clone https://github.com/abilioinsights/free_code_camp.git
cd free_code_camp/scientific_computing_with_python/card_validator_generator
```
<p>No additional dependencies are required to run the script since it uses only standard Python libraries.</p>
<h2>Card Number Validation</h2>
<p>To validate a card number, choose the option to input a number manually:</p>

```py
python card_tool.py
```
<p><strong>Example interaction:</strong></p>

```yaml
Choose an option:
1. Validate a card number
2. Generate a valid card number
3. Exit

Enter your choice (1-3): 1
Enter the card number: 4111111111111111

Card Type: Visa
Status: VALID!
```
<h2>Card Number Generation</h2>
<p>You can also generate valid card numbers for testing purposes:</p>

```markdown
Choose an option:
1. Validate a card number
2. Generate a valid card number
3. Exit

Enter your choice (1-3): 2
```
<p><strong>Then choose the card type:</strong

  ```markdown
Choose a card brand to generate:
1. Visa
2. MasterCard
3. American Express
4. Diners Club
5. Discover
6. JCB
7. Back

Enter your choice (1-7): 1
```
<p><strong>A valid Visa card number will be generated, for example:</strong></p>

```java
Generated Card (Visa): 4532488243809092
```
<h2>Luhn Algorithm</h2>
<p>This project implements the <a href="https://en.wikipedia.org/wiki/Luhn_algorithm" target="_blank"> Luhn algorithm</a>, also known as the "modulus 10" algorithm, to validate card numbers by ensuring the correct check digit is appended.</p>

<h3>Supported Card Brands</h3>
<pThe following card brands are supported for generation and validation:</p>
<ul>
<li>Visa (16 digits)</li>
<li>MasterCard (16 digits)</li>
<li>American Express (15 digits)</li>
<li>Diners Club (14 digits)</li>
<li>Discover (16 digits)</li>
<li>JCB (16 digits)</li>
  </ul>
<h2>License</h2>
<p>This project is open-source and available under the MIT License.</p>
