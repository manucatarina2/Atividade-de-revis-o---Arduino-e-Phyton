Exercício de Fixação e Aprofundamento – Python e Arduino

Este repositório contém duas atividades práticas que unem hardware (Arduino) e software (Python), com o objetivo de fixar conceitos fundamentais de programação e automação.

Atividade 1 – Arduino

Tema: Automatização de iluminação com sensor LDR

Escopo

Desenvolver um sistema simples no Arduino que acenda um LED quando o ambiente estiver escuro e o apague quando houver luminosidade suficiente.

Materiais necessários

1 Placa Arduino UNO (ou similar)

1 LED

1 resistor de 220Ω

1 resistor de 10kΩ

1 LDR (sensor de luminosidade)

Jumpers e protoboard

Passos da atividade

Montar o circuito no protoboard:

LDR em série com resistor de 10kΩ → divisor de tensão.

LED com resistor de 220Ω → pino digital.

Programar o Arduino para ler o valor analógico do LDR.

Definir um limiar (threshold) para decidir se o LED deve acender ou apagar.

Testar em ambiente claro e escuro.

Objetivos pedagógicos

Compreender entrada analógica (LDR) e saída digital (LED).

Reforçar o uso de condicionais no Arduino.

Relacionar conceitos de hardware + software na interação físico-digital.

Atividade 2 – Python

Tema: Sistema de Cadastro e Busca de Alunos

Escopo

Criar um programa em Python que cadastre alunos em uma lista e permita pesquisar um aluno pelo nome.

Funcionalidades mínimas

Menu inicial com opções:

1 → Cadastrar aluno

2 → Listar todos os alunos

3 → Pesquisar aluno por nome

4 → Sair

Cada aluno deve ter: Nome, Idade, Curso.

Cadastro salvo em uma lista de dicionários.

Busca por nome com mensagem caso não seja encontrado.

Objetivos pedagógicos

Reforçar uso de listas e dicionários.

Praticar manipulação de strings e loops.

Aplicar lógica de programação em um problema real.
