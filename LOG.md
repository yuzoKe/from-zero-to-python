# 📓 From Zero to Python — Learning Journal
This is my personal record of daily learning. Each day includes a short summary of what I worked on, what I learned, and what I plan to improve. Mistakes included. Growth guaranteed.

---

# ✅ Day 1 — Task Manager (Lists, Input/Output)
📅 Date: 27/06/2025
📁 Project: days/day01_task_manager/task_manager.py

## 📌 Focus:
* Learn basic list operations
* Use input() to interact with the user
* Practice loops with for and enumerate()
* Implement simple conditionals with if and else

## 🔍 What I learned:
* How to create and update lists in Python using .append() and .pop()
* How to loop over elements with indexes using enumerate()
* How to safely remove an item from a list by validating the index
* That input() always returns a string — so converting to int is essential when working with numbers
* The use of \n to jump a line

## ⚠️ Challenges:
Understanding zero-based indexing and how to adjust it when displaying options to users

## 🧠 Reflections:
This was my first real Python script and it felt great to see a working CLI program. It's simple, but functional. I already started thinking about making it "tangible" and saving data to a file.

---

# ✅ Day 2 — GUI Task Manager (First time with Tkinter!)
📅 Date: 29/06/2025
📁 Project: days/day02_gui_task_manager/

## 📌 What I tried to do:
* Make a visual version of yesterday's task manager
* Learn about windows and buttons (Tkinter)
* Figure out how to save tasks so they don't disappear

## 🔍 What I actually learned:
* Classes are confusing but useful: Still don't fully get self but I see it organizes code better
* Tkinter basics: Made a window with buttons! Took forever to figure out pack()
* Saving data: Used JSON - basically a text file that looks like Python dictionaries
* Buttons do things: Connecting command=function_name was magical when it worked

## 😅 Honest struggles:
* Spent 2 hours trying to understand why my button wasn't working
* Classes vs functions - still mixing them up
* Error messages everywhere until I added try/except (copied from examples)
* The code is mostly working but I don't understand every single line

## 🎉 Cool things that worked:
* You can actually check off tasks!
* Tasks keep saved when you close the program (mind blown)
* Delete button works (with confirmation so I don't delete by accident)
* Changed colors to make it look less ugly

## 🤔 Things I copy-pasted and need to understand better:
* The scrollbar part (it works but... how?)
* Lambda functions - used them but still googling what they do
* Some of the layout code
* Error handling - I know it's important but added it blindly

## 🧠 Honest reflection:
This feels like a huge jump from yesterday! The GUI actually looks like a real program. Got help from AI/tutorials for the complex parts, but I typed every line and tested everything. Still have no idea how some parts work, but how I said, I believe in learning by doing.
The best part: when I showed it to my family, they said "wow, you made that?!", felt good.

## 🎯 Tomorrow I want to:
* Actually understand what self means
* Add simple features without copying code
* Try colors or fonts
* Read more about classes

---

# 📘 Dev Log — Dia 03 (01/07/2025)

## 💻 O que fiz hoje

Hoje precisei sair da trilha do Python para resolver uma demanda urgente e prática da minha loja.

Criei um **sistema completo de fidelidade em VBA** para o Excel, automatizando o controle de alicates trazidos por clientes. Antes, esse controle era feito manualmente com cartões físicos. Agora:

- A cada 12 alicates, o sistema **aplica automaticamente R$10 de desconto**.
- O que ultrapassa 12 **vira saldo acumulado** para o próximo pedido.
- O sistema identifica o cliente pelo telefone e **acumula histórico automaticamente**.
- Não é necessário cadastrar previamente — o sistema **cria ou atualiza os dados do cliente na hora**.

## ⚙️ Por que isso importa

Embora não tenha sido um avanço direto em Python, **foi um avanço como desenvolvedor**.

Eu precisei:
- Criar uma estrutura de dados (`Type`) em VBA.
- Trabalhar com lógica condicional e cálculo de saldos acumulados.
- Automatizar buscas em planilhas e criação de registros históricos.
- Pensar em usabilidade para operadores e integração com a rotina da loja.

Tudo isso me aproximou mais de conceitos de **persistência de dados, modularização e automação de tarefas**, que também fazem parte do universo do Python — só que aqui aplicados em um sistema real.

## 🧠 Reflexão

Hoje eu entendi que **programar não é só aprender linguagens, mas resolver problemas**. E cada vez que resolvemos um problema com código — seja em Python, VBA ou qualquer outro ambiente — estamos nos tornando programadores mais completos.

**Amanhã, volto pro Python. Mas com uma nova bagagem.**
