# -*- coding: utf-8 -*-
"""
Camada de LOGICA / DOMINIO da calculadora.

Esta classe nao sabe nada sobre PySide6, botoes ou janelas.
Ela apenas recebe comandos (digitos, operacoes) e devolve o texto
que deve aparecer no visor.
"""


class DivisaoPorZeroError(Exception):
    """Erro especifico de dominio para divisao por zero."""
    pass


class CalculadoraModel:
    OPERACOES = {"+", "-", "*", "/"}

    def __init__(self):
        self.reset()

    def reset(self):
        """Zera todo o estado do calculo (equivalente ao botao 'C')."""
        self.display = "0"
        self.operando_anterior = None
        self.operacao_pendente = None
        self.iniciar_novo_numero = True

    def inserir_digito(self, digito: str):
        if self.iniciar_novo_numero:
            self.display = digito
            self.iniciar_novo_numero = False
        else:
            if self.display == "0":
                self.display = digito
            else:
                self.display += digito

    def inserir_ponto(self):
        if self.iniciar_novo_numero:
            self.display = "0."
            self.iniciar_novo_numero = False
        elif "." not in self.display:
            self.display += "."

    def alternar_sinal(self):
        if self.display.startswith("-"):
            self.display = self.display[1:]
        elif self.display != "0":
            self.display = "-" + self.display

    def apagar_ultimo(self):
        if self.iniciar_novo_numero:
            return
        self.display = self.display[:-1] or "0"
        if self.display in ("", "-"):
            self.display = "0"

    def definir_operacao(self, operacao: str):
        if operacao not in self.OPERACOES:
            raise ValueError(f"Operacao invalida: {operacao}")

        if self.operacao_pendente is not None and not self.iniciar_novo_numero:
            self.calcular()

        self.operando_anterior = float(self.display)
        self.operacao_pendente = operacao
        self.iniciar_novo_numero = True

    def calcular(self):
        """Executa a operacao pendente (botao '='). Retorna o resultado."""
        if self.operacao_pendente is None or self.operando_anterior is None:
            return float(self.display)

        operando_atual = float(self.display)
        resultado = self._aplicar_operacao(
            self.operando_anterior, operando_atual, self.operacao_pendente
        )

        self.display = self._formatar(resultado)
        self.operando_anterior = resultado
        self.operacao_pendente = None
        self.iniciar_novo_numero = True
        return resultado

    def _aplicar_operacao(self, a: float, b: float, operacao: str) -> float:
        if operacao == "+":
            return a + b
        if operacao == "-":
            return a - b
        if operacao == "*":
            return a * b
        if operacao == "/":
            if b == 0:
                raise DivisaoPorZeroError("Nao e possivel dividir por zero.")
            return a / b
        raise ValueError(f"Operacao invalida: {operacao}")

    @staticmethod
    def _formatar(numero: float) -> str:
        if numero == int(numero) and abs(numero) < 1e15:
            return str(int(numero))
        return str(numero)
