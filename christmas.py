import customtkinter

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title('Madlibs - Christmas')


def madlibs():
    madlib = (f"I am so excited for Christmas this year! I've been doing a lot of {verb1_input.get()}ing"
              f" to prepare! I have already picked presents for everyone. I got {person1_input.get()} a "
              f"{noun1_input.get()}, and {person2_input.get()} a {noun2_input.get()}. I wrapped their "
              f"presents in {noun3_input.get()} and hid them in the {room1_input.get()} so they wouldn't "
              f"find them. {person3_input.get().capitalize()} and I made {food_input.get()} for everyone "
              f"to enjoy. They smell {adj1_input.get()}! I can't wait to eat them. We picked out the "
              f"perfect tree. It is {adj2_input.get()}, and {adj3_input.get()} and smells like {scent_input.get()}. "
              f"It's my job to {verb2_input.get()} the tree every day. I've been hoping for a {noun4_input.get()} "
              f"under the Christmas tree this year. I really don't want to get a {noun5_input.get()} this year! "
              f"{person4_input.get().capitalize()} tells me that I need to go to bed early on Christmas Eve so "
              f"Santa can come. He's going to drive his {transport_input.get()} with his {animal_input.get()} and "
              f"land on our roof. I hope everyone has a {adj4_input.get()} Christmas!")

    entradas = [
        verb1_input.get(), person1_input.get(), noun1_input.get(), person2_input.get(),
        noun2_input.get(), noun3_input.get(), room1_input.get(), person3_input.get(),
        food_input.get(), adj1_input.get(), adj2_input.get(), adj3_input.get(),
        scent_input.get(), verb2_input.get(), noun4_input.get(), noun5_input.get(),
        person4_input.get(), transport_input.get(), animal_input.get(), adj4_input.get()
    ]

    if "" in entradas:
        label_entradas = customtkinter.CTkLabel(app, text="Preencha todos os campos",
                                                font=label)
        label_entradas.grid(row=10, column=2, pady=(0, 10))
    else:
        toplevel = customtkinter.CTkToplevel(app)
        label_toplevel = customtkinter.CTkLabel(toplevel, text="Christmas Night", font=titulo)
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
label_titulo = customtkinter.CTkLabel(app, text="Snowy Mad Libs", font=titulo, padx=10, pady=10)
label_titulo.grid(column=2)

adj1 = customtkinter.CTkLabel(app, text="Adjective", font=label)
adj1.grid(row=3, column=4)
adj1_input = customtkinter.CTkEntry(app)
adj1_input.grid(row=4, column=4, padx=10, pady=(0, 10))

adj2 = customtkinter.CTkLabel(app, text="Adjective", font=label)
adj2.grid(row=5, column=0)
adj2_input = customtkinter.CTkEntry(app)
adj2_input.grid(row=6, column=0, padx=10, pady=(0, 10))

adj3 = customtkinter.CTkLabel(app, text="Adjective", font=label)
adj3.grid(row=5, column=1)
adj3_input = customtkinter.CTkEntry(app)
adj3_input.grid(row=6, column=1, pady=(0, 10))

adj4 = customtkinter.CTkLabel(app, text="Adjective", font=label)
adj4.grid(row=7, column=4)
adj4_input = customtkinter.CTkEntry(app)
adj4_input.grid(row=8, column=4, pady=(0, 10))

person1 = customtkinter.CTkLabel(app, text="Person", font=label)
person1.grid(row=1, column=1)
person1_input = customtkinter.CTkEntry(app)
person1_input.grid(row=2, column=1, padx=(0, 10), pady=(0, 10))

person2 = customtkinter.CTkLabel(app, text="Person", font=label)
person2.grid(row=1, column=3)
person2_input = customtkinter.CTkEntry(app)
person2_input.grid(row=2, column=3, padx=(0, 10), pady=(0, 10))

person3 = customtkinter.CTkLabel(app, text="Person", font=label)
person3.grid(row=3, column=2)
person3_input = customtkinter.CTkEntry(app)
person3_input.grid(row=4, column=2, pady=(0, 10))

person4 = customtkinter.CTkLabel(app, text="Person", font=label)
person4.grid(row=7, column=1)
person4_input = customtkinter.CTkEntry(app)
person4_input.grid(row=8, column=1, pady=(0, 10))

verb1 = customtkinter.CTkLabel(app, text="Verb", font=label)
verb1.grid(row=1, column=0)
verb1_input = customtkinter.CTkEntry(app)
verb1_input.grid(row=2, column=0, pady=(0, 10), padx=10)

verb2 = customtkinter.CTkLabel(app, text="Verb", font=label)
verb2.grid(row=5, column=3)
verb2_input = customtkinter.CTkEntry(app)
verb2_input.grid(row=6, column=3, pady=(0, 10))

scent = customtkinter.CTkLabel(app, text="Scent", font=label)
scent.grid(row=5, column=2)
scent_input = customtkinter.CTkEntry(app)
scent_input.grid(row=6, column=2, pady=(0, 10))

noun1 = customtkinter.CTkLabel(app, text="Noun", font=label)
noun1.grid(row=1, column=2)
noun1_input = customtkinter.CTkEntry(app)
noun1_input.grid(row=2, column=2, pady=(0, 10))

noun2 = customtkinter.CTkLabel(app, text="Noun", font=label)
noun2.grid(row=1, column=4)
noun2_input = customtkinter.CTkEntry(app)
noun2_input.grid(row=2, column=4, padx=(0, 10), pady=(0, 10))

noun3 = customtkinter.CTkLabel(app, text="Noun", font=label)
noun3.grid(row=3, column=0)
noun3_input = customtkinter.CTkEntry(app)
noun3_input.grid(row=4, column=0, pady=(0, 10))

noun4 = customtkinter.CTkLabel(app, text="Noun", font=label)
noun4.grid(row=5, column=4)
noun4_input = customtkinter.CTkEntry(app)
noun4_input.grid(row=6, column=4, pady=(0, 10))

noun5 = customtkinter.CTkLabel(app, text="Noun", font=label)
noun5.grid(row=7, column=0)
noun5_input = customtkinter.CTkEntry(app)
noun5_input.grid(row=8, column=0, pady=(0, 10))

food = customtkinter.CTkLabel(app, text="Food", font=label)
food.grid(row=3, column=3)
food_input = customtkinter.CTkEntry(app)
food_input.grid(row=4, column=3, pady=(0, 10))

room1 = customtkinter.CTkLabel(app, text="Room", font=label)
room1.grid(row=3, column=1)
room1_input = customtkinter.CTkEntry(app)
room1_input.grid(row=4, column=1, pady=(0, 10))

transport = customtkinter.CTkLabel(app, text="Transportation", font=label)
transport.grid(row=7, column=2)
transport_input = customtkinter.CTkEntry(app)
transport_input.grid(row=8, column=2, pady=(0, 10))

animal = customtkinter.CTkLabel(app, text="Animal", font=label)
animal.grid(row=7, column=3)
animal_input = customtkinter.CTkEntry(app)
animal_input.grid(row=8, column=3, pady=(0, 10))

button = customtkinter.CTkButton(
    app,
    text="Go Mad!",
    font=botao, height=40,
    anchor="center",
    fg_color="#8B0000",
    hover_color="#E60909",
    command=madlibs,
)
button.grid(row=9, column=2, pady=(0, 10))

app.mainloop()
