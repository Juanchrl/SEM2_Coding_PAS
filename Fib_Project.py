import tkinter as tk

def fibonacci(n):
    fib_awal = [0, 1]
    while len(fib_awal) < n:
        fib_awal.append(fib_awal[-1] + fib_awal[-2])
    return fib_awal[:n]

def fib_generator():
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError("harus positif")
        fib_awal = fibonacci(n)
        hasil_text.set(', '.join(map(str, fib_awal)))
        error_text.set('')
    except ValueError as e:
        error_text.set(str(e))


root = tk.Tk()
root.title("Deret Fibonacci")

hasil_text = tk.StringVar()
error_text = tk.StringVar()

label = tk.Label(root, text="masukkan angka:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="generate", command=fib_generator)
button.pack(pady=10)

result_label = tk.Label(root, textvariable=hasil_text, wraplength=300)
result_label.pack(pady=10)

error_label = tk.Label(root, textvariable=error_text, fg='red')
error_label.pack(pady=5)

#buat run
root.mainloop()
