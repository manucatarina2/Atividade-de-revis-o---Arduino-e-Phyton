# Exercício de Fixação e Aprofundamento – Python e Arduino

Este repositório contém duas atividades práticas para consolidar o aprendizado em **Arduino** e **Python**, explorando conceitos de **hardware, software e lógica de programação**.

---

## Atividade 1 – Arduino  
### Tema: Automatização de iluminação com sensor LDR  

**Descrição:**  
O aluno deve desenvolver um sistema simples que acenda um **LED** quando o ambiente estiver escuro e o apague quando houver luminosidade suficiente.  

### Escopo
1. Montar o circuito no protoboard:  
   - Conectar o **LDR** em série com resistor de **10kΩ** para formar um divisor de tensão.  
   - Conectar o **LED** com resistor de **220Ω** em um pino digital do Arduino.  
2. Programar o Arduino para ler o valor analógico do LDR.  
3. Definir um limite (*threshold*) para decidir se o LED deve acender ou apagar.  
4. Testar em ambientes claro e escuro.  

### Materiais
- 1 Arduino UNO (ou similar)  
- 1 LED  
- 1 resistor de 220Ω  
- 1 resistor de 10kΩ  
- 1 LDR (sensor de luminosidade)  
- Jumpers e protoboard  

### Objetivos Pedagógicos
- Trabalhar **entrada analógica** (LDR) e **saída digital** (LED).  
- Reforçar a **lógica condicional** no Arduino.  
- Relacionar conceitos de **hardware + software** (interação físico-digital).  

---

## Atividade 2 – Python  
### Tema: Sistema de Cadastro e Busca de Alunos  

**Descrição:**  
O aluno deve criar um programa em Python que permita **cadastrar alunos** em uma lista e **pesquisar alunos pelo nome**.  

### Funcionalidades mínimas
1. Menu inicial com opções:  
   - `1` → Cadastrar aluno  
   - `2` → Listar todos os alunos  
   - `3` → Pesquisar aluno por nome  
   - `4` → Sair  
2. Cada aluno deve conter: **Nome, Idade, Curso**.  
3. Dados salvos em uma **lista de dicionários**.  
4. Na busca, exibir mensagem caso o aluno não seja encontrado.  

### Objetivos Pedagógicos
- Reforçar uso de **listas e dicionários** em Python.  
- Trabalhar **manipulação de strings** e **loops**.  
- Aplicar **lógica de programação** em um problema prático.  

---

## Organização do Repositório
- `/arduino/` → Código e esquemático da Atividade 1  
- `/python/` → Código da Atividade 2  

---

## Aprendizados Esperados
- Integração entre **hardware (Arduino)** e **software (código Python)**.  
- Desenvolvimento de soluções lógicas e práticas.  
- Consolidação de conceitos fundamentais de programação e eletrônica.  

