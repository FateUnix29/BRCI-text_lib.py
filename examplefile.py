import BRCI as brci
import text_lib
import os
filedir = os.path.dirname(os.path.realpath(__file__))
data = brci.BRCI()
data.project_name = 'texttest'
data.project_display_name = 'Text Test'
data.project_folder_directory = os.path.join(filedir, 'Projects')
data.file_description = 'Testing the text_lib module.'
data.visibility = 0
data.logs = ['time']
data.write_blank = False
generate = True

curx, cury = 0, 0

curx, cury, _ = text_lib.split_text_bricks(data, 
                           "These text bricks were generated using BRCI,\nand the library of Destiny's design,\ncalled text_lib.py. If you want to see BRCI,\nand or text_lib, go to the link below!\nThis is a showcase for what BRCI can do as well.\n\nThe link can be found here:\n",
                           material="Steel",
                           debug=False)

text_lib.split_text_bricks(data, "https://discord.gg/4cEgcbhHHV", debug=False,
                           material="Steel", xstart=curx, ystart=cury, brickcolorHSVA=[0, 0, 0, 255], textcolorHSV=[17, 255, 255])

if generate:
    data.write_preview()
    data.write_metadata()
    data.write_brv()
    data.write_to_br()
    data.clear_bricks()
