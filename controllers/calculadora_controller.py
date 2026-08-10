# -*- coding: utf-8 -*-
"""
Camada de CONTROLE.

Conecta os eventos de clique (Signals) da UI aos metodos (Slots) que
chamam a logica de negocio no Model. A UI so exibe; o Model so calcula;
o Controller e quem faz a ponte entre os dois.
"""

from PySide6.QtWidgets import QWidget

from models.calculadora_model import CalculadoraModel, DivisaoPorZeroError
from ui.calculadora_window import CalculadoraWindow

DIGITOS = set("0123456789")
OPERACOES = {"+", "-", "*", "/"}


class CalculadoraController(QWidget):
    def __init__(self):
        super().__init__()
        self.model = CalculadoraModel()
        self.window = CalculadoraWindow()

        self._conectar_sinais()

    def _conectar_sinais(self):
        for texto, botao in self.window.botoes.items():
            botao.clicked.connect(lambda checked=False, t=texto: self._on_click(t))

    def _on_click(self, texto: str):
        try:
            if texto in DIGITOS:
                self.model.inserir_digito(texto)
            elif texto == ".":
                self.model.inserir_ponto()
            elif texto in OPERACOES:
                self.model.definir_operacao(texto)
            elif texto == "=":
                self.model.calcular()
            elif texto == "C":
                self.model.reset()
            elif texto == "Del":
                self.model.apagar_ultimo()
            elif texto == "+/-":
                self.model.alternar_sinal()
            elif texto == "%":
                self.model.display = self.model._formatar(float(self.model.display) / 100)

            self.window.atualizar_visor(self.model.display)

        except DivisaoPorZeroError:
            self.window.atualizar_visor("Erro: div/0")
            self.model.reset()
        except (ValueError, OverflowError):
            self.window.atualizar_visor("Erro")
            self.model.reset()

    def show(self):
        self.window.show()
