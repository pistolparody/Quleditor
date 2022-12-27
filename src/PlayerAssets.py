from pg_atlas import PGAtlas
from Structures.Sprite import Sprite
from Structures.MSprite import MSprite
import Structures.Constants as c


class PlayerAssets :

    def __init__( self ) :
        self.walk_east_sprites: list[Sprite] = []
        self.walk_west_sprites: list[Sprite] = []
        self.walk_north_sprites: list[Sprite] = []
        self.walk_south_sprites: list[Sprite] = []

        self.run_east_sprites: list[Sprite] = []
        self.run_west_sprites: list[Sprite] = []
        self.run_north_sprites: list[Sprite] = []
        self.run_south_sprites: list[Sprite] = []

        self.idle_east_sprites: list[Sprite] = []
        self.idle_west_sprites: list[Sprite] = []
        self.idle_north_sprites: list[Sprite] = []
        self.idle_south_sprites: list[Sprite] = []

        self.climb_east_sprites: list[Sprite] = []
        self.climb_west_sprites: list[Sprite] = []
        self.climb_north_sprites: list[Sprite] = []
        self.climb_south_sprites: list[Sprite] = []

        self.push_east_sprites: list[Sprite] = []
        self.push_west_sprites: list[Sprite] = []
        self.push_north_sprites: list[Sprite] = []
        self.push_south_sprites: list[Sprite] = []

        self.swing_east_sprites: list[Sprite] = []
        self.swing_west_sprites: list[Sprite] = []
        self.swing_north_sprites: list[Sprite] = []
        self.swing_south_sprites: list[Sprite] = []

        self.__load_atlas()

        walk_row = {
            c.EAST : self.walk_east_msprite,
            c.WEST : self.walk_west_msprite,
            c.NORTH : self.walk_north_msprite,
            c.SOUTH : self.walk_south_msprite
        }

        idle_row = {
            c.EAST : self.idle_east_msprite,
            c.WEST : self.idle_west_msprite,
            c.NORTH : self.idle_north_msprite,
            c.SOUTH : self.idle_south_msprite
        }

        run_row = {
            c.EAST : self.run_east_msprite,
            c.WEST : self.run_west_msprite,
            c.NORTH : self.run_north_msprite,
            c.SOUTH : self.run_south_msprite
        }
        climb_row = {
            c.EAST : self.climb_east_msprite,
            c.WEST : self.climb_west_msprite,
            c.NORTH : self.climb_north_msprite,
            c.SOUTH : self.climb_south_msprite
        }

        push_row = {
            c.EAST : self.push_east_msprite,
            c.WEST : self.push_west_msprite,
            c.NORTH : self.push_north_msprite,
            c.SOUTH : self.push_south_msprite
        }

        swing_row = {
            c.EAST : self.swing_east_msprite,
            c.WEST : self.swing_west_msprite,
            c.NORTH : self.swing_north_msprite,
            c.SOUTH : self.swing_south_msprite
        }

        self.atlas_table = {
            c.WALK : walk_row,
            c.IDLE : idle_row,
            c.RUN : run_row,
            c.CLIMB : climb_row,
            c.PUSH : push_row,
            c.SWING : swing_row
        }


    def __load_atlas( self ) :
        self.atlas = PGAtlas(
            "/home/yolo/Workstation/Python/pygame/Chaotic-Kung-Fu-Kid/assets/images/Kung-Fu-Kid"
            ".json")

        self.__load_idle_sprites()
        self.__load_walk_sprites()
        self.__load_run_sprites()
        self.__load_climb_sprites()
        self.__load_push_sprites()
        self.__load_swing_sprites()


        self.idle_east_msprite = MSprite(self.idle_east_sprites, 0.5)
        self.idle_west_msprite = MSprite(self.idle_west_sprites, 0.5)
        self.idle_north_msprite = MSprite(self.idle_north_sprites, 0.5)
        self.idle_south_msprite = MSprite(self.idle_south_sprites, 0.5)

        self.climb_east_msprite = MSprite(self.climb_east_sprites, 0.5)
        self.climb_west_msprite = MSprite(self.climb_west_sprites, 0.5)
        self.climb_north_msprite = MSprite(self.climb_north_sprites, 0.5)
        self.climb_south_msprite = MSprite(self.climb_south_sprites, 0.5)

        self.walk_east_msprite = MSprite(self.walk_east_sprites, 0.2)
        self.walk_west_msprite = MSprite(self.walk_west_sprites, 0.2)
        self.walk_north_msprite = MSprite(self.walk_north_sprites, 0.2)
        self.walk_south_msprite = MSprite(self.walk_south_sprites, 0.2)

        self.push_east_msprite = MSprite(self.push_east_sprites, 0.5)
        self.push_west_msprite = MSprite(self.push_west_sprites, 0.5)
        self.push_north_msprite = MSprite(self.push_north_sprites, 0.5)
        self.push_south_msprite = MSprite(self.push_south_sprites, 0.5)

        self.swing_east_msprite = MSprite(self.swing_east_sprites, 0.1)
        self.swing_west_msprite = MSprite(self.swing_west_sprites, 0.1)
        self.swing_north_msprite = MSprite(self.swing_north_sprites, 0.1)
        self.swing_south_msprite = MSprite(self.swing_south_sprites, 0.1)

        self.run_east_msprite = MSprite(self.run_east_sprites, 0.2)
        self.run_west_msprite = MSprite(self.run_west_sprites, 0.2)
        self.run_north_msprite = MSprite(self.run_north_sprites, 0.2)
        self.run_south_msprite = MSprite(self.run_south_sprites, 0.2)




    def __load_idle_sprites( self ) :
        self.idle_west_sprites = [f"Idle_WEST_{str(i)}.png" for i in range(4)]
        self.idle_east_sprites = [f"Idle_EAST_{str(i)}.png" for i in range(4)]
        self.idle_north_sprites = [f"Idle_NORTH_{str(i)}.png" for i in range(4)]
        self.idle_south_sprites = [f"Idle_SOUTH_{str(i)}.png" for i in range(4)]

        self.idle_west_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.idle_west_sprites]

        self.idle_east_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.idle_east_sprites]

        self.idle_north_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.idle_north_sprites]

        self.idle_south_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.idle_south_sprites]


    def __load_walk_sprites( self ) :
        self.walk_west_sprites = [f"Walk_WEST_{str(i)}.png" for i in range(4)]
        self.walk_east_sprites = [f"Walk_EAST_{str(i)}.png" for i in range(4)]
        self.walk_north_sprites = [f"Walk_NORTH_{str(i)}.png" for i in range(4)]
        self.walk_south_sprites = [f"Walk_SOUTH_{str(i)}.png" for i in range(4)]

        self.walk_west_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.walk_west_sprites]

        self.walk_east_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.walk_east_sprites]

        self.walk_north_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.walk_north_sprites]

        self.walk_south_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.walk_south_sprites]


    def __load_run_sprites( self ) :
        self.run_west_sprites = [f"Run_WEST_{str(i)}.png" for i in range(4)]
        self.run_east_sprites = [f"Run_EAST_{str(i)}.png" for i in range(4)]
        self.run_north_sprites = [f"Run_NORTH_{str(i)}.png" for i in range(4)]
        self.run_south_sprites = [f"Run_SOUTH_{str(i)}.png" for i in range(4)]

        self.run_west_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.run_west_sprites]

        self.run_east_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.run_east_sprites]

        self.run_north_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.run_north_sprites]

        self.run_south_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.run_south_sprites]


    def __load_climb_sprites( self ) :
        self.climb_west_sprites = [f"Climb_WEST_{str(i)}.png" for i in range(4)]
        self.climb_east_sprites = [f"Climb_EAST_{str(i)}.png" for i in range(4)]
        self.climb_north_sprites = [f"Climb_NORTH_{str(i)}.png" for i in range(4)]
        self.climb_south_sprites = [f"Climb_SOUTH_{str(i)}.png" for i in range(4)]

        self.climb_west_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.climb_west_sprites]

        self.climb_east_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.climb_east_sprites]

        self.climb_north_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.climb_north_sprites]

        self.climb_south_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.climb_south_sprites]


    def __load_swing_sprites( self ) :
        self.swing_west_sprites = [f"Swing_WEST_{str(i)}.png" for i in range(4)]
        self.swing_east_sprites = [f"Swing_EAST_{str(i)}.png" for i in range(4)]
        self.swing_north_sprites = [f"Swing_NORTH_{str(i)}.png" for i in range(4)]
        self.swing_south_sprites = [f"Swing_SOUTH_{str(i)}.png" for i in range(4)]

        self.swing_west_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.swing_west_sprites]

        self.swing_east_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.swing_east_sprites]

        self.swing_north_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.swing_north_sprites]

        self.swing_south_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.swing_south_sprites]


    def __load_push_sprites( self ) :
        self.push_west_sprites = [f"Push_WEST_{str(i)}.png" for i in range(4)]
        self.push_east_sprites = [f"Push_EAST_{str(i)}.png" for i in range(4)]
        self.push_north_sprites = [f"Push_NORTH_{str(i)}.png" for i in range(4)]
        self.push_south_sprites = [f"Push_SOUTH_{str(i)}.png" for i in range(4)]

        self.push_west_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.push_west_sprites]

        self.push_east_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.push_east_sprites]

        self.push_north_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.push_north_sprites]

        self.push_south_sprites = [Sprite(surface=self.atlas.create_image(i)) for i in
            self.push_south_sprites]