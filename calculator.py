from __future__ import annotations

import typing

import urwid


num1: str = input("enter the 1st number: ")

if '.' in num1:
  num1 = float(num1)

elif ',' in num1:
    num1 = num1.replace(',', '.')
    num1 = float(num1)

elif num1.isdigit():
    num1 = int(num1)

print(num1) 
print(type(num1))   

num2: str = input("enter the 2st number: ")

if '.' in num2:
  num2 = float(num2)

elif ',' in num2:
    num2 = num2.replace(',', '.')
    num2 = float(num2)

elif num2.isdigit():
    num2 = int(num2)

if typing.TYPE_CHECKING:
    from collections.abc import Iterable

choices = "+ - * /".split()


def menu(title: str, choices_: Iterable[str]) -> urwid.ListBox:
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices_:
        button = urwid.Button(c)
        urwid.connect_signal(button, "click", item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map="reversed"))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def item_chosen(button: urwid.Button, choice: str) -> None:
    """Executa a operação matemática baseada na escolha do usuário."""
    if choice == "+":
        result = num1 + num2
    elif choice == "-":
        result = num1 - num2
    elif choice == "*":
        result = num1 * num2
    elif choice == "/":
        result = num1 / num2 if num2 != 0 else "Erro: divisão por zero"
    else:
        result = "Operação inválida"

    response = urwid.Text([f"Você escolheu {choice}, resultado: {result}\n"])
    done = urwid.Button("Ok")
    urwid.connect_signal(done, "click", exit_program)

    main.original_widget = urwid.Filler(
        urwid.Pile(
            [
                response,
                urwid.AttrMap(done, None, focus_map="reversed"),
            ]
        )
    )


def exit_program(button: urwid.Button) -> None:
    """Encerra o programa."""
    raise urwid.ExitMainLoop()





main = urwid.Padding(menu("Operador", choices), left=2, right=2)
top = urwid.Overlay(
    main,
    urwid.SolidFill("\N{MEDIUM SHADE}"),
    align=urwid.CENTER,
    width=(urwid.RELATIVE, 60),
    valign=urwid.MIDDLE,
    height=(urwid.RELATIVE, 60),
    min_width=20,
    min_height=9,
)
urwid.MainLoop(top, palette=[("reversed", "standout", "")]).run()   
