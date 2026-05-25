# Quiz de Lógica de Programação

Quiz feito em Python com interface gráfica usando tkinter. Projeto de faculdade.

## Rodando o projeto

```bash
python main.py
```

## Estrutura de pastas

```
projeto_faculdade/
├── main.py
└── quiz/
    ├── data/
    │   └── perguntas.py
    ├── ui/
    │   └── tela.py
    └── utils/
        └── score.py
```

**main.py** — só chama a função que abre a janela. Nada mais.

**quiz/data/perguntas.py** — lista com as perguntas, opções e resposta correta de cada uma. Se quiser adicionar ou mudar alguma pergunta, é aqui.

**quiz/ui/tela.py** — toda a interface gráfica fica aqui. A classe `TelaQuiz` cuida de montar a tela, mostrar as perguntas, colorir os botões certo/errado e exibir o resultado no final.

**quiz/utils/score.py** — uma função só: calcula o percentual de acertos. Usada na tela de resultado.

Os `__init__.py` dentro de cada pasta são necessários para o Python reconhecer as pastas como pacotes e deixar os arquivos se importarem entre si.

## Fluxo do jogo

O usuário roda o `main.py`, a janela abre já centralizada na tela. A classe `TelaQuiz` monta todos os widgets de uma vez: título, progresso, pontuação, a pergunta e os quatro botões de resposta.

Quando o usuário clica numa alternativa, os botões são desabilitados na hora pra evitar clique duplo, o botão certo fica verde e o errado fica vermelho. A pontuação atualiza e aparece o botão "Próxima".

Isso se repete até acabar as cinco perguntas. Aí a tela é limpa e mostra o resultado final com a pontuação, o percentual e uma mensagem dependendo do desempenho. Tem um botão pra jogar de novo, que zera tudo e remonta a tela do zero.
