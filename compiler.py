import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

def main():
    def process_data():
        info = info_entry.get()
        path_ = path_exe.get()
        filepath = filedialog.askopenfilename(
            title="выберите файл для компиляции",
            filetypes=[("твой python файл", "*.py")]
        )

        if filepath and path_:  # Проверяет, что введен текст и выбран файл
            try:
                # Здесь можно выполнить необходимые действия с полученными данными:
                # Например, сохранить в файл, отправить на сервер, обработать и т.д.
                # В этом примере просто отображаем данные в messagebox:
                os.chdir(path_)
                if info:
                    _ = os.system(f'pyinstaller --distpath "{path_}" {info} "{filepath}"')
                    if _ == 0:
                        messagebox.showinfo('Готово!', 'Файл преобразовован в .exe исполняющий файл.')
                    else:
                        messagebox.showerror("Ошибка", f"Произошла ошибка. Проверьте, что установлен модуль pyinstaller.")
                else:
                    __ = os.system(f'pyinstaller --distpath "{path_}" "{filepath}"')
                    if __ == 0:
                        messagebox.showinfo('Готово!', 'Файл преобразовован в .exe исполняющий файл.')
                    else:
                        messagebox.showerror("Ошибка", f"Произошла ошибка. Проверьте, что установлен модуль pyinstaller.")

            except Exception as e:
                messagebox.showerror("Ошибка", f"Произошла ошибка: {e}. Проверьте, что установлен модуль pyinstaller.")

        else:
            messagebox.showwarning("Внимание", "Пожалуйста, выберите файл, или напишите путь сохранение .exe файла.")
    global path_exe, info_entry
    # Создание основного окна Tkinter
    root = tk.Tk()
    root.title("Компиляция из .py в .exe")

    # 1. Поле ввода информации
    info_label = tk.Label(root, text="Введите флаги PyInstaller (если есть):")
    info_label.pack(pady=5)

    info_entry = tk.Entry(root, width=40)  # Увеличивает ширину поля ввода
    info_entry.pack(pady=5)

    path_label = tk.Label(root, text='Выберите путь сохранения .exe:')
    path_label.pack(pady=10)
    path_exe = tk.Entry(root, width=40)
    path_exe.pack(pady=10)

    # 2. Кнопка для запуска процесса
    process_button = tk.Button(root, text="Выбрать файл", command=process_data)
    process_button.pack(pady=15)


    # Запуск главного цикла обработки событий Tkinter
    root.mainloop()

main()