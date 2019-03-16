# screen constants
class screen:
    Width = 1000
    Height = 500


# table constants
class table:
    Width = 900
    Height = 400
    Left = 50
    Top = 50
    Color = (18, 104, 54)

    class Frame:
        Thickness = 30
        Color = (107, 75, 59)


# hole constants
class hole:
    Radius = 20
    Diameter = 40
    TopPosition = 50
    BottomPosition = screen.Height - 50
    InitialHorizontalPosition = 50


# 16 balls initial position
class ball:
    balls = []


# color
class color:
    White = (255, 255, 255)
    Black = (0, 0, 0)
