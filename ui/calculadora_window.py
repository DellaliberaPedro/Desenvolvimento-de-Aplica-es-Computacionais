# -*- coding: utf-8 -*-
"""
Camada de APRESENTACAO (UI).

So monta os widgets e o layout. Nao faz nenhuma conta aqui dentro -
quem faz isso e o Controller + Model. A janela apenas expoe os
widgets (self.visor, self.botoes) para o Controller conectar os sinais.

Construida em codigo puro (QGridLayout) em vez de arquivo .ui do
Qt Designer, para nao depender do designer/uic.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QSizePolicy,
)


class CalculadoraWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora - Projeto Integrador")
        self.setFixedSize(300, 400)

        self._montar_visor()
        self._montar_botoes()
        self._montar_layout()

    def _montar_visor(self):
        self.visor = QLineEdit("0")
        self.visor.setReadOnly(True)
        self.visor.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.visor.setStyleSheet("font-size: 28px; padding: 8px;")
        self.visor.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def _montar_botoes(self):
        layout_botoes = [
            ("C", 0, 0, 1), ("Del", 0, 1, 1), ("%", 0, 2, 1), ("/", 0, 3, 1),
            ("7", 1, 0, 1), ("8", 1, 1, 1), ("9", 1, 2, 1), ("*", 1, 3, 1),
            ("4", 2, 0, 1), ("5", 2, 1, 1), ("6", 2, 2, 1), ("-", 2, 3, 1),
            ("1", 3, 0, 1), ("2", 3, 1, 1), ("3", 3, 2, 1), ("+", 3, 3, 1),
            ("+/-", 4, 0, 1), ("0", 4, 1, 1), (".", 4, 2, 1), ("=", 4, 3, 1),
        ]

        self.botoes = {}
        self._layout_botoes = layout_botoes

        for texto, _linha, _coluna, _colspan in layout_botoes:
            botao = QPushButton(texto)
            botao.setFixedHeight(55)
            botao.setStyleSheet("font-size: 18px;")
            self.botoes[texto] = botao

    def _montar_layout(self):
        grid = QGridLayout()
        grid.addWidget(self.visor, 0, 0, 1, 4)

        for texto, linha, coluna, colspan in self._layout_botoes:
            grid.addWidget(self.botoes[texto], linha + 1, coluna, 1, colspan)

        self.setLayout(grid)

    def atualizar_visor(self, texto: str):
        self.visor.setText(texto)
