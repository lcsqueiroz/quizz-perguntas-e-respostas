import tkinter as tk
from quiz.data.perguntas import perguntas
from quiz.utils.score import calcular_percentual

FUNDO = "#1e1e2e"
BOTAO = "#313244"
TEXTO = "#cdd6f4"
CINZA = "#a6adc8"
VERDE = "#a6e3a1"
VERMELHO = "#f38ba8"
AZUL = "#89b4fa"

LETRAS = ["A", "B", "C", "D"]


class TelaQuiz:
    def __init__(self, janela):
        self.janela = janela
        largura = 620
        altura = 500
        x = (self.janela.winfo_screenwidth() - largura) // 2
        y = (self.janela.winfo_screenheight() - altura) // 2

        self.janela.title("Quiz de Lógica de Programação")
        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")
        self.janela.resizable(False, False)
        self.janela.configure(bg=FUNDO)

        self.indice = 0
        self.pontuacao = 0

        self._montar_tela()

    def _label(self, texto, tamanho=12, cor=None, negrito=False):
        estilo = "bold" if negrito else "normal"
        return tk.Label(
            self.janela,
            text=texto,
            font=("Arial", tamanho, estilo),
            bg=FUNDO,
            fg=cor or TEXTO,
            wraplength=540,
            justify="center"
        )

    def _botao(self, texto, cor_fundo, acao):
        return tk.Button(
            self.janela,
            text=texto,
            font=("Arial", 11),
            bg=cor_fundo,
            fg=FUNDO,
            relief="flat",
            cursor="hand2",
            command=acao
        )

    def _montar_tela(self):
        self._label("Quiz de Lógica de Programação", tamanho=17, negrito=True).pack(pady=(20, 4))

        self.txt_progresso = self._label("", tamanho=11, cor=CINZA)
        self.txt_progresso.pack()

        self.txt_pontuacao = self._label("Pontuação: 0", tamanho=11, cor=VERDE, negrito=True)
        self.txt_pontuacao.pack(pady=(2, 12))

        self.txt_pergunta = self._label("", tamanho=13)
        self.txt_pergunta.pack(pady=(0, 16))

        frame_botoes = tk.Frame(self.janela, bg=FUNDO)
        frame_botoes.pack()

        self.botoes = []
        for i in range(4):
            btn = tk.Button(
                frame_botoes,
                text="",
                font=("Arial", 11),
                width=52,
                bg=BOTAO,
                fg=TEXTO,
                activebackground="#45475a",
                relief="flat",
                cursor="hand2",
                command=lambda idx=i: self._responder(idx)
            )
            btn.pack(pady=4)
            self.botoes.append(btn)

        self.txt_feedback = self._label("", tamanho=12, negrito=True)
        self.txt_feedback.pack(pady=10)

        self.btn_proxima = self._botao("Próxima →", AZUL, self._proxima_pergunta)

        self._carregar_pergunta()

    def _carregar_pergunta(self):
        dados = perguntas[self.indice]

        self.txt_progresso.config(text=f"Pergunta {self.indice + 1} de {len(perguntas)}")
        self.txt_pergunta.config(text=dados["pergunta"])
        self.txt_feedback.config(text="")
        self.btn_proxima.pack_forget()

        for i, btn in enumerate(self.botoes):
            btn.config(text=dados["opcoes"][i], state="normal", bg=BOTAO, fg=TEXTO)

    def _responder(self, indice):
        dados = perguntas[self.indice]
        acertou = LETRAS[indice] == dados["resposta"]
        idx_certa = LETRAS.index(dados["resposta"])

        for btn in self.botoes:
            btn.config(state="disabled")

        if acertou:
            self.pontuacao += 1
            self.txt_feedback.config(text="Correto!", fg=VERDE)
        else:
            self.txt_feedback.config(text=f"Errado! A resposta correta era: {dados['resposta']}", fg=VERMELHO)
            self.botoes[indice].config(bg=VERMELHO, fg=FUNDO)

        self.botoes[idx_certa].config(bg=VERDE, fg=FUNDO)
        self.txt_pontuacao.config(text=f"Pontuação: {self.pontuacao}")
        self.btn_proxima.pack(pady=4)

    def _proxima_pergunta(self):
        self.indice += 1
        if self.indice < len(perguntas):
            self._carregar_pergunta()
        else:
            self._mostrar_resultado()

    def _mostrar_resultado(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

        total = len(perguntas)
        percentual = calcular_percentual(self.pontuacao, total)

        if percentual == 100:
            mensagem, cor = "Excelente! Nota máxima!", VERDE
        elif percentual >= 60:
            mensagem, cor = "Bom trabalho! Você foi aprovado!", AZUL
        else:
            mensagem, cor = "Estude mais e tente novamente.", VERMELHO

        self._label("Resultado Final", tamanho=20, negrito=True).pack(pady=(50, 8))
        self._label(f"{self.pontuacao} de {total} acertos", tamanho=14, cor=CINZA).pack()
        self._label(f"{percentual:.0f}%", tamanho=48, cor=cor, negrito=True).pack(pady=8)
        self._label(mensagem, tamanho=14, cor=cor).pack()

        self._botao("Jogar Novamente", AZUL, self._reiniciar).pack(pady=35)

    def _reiniciar(self):
        self.indice = 0
        self.pontuacao = 0
        for widget in self.janela.winfo_children():
            widget.destroy()
        self._montar_tela()


def iniciar_tela():
    janela = tk.Tk()
    TelaQuiz(janela)
    janela.mainloop()
