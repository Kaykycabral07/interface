from gui import mostrar_inicial, janela


if __name__ == "__main__":
    janela.after(0, mostrar_inicial)
    janela.mainloop()