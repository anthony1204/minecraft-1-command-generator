import PySimpleGUI as sg
import pyperclip
layout = [[sg.Text("anthony4933/discord's 1 command generator for minecraft 1.20")],[sg.Text("this will create a file called cmds in the directory!")],
           [sg.Multiline("cmds",write_only=False,size=(25,10,),key='cmds')],[sg.Button("generate",key="gen")],[sg.Button("close")]]
window = sg.Window("Anthony Command Generator 3000", layout,margins=(200,100),background_color="#397400")
while True:
    event, values = window.read()
    if event == "close" or event == sg.WIN_CLOSED:
        sg.popup('dont leave :()')
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
                out += ''
                out += "{id:command_block_minecart,Command:'"+ i +"'},"
            out += "{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:\"fill ~ ~ ~ ~ ~-3 ~ air\"}'},"
            out += "{id:command_block_minecart,Command:'kill @e[type=command_block_minecart,distance=..1]'}]}]}]}"
            sg.popup("command copied to clipboard!\n"+out)
            pyperclip.copy(out)
window.close()