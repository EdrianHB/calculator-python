# 🧮 Calculadora em Python

Um projeto simples de **calculadora em Python** feito para praticar modularização e organização de código.
O programa permite que o usuário escolha uma operação matemática e informe os valores para realizar o cálculo.

---

## Estrutura do Projeto

```
 PROJETO
 ├── e10.py   # Arquivo principal (interface da calculadora)
 └── ep10.py  # Módulo com as funções das operações
```

---

## Como Funciona

* O arquivo **`e10.py`** é o programa principal.
* Ele utiliza o comando:

```python
import ep10
```

para acessar as funções matemáticas definidas no módulo **`ep10.py`**.

Ou seja:

* `e10.py` → controla interação com o usuário
* `ep10.py` → guarda a lógica das operações

Essa separação facilita:

* organização do código
* reutilização das funções
* manutenção do projeto

---

## Como Executar

1. Certifique-se de ter o **Python instalado** (versão 3 ou superior).
2. Coloque os dois arquivos na mesma pasta.
3. Execute no terminal:

```bash
python e10.py
```

---

## Operações Disponíveis

As operações matemáticas ficam dentro do módulo `ep10.py` e podem incluir, por exemplo:

* Soma
* Subtração
* Multiplicação
* Divisão

*(As operações exatas dependem das funções implementadas no módulo.)*

---

## Objetivo do Projeto

Este projeto foi desenvolvido para praticar:

* Importação de módulos em Python
* Organização de código em arquivos separados
* Lógica de programação
* Interação com usuário via terminal

---

## Possíveis Melhorias Futuras

* Interface gráfica
* Histórico de cálculos
* Tratamento de erros mais robusto
* Suporte a mais operações matemáticas

---

## Autor

Projeto desenvolvido por **Edrian Hípamo Boldrini** para fins de aprendizado.

---

Se quiser, você pode dar uma estrela no repositório para apoiar o projeto!
