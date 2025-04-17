from gui import mostrar_frame_inicial, janela


if __name__ == "__main__":
    janela.after(0, mostrar_frame_inicial)
    janela.mainloop()