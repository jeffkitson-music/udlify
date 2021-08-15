from appJar import gui


def press():
    badtext = app.getTextArea("text")
    goodtext = badtext.title()
    app.clearTextArea("text")
    app.setTextArea("text",goodtext)


def clear():
    app.clearTextArea("text")


def clipboard():
    app.topLevel.clipboard_clear()
    app.topLevel.clipboard_append(app.getTextArea("text"))


with gui("UDL-izer", "700x400", bg='#006747', font={'size':32}) as app:
    app.label("UDL-izer", bg='#bec6c4', fg='#006747')
    app.enableEnter(press)
    app.setPadding([5,5])
    #app.setInPadding([10,10])
    app.textArea("text")
    app.buttons(["✔","✖", "✂", "✌"], [press,clear, clipboard, app.stop])
