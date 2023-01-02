import pygame as pg

from ..structures.Pos import Pos
from ..structures.Rect import Rect
from ..structures import Color
from ..structures.Surface import Surface

# It could have been DrawableObject but that's not finger friendly
class Object(object) :
    """
    "Object" contains the information about how something should be rendered
    on the screen.
    The content to be rendered is provided by subclasses that use this class
     it has padding, border and margin properties.
    But its functionality is completely different from HTML drawable objects.
    Since the rect parameter which is fed to this Object while initialization determines
     an absolute rendering point and  DOES NOT CHANGE IN RELATION TO OTHER OBJECTS.
    So the rectangular size of the content to be rendered is:
        content_width = rect.width - padding_horizontal + border_horizontal + margin_horizontal
        content_height = rect.height - padding_vertical + border_vertical + margin_vertical

    """
    def __init__( self, rect: Rect ) :

        self.rect: Rect = rect

        self.__padding_left = 0
        self.__padding_right = 0
        self.__padding_top = 0
        self.__padding_bottom = 0

        self.__margin_left = 0
        self.__margin_right = 0
        self.__margin_top = 0
        self.__margin_bottom = 0

        self.__border_left_width = 0
        self.__border_right_width = 0
        self.__border_top_width = 0
        self.__border_bottom_width = 0

        self.__border_color = Color.Constants.BLACK


        self.__left_neighbor: Object or None = None
        self.__right_neighbor: Object or None = None
        self.__top_neighbor: Object or None = None
        self.__bottom_neighbor: Object or None = None

        super(Object, self).__init__()


    @property
    def all_attrs( self ) -> str :
        text = "Object {\n"
        L = vars(self)
        for i in L :
            text += "\t" + str(i) + " = " + str(L[i]) + "\n"
        text += "}"
        return text


    @property
    def padding( self ) -> tuple[float,float,float,float]:
        return self.__padding_left, self.__padding_top, self.__padding_right, self.__padding_bottom


    @padding.setter
    def padding( self, new_padding: tuple[float, float, float, float] ) :
        self.__padding_left, self.__padding_top = new_padding[:2]
        self.__padding_right, self.__padding_bottom = new_padding[2 :]


    @property
    def margin( self ) -> tuple[float,float,float,float] :
        return self.__margin_left, self.__margin_top, self.__margin_right, self.__margin_bottom


    @margin.setter
    def margin( self, new_margin: tuple[float, float, float, float] ) :
        self.__margin_left, self.__margin_top = new_margin[:2]
        self.__margin_right, self.__margin_bottom = new_margin[2 :]


    @property
    def border( self ) -> tuple[int, int, int, int] :
        return self.__border_left_width, self.__border_top_width,\
            self.__border_right_width, self.__border_bottom_width


    @border.setter
    def border( self, new_border: tuple[int, int, int, int] ) :
        self.__border_left_width, self.__border_top_width = new_border[:2]
        self.__border_right_width, self.__border_bottom_width = new_border[2 :]


    @property
    def neighbors( self ) :
        return self.__left_neighbor, self.__top_neighbor, \
                self.__right_neighbor, self.__bottom_neighbor

    @neighbors.setter
    def neighbors( self,new_neighbors: tuple ):
        self.__padding_left, self.__padding_top = new_neighbors[:2]
        self.__padding_right, self.__padding_bottom = new_neighbors[2 :]

    def render( self ) :
        pass
