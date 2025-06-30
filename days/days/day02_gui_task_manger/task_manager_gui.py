import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime


class TaskManagerGUI:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

        # Configuração da janela principal
        self.root = tk.Tk()
        self.root.title("🎯 Task Manager")
        self.root.geometry("500x700")
        self.root.configure(bg="#2c3e50")

        # Configuração de fonte
        self.default_font = ("Arial", 10)
        self.title_font = ("Arial", 14, "bold")

        self.setup_ui()
        self.render_tasks()

    def load_tasks(self):
        """Carrega tarefas do arquivo JSON"""
        if os.path.exists("tasks_gui.json"):
            try:
                with open("tasks_gui.json", "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
            except:
                self.tasks = ["Study Python",
                              "Train jiu-jitsu", "Buy groceries"]
        else:
            self.tasks = ["Study Python", "Train jiu-jitsu", "Buy groceries"]

    def save_tasks(self):
        """Salva tarefas no arquivo JSON"""
        try:
            with open("tasks_gui.json", "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {e}")

    def setup_ui(self):
        """Configura a interface do usuário"""

        # Título principal
        title_frame = tk.Frame(self.root, bg="#2c3e50")
        title_frame.pack(pady=20)

        tk.Label(title_frame, text="🎯 Suas Tarefas",
                 font=self.title_font, bg="#2c3e50",
                 fg="#ecf0f1").pack()

        # Frame para entrada de nova tarefa
        input_frame = tk.Frame(self.root, bg="#2c3e50")
        input_frame.pack(pady=10, padx=20, fill="x")

        self.task_entry = tk.Entry(input_frame, font=self.default_font,
                                   width=30, relief="flat", bd=5)
        self.task_entry.pack(side="left", padx=(0, 10), fill="x", expand=True)
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        add_btn = tk.Button(input_frame, text="➕ Adicionar",
                            command=self.add_task,
                            font=self.default_font,
                            bg="#27ae60", fg="white",
                            relief="flat", bd=0, padx=15)
        add_btn.pack(side="right")

        # Frame para botões de ação
        action_frame = tk.Frame(self.root, bg="#2c3e50")
        action_frame.pack(pady=10)

        btn_style = {"font": self.default_font, "relief": "flat",
                     "bd": 0, "padx": 15, "pady": 5}

        tk.Button(action_frame, text="🗑️ Limpar Concluídas",
                  command=self.clear_completed,
                  bg="#e74c3c", fg="white", **btn_style).pack(side="left", padx=5)

        tk.Button(action_frame, text="📊 Estatísticas",
                  command=self.show_stats,
                  bg="#3498db", fg="white", **btn_style).pack(side="left", padx=5)

        tk.Button(action_frame, text="💾 Salvar",
                  command=self.save_tasks,
                  bg="#9b59b6", fg="white", **btn_style).pack(side="left", padx=5)

        # Frame principal para tarefas com scrollbar
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Canvas e scrollbar para scroll
        canvas = tk.Canvas(main_frame, bg="#34495e", highlightthickness=0)
        scrollbar = ttk.Scrollbar(
            main_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg="#34495e")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Status bar
        self.status_frame = tk.Frame(self.root, bg="#34495e", height=30)
        self.status_frame.pack(fill="x", side="bottom")

        self.status_label = tk.Label(self.status_frame, text="Pronto",
                                     font=("Arial", 9), bg="#34495e",
                                     fg="#bdc3c7", anchor="w")
        self.status_label.pack(fill="x", padx=10, pady=5)

        # Configurar scroll com mouse wheel
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", on_mousewheel)

    def render_tasks(self):
        """Renderiza as tarefas na interface"""
        # Limpa tarefas anteriores
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if not self.tasks:
            empty_label = tk.Label(self.scrollable_frame,
                                   text="🎉 Nenhuma tarefa! Adicione uma nova acima.",
                                   font=self.default_font, bg="#34495e",
                                   fg="#95a5a6", pady=20)
            empty_label.pack(fill="x")
            self.update_status("Nenhuma tarefa")
            return

        for i, task_data in enumerate(self.tasks):
            # Suporte tanto para strings simples quanto dicionários
            if isinstance(task_data, str):
                task_text = task_data
                completed = False
            else:
                task_text = task_data.get("text", "")
                completed = task_data.get("completed", False)

            # Frame para cada tarefa
            task_frame = tk.Frame(self.scrollable_frame, bg="#ecf0f1",
                                  relief="raised", bd=1)
            task_frame.pack(fill="x", pady=3, padx=5)

            # Checkbox
            var = tk.BooleanVar(value=completed)
            checkbox = tk.Checkbutton(task_frame, variable=var, bg="#ecf0f1",
                                      command=lambda idx=i, v=var: self.toggle_task(idx, v.get()))
            checkbox.pack(side="left", padx=10)

            # Label da tarefa
            text_color = "#7f8c8d" if completed else "#2c3e50"
            font_style = self.default_font if not completed else (
                *self.default_font[:2], "overstrike")

            task_label = tk.Label(task_frame, text=f"{i+1}. {task_text}",
                                  font=font_style, bg="#ecf0f1",
                                  fg=text_color, anchor="w")
            task_label.pack(side="left", fill="x", expand=True, padx=5)

            # Botão de remover
            remove_btn = tk.Button(task_frame, text="❌",
                                   command=lambda idx=i: self.remove_task(idx),
                                   bg="#e74c3c", fg="white",
                                   font=("Arial", 8), relief="flat",
                                   bd=0, width=3)
            remove_btn.pack(side="right", padx=5)

            # Botão de editar
            edit_btn = tk.Button(task_frame, text="✏️",
                                 command=lambda idx=i: self.edit_task(idx),
                                 bg="#f39c12", fg="white",
                                 font=("Arial", 8), relief="flat",
                                 bd=0, width=3)
            edit_btn.pack(side="right", padx=2)

        self.update_status_count()

    def add_task(self):
        """Adiciona uma nova tarefa"""
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Aviso", "Digite uma tarefa!")
            return

        # Cria tarefa como dicionário
        new_task = {
            "text": task_text,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.tasks.append(new_task)
        self.task_entry.delete(0, tk.END)
        self.render_tasks()
        self.save_tasks()
        self.update_status(f"Tarefa '{task_text}' adicionada!")

    def remove_task(self, index):
        """Remove uma tarefa"""
        if 0 <= index < len(self.tasks):
            task_data = self.tasks[index]
            task_text = task_data["text"] if isinstance(
                task_data, dict) else task_data

            if messagebox.askyesno("Confirmar", f"Remover '{task_text}'?"):
                self.tasks.pop(index)
                self.render_tasks()
                self.save_tasks()
                self.update_status(f"Tarefa removida!")

    def edit_task(self, index):
        """Edita uma tarefa"""
        if 0 <= index < len(self.tasks):
            task_data = self.tasks[index]
            current_text = task_data["text"] if isinstance(
                task_data, dict) else task_data

            new_text = simpledialog.askstring("Editar Tarefa",
                                              "Digite o novo texto:",
                                              initialvalue=current_text)
            if new_text and new_text.strip():
                if isinstance(self.tasks[index], dict):
                    self.tasks[index]["text"] = new_text.strip()
                else:
                    self.tasks[index] = new_text.strip()

                self.render_tasks()
                self.save_tasks()
                self.update_status("Tarefa editada!")

    def toggle_task(self, index, completed):
        """Alterna o status de uma tarefa"""
        if 0 <= index < len(self.tasks):
            # Converte string para dict se necessário
            if isinstance(self.tasks[index], str):
                self.tasks[index] = {
                    "text": self.tasks[index],
                    "completed": completed,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            else:
                self.tasks[index]["completed"] = completed

            if completed:
                self.tasks[index]["completed_at"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S")

            self.render_tasks()
            self.save_tasks()
            status = "concluída" if completed else "reaberta"
            self.update_status(f"Tarefa {status}!")

    def clear_completed(self):
        """Remove todas as tarefas concluídas"""
        completed_count = sum(1 for task in self.tasks
                              if isinstance(task, dict) and task.get("completed", False))

        if completed_count == 0:
            messagebox.showinfo(
                "Informação", "Nenhuma tarefa concluída para remover!")
            return

        if messagebox.askyesno("Confirmar",
                               f"Remover {completed_count} tarefa(s) concluída(s)?"):
            self.tasks = [task for task in self.tasks
                          if not (isinstance(task, dict) and task.get("completed", False))]
            self.render_tasks()
            self.save_tasks()
            self.update_status(
                f"{completed_count} tarefa(s) concluída(s) removida(s)!")

    def show_stats(self):
        """Mostra estatísticas das tarefas"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks
                        if isinstance(task, dict) and task.get("completed", False))
        pending = total - completed

        if total > 0:
            completion_rate = (completed / total) * 100
        else:
            completion_rate = 0

        stats_text = f"""📊 Estatísticas das Tarefas

📝 Total: {total}
✅ Concluídas: {completed}
⏳ Pendentes: {pending}
📈 Taxa de Conclusão: {completion_rate:.1f}%"""

        messagebox.showinfo("Estatísticas", stats_text)

    def update_status(self, message):
        """Atualiza a barra de status"""
        self.status_label.config(text=message)
        self.root.after(3000, lambda: self.status_label.config(text="Pronto"))

    def update_status_count(self):
        """Atualiza contagem na barra de status"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks
                        if isinstance(task, dict) and task.get("completed", False))
        self.status_label.config(
            text=f"Total: {total} | Concluídas: {completed} | Pendentes: {total - completed}")

    def run(self):
        """Inicia a aplicação"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        """Chamado quando a janela é fechada"""
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    app = TaskManagerGUI()
    app.run()
