import PySimpleGUI as sg
import os
spu = False #if ur looking at this, this just checks if you have seen the copied to clipboard before
layout = [[sg.Text("anthony4933/discord's 1 command generator for minecraft 1.20")],[sg.Multiline("cmds",write_only=False,size=(40,10),key='cmds')],[sg.Button("generate",key="gen")],[sg.Button("generate /give command block",key="gencmd")],[sg.Button("close")]]
window = sg.Window("Anthony Command Generator 3000",layout,margins=(200,100),background_color="#397400",icon="ico.ico",titlebar_icon="ico.ico")
while True:
    event, values = window.read()
    if event == "close" or event == sg.WIN_CLOSED:
        break
    if event == "gen":
        file = open('cmds','w+')
        file.write(values['cmds'])
        file.close()
        with open("cmds") as f:
            cmds = [ i.split("\n")[0] for i in f.readlines() ]
            out = 'summon falling_block ~ ~.5 ~ {Time:1,BlockState:{Name:redstone_block},Passengers:[{id:armor_stand,Health:0,Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},Passengers:['
            out += "{id:command_block_minecart,Command:'gamerule commandBlockOutput false'},"
            for i in cmds:
                out += "{id:command_block_minecart,Command:'"+ i +"'},"
            out += "{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:\"fill ~ ~ ~ ~ ~-3 ~ air\"}'},"
            out += "{id:command_block_minecart,Command:'kill @e[type=command_block_minecart,distance=..2]'}]}]}]}"
            if spu == False:
                sg.popup_auto_close("the command is copied to clipboard! this will only be shown once",auto_close_duration=1.6)
                spu = True
            sg.clipboard_set(out)
    if event== "gencmd":
        sg.popup_animated("sad.gif","not a feature implemented yet! click on the window behind to close",keep_on_top=False)
if os.path.exists("cmds"):
    os.remove("cmds")
window.close()