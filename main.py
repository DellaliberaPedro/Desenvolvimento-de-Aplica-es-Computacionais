# -*- coding: utf-8 -*-
"""
Ponto de entrada da aplicacao.

Rode sempre a partir desta pasta:
    python main.py
"""

import sys
from PySide6.QtWidgets import QApplication

from controllers.calculadora_controller import CalculadoraController


def main():
    app = QApplication(sys.argv)

    janela = CalculadoraController()
    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
