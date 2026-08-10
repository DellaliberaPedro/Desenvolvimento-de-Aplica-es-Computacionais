# Calculadora Desktop Modularizada

Projeto Integrador - Unidade 1. Calculadora desktop em PySide6 com arquitetura em camadas (UI / Controller / Model).

Integrantes:
Pedro Henrique Devens Dellalibera 432700
João Gabriel Trevisol 433578
Alan Hoffman Dos Santos 432690

## Estrutura

- models/calculadora_model.py - regras de negocio (soma, subtracao, multiplicacao, divisao, estado)
- controllers/calculadora_controller.py - conecta cliques da UI aos metodos do model
- ui/calculadora_window.py - janela, visor e teclado (QGridLayout)
- main.py - ponto de entrada

## Como rodar

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py

Sempre execute "python main.py" estando dentro desta pasta.
Boa Noite