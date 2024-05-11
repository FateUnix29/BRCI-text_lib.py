from BRCI import BRCI as BRCI_class

def split_text_bricks(brci_instance: BRCI_class, text: str = "Hello World!", brickcolorHSVA: list[int] = [0, 0, 127, 255], textcolorHSV: list[int] = [0, 0, 0], material: str = "Plastic", xspacing: int = 10, yspacing: int = 10, rotation: list[int] = [0, 0, -90], textbrick: str = "Nameplate_1sx1sx1s", xstart: int = 0, ystart: int = 0, debug: bool = False):
    """Gives each character in variable 'text' it's own text brick. \\n will cause it to place text bricks below the previous ones.

    Args:
        brci_instance (BRCI): BRCI instance
        text (str, optional): Text to split. Defaults to "Hello World!".
        brickcolorHSVA (list[int], optional): Color of the text bricks. Defaults to [0, 0, 127, 255].
        textcolorHSV (list[int], optional): Color of the text. Defaults to [0, 0, 0].
        material (str, optional): Material of the text bricks. Defaults to "Plastic".
        xspacing (int, optional): Horizontal spacing between text bricks. Defaults to 10.
        yspacing (int, optional): Vertical spacing between text bricks. Defaults to 10.
        rotation (list[int], optional): Rotation of the text bricks. Defaults to [0, 0, -90].
        textbrick (str, optional): Text brick to use. Defaults to "Nameplate_1sx1sx1s".
        xstart (int, optional): Starting x position. Defaults to 0.
        ystart (int, optional): Starting y position. Defaults to 0.
        debug (bool, optional): Whether to print debug messages. Defaults to False.
    
    Raises:
        ValueError: If textbrick is not a valid text brick (Text cylinders do not count)
        
    Returns:
        both final values of the pointer (x and y variables), so you can chain this function with itself, and the BRCI instance."""
    
    available_textbricks = [
        "Nameplate_1sx1sx1s",
        "Nameplate_1x1sx1s",
        "Nameplate_1x1x1s",
        #"NameZylinder_1x1x1s", # Zylinders will not connect by their sides, so they'll be loose bricks..
        "Nameplate_2x1sx1s",
        "Nameplate_2x1x1s",
        "Nameplate_2x2x1s",
        #"NameZylinder_2x2x1s", # Zylinders will not connect by their sides, so they'll be loose bricks..
        "Nameplate_4x1x1s",
        "Nameplate_4x2x1s",
        "Nameplate_6x1x1s",
        "Nameplate_6x2x1s",
        "Nameplate_8x1x1s",
        "Nameplate_8x2x1s"
    ]

    if textbrick not in available_textbricks:
        raise ValueError(f"Text brick {textbrick} does not seem to exist. Please use one of the following: {available_textbricks}")

    brick2add = textbrick
    filler = "ScalableBrick"
    x, y = xstart, ystart # Initialize the positions
    lastnewline = False # Keep track of whether the last character was a newline
    for curindex, letter in enumerate(text, start=0):
        if letter != "\n":
            if debug: print(f"{curindex}: {letter}")
            if letter != " ": brci_instance.add_new_brick(str(curindex), brick2add, position=[y, x, 0], brick={"Text": letter, "Rotation": rotation, "BrickColor": brickcolorHSVA, "TextColor": textcolorHSV, "BrickMaterial": material})
            else:
                brci_instance.add_new_brick(str(curindex), filler, position=[y, x, 5], brick={"BrickSize": [1, 1, 1], "BrickColor": brickcolorHSVA, "BrickMaterial": material})
            x += xspacing
            if debug: print(f"{x}, {y}")
            lastnewline = False
        else:
            if debug: print(f"{curindex}: {letter}")
            y -= yspacing; x = 0
            if debug: print(f"{x}, {y}")
            if lastnewline:
                y += yspacing; x = 0 # Go back to the previous line
                brci_instance.add_new_brick(str(curindex), filler, position=[y, x, 5], brick={"BrickSize": [1, 1, 1], "BrickColor": brickcolorHSVA, "BrickMaterial": material}) # Make a 1/3 x 1/3 x 1/3 filler brick so it doesn't get cut off
                y -= yspacing # Go back to the current line
            lastnewline = True
    return x, y, brci_instance
