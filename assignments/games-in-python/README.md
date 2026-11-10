
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Implemente um jogo da Forca em Python para praticar strings, listas, estruturas de repetição, condicionais e entrada de dados. O jogador deve descobrir uma palavra oculta antes de atingir o limite de erros.

## 📝 Tarefas

### 🛠️ Implementar a Partida

#### Descrição
Complete o código inicial para escolher uma palavra e executar uma partida, atualizando o progresso a cada palpite.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida.
- Mostrar as letras ainda não descobertas como espaços reservados, por exemplo, `_ _ _ _`.
- Solicitar palpites de letras e revelar todas as ocorrências de cada letra correta.
- Contabilizar os palpites incorretos e limitar o número de erros.
- Encerrar a partida quando a palavra for descoberta ou o limite de erros for atingido.
- Informar se o jogador venceu ou perdeu e, em caso de derrota, revelar a palavra.

### 🛠️ Validar os Palpites

#### Descrição
Trate entradas inválidas e repetidas para que elas não alterem indevidamente o estado da partida.

#### Requisitos
O programa concluído deve:

- Aceitar somente um caractere alfabético por palpite e comparar letras sem diferenciar maiúsculas de minúsculas.
- Avisar quando a entrada não for uma letra válida, sem consumir uma tentativa.
- Avisar quando uma letra já tiver sido usada, sem contabilizá-la novamente.
- Exibir as letras já tentadas e os erros restantes após cada palpite válido.