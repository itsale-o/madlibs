import customtkinter

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title('Madlibs - Halloween')


def madlibs():
    madlib = (f"Tonight is the night when all of the {adj1_input.get()} monsters come out to "
              f"{verb1_input.get()}. {adj2_input.get().capitalize()} witches with big {noun1_input.get()} and {color_input.get()} "
              f"shoes make potions and very spooky brews. Vampires with {noun2_input.get()} and long red capes "
              f"visit with friends and search for neck napes. Ogres and ghosts sometimes {verb2_input.get()} and play "
              f"on this {adj3_input.get()} October day. All the trick-or-treaters {verb3_input.get()} and "
              f"hunt for {noun3_input.get()} and scare, dressed up as princesses and cowboys here and there")

    entradas = [
        adj1_input.get(), verb1_input.get(), adj2_input.get(),
        noun1_input.get(), color_input.get(), noun2_input.get(),
        verb2_input.get(), adj3_input.get(), verb3_input.get(), noun3_input.get()
    ]

    if "" in entradas:
        label_entradas = customtkinter.CTkLabel(app, text="Preencha todos os campos",
                                                font=label)
        label_entradas.grid(row=10, column=1, pady=(0, 10))
    else:
        toplevel = customtkinter.CTkToplevel(app)
        label_toplevel = customtkinter.CTkLabel(toplevel, text="Halloween Night", font=titulo)
        label_toplevel.grid(pady=10)
        toplevel.title('Madlib!')
        textbox = customtkinter.CTkTextbox(toplevel, wrap="word", width=550, height=320, font=label)
        textbox.insert("0.0", madlib)
        textbox.configure(state="disabled")
        textbox.grid(padx=10, pady=10)


# Customizando as fontes
titulo = customtkinter.CTkFont(size=24, weight="bold")
label = customtkinter.CTkFont(size=18)
botao = customtkinter.CTkFont(size=20, weight="bold")

# Customizando a janela
label_titulo = customtkinter.CTkLabel(app, text="Monstrous Mad Libs", font=titulo, padx=10, pady=10)
label_titulo.grid(column=1)

adj1 = customtkinter.CTkLabel(app, text="Adjective", font=label)
adj1.grid(row=1, column=0)
adj1_input = customtkinter.CTkEntry(app)
adj1_input.grid(row=2, column=0, padx=10, pady=(0, 10))

adj2 = customtkinter.CTkLabel(app, text="Adjective", font=label)
adj2.grid(row=1, column=2)
adj2_input = customtkinter.CTkEntry(app)
adj2_input.grid(row=2, column=2, padx=10, pady=(0, 10))

adj3 = customtkinter.CTkLabel(app, text="Adjective", font=label)
adj3.grid(row=5, column=1)
adj3_input = customtkinter.CTkEntry(app)
adj3_input.grid(row=6, column=1, pady=(0, 10))

verb1 = customtkinter.CTkLabel(app, text="Verb", font=label)
verb1.grid(row=1, column=1)
verb1_input = customtkinter.CTkEntry(app)
verb1_input.grid(row=2, column=1, pady=(0, 10))

verb2 = customtkinter.CTkLabel(app, text="Verb", font=label)
verb2.grid(row=5, column=0)
verb2_input = customtkinter.CTkEntry(app)
verb2_input.grid(row=6, column=0, pady=(0, 10))

verb3 = customtkinter.CTkLabel(app, text="Verb", font=label)
verb3.grid(row=5, column=2)
verb3_input = customtkinter.CTkEntry(app)
verb3_input.grid(row=6, column=2, pady=(0, 10))

noun1 = customtkinter.CTkLabel(app, text="Noun", font=label)
noun1.grid(row=3, column=0)
noun1_input = customtkinter.CTkEntry(app)
noun1_input.grid(row=4, column=0, pady=(0, 10))

noun2 = customtkinter.CTkLabel(app, text="Noun (plural)", font=label)
noun2.grid(row=3, column=2)
noun2_input = customtkinter.CTkEntry(app)
noun2_input.grid(row=4, column=2, pady=(0, 10))

noun3 = customtkinter.CTkLabel(app, text="Noun", font=label)
noun3.grid(row=7, column=1)
noun3_input = customtkinter.CTkEntry(app)
noun3_input.grid(row=8, column=1, pady=(0, 10))

color = customtkinter.CTkLabel(app, text="Color", font=label)
color.grid(row=3, column=1)
color_input = customtkinter.CTkEntry(app)
color_input.grid(row=4, column=1, pady=(0, 10))

button = customtkinter.CTkButton(
    app,
    text="Go Mad!",
    font=botao, height=40,
    anchor="center",
    fg_color="#F6660D",
    hover_color="#cc5b14",
    command=madlibs,
)
button.grid(row=9, column=1, pady=(0, 10))

app.mainloop()
