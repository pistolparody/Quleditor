""" readme
classes defined here mostly extend built-in pygame classes.
I call them L1 or layer 1 classes. (L0 is layer 0 pygame&python classes and functions)

classes defined in L1 only use structures from L0 or L1

Color.py inherits pg.color.Color
Pos.py inherits pg.math.Vector2
Rect.py inherits pg.rect.Rect
Surface inherits pg.surface.Surface

Color uses nothing
Pos uses nothing
Rect uses Pos
Surface uses Color,Pos,Rect
"""