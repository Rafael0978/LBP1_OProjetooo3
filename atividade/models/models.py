from flask import render_template

class Filme:
    def __init__(self, nome, classificaco, anoLanc):
        self.nome = nome
        self.email = classificaco
        self.senha = anoLanc
