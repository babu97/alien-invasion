class Settings:
    """A class that stores alien settings"""
    def __init__(self) -> None:
        """Initialize game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250,250,250)
        #Ship settings 
        self.ship_speed = 1.5
        self.ship_limit = 3
        

        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color = (60,60,60)

        self.bullets_allowed = 3
        #alien settings
        self.alien_speed = 1.0 
        self.fleet_drop_speed = 10 

        #how quickly the game speeds up e_dynam
        self.speedup_scale = 1.1

        self. initialize_dynamic_setting() 
        #fleet direction represent  1  represents right and -1 left respectively
        self.fleet_direction = 1

    def initialize_dynamic_setting(self):
        """Initialize settings that change throughout the game."""
        self.ship = 1.5
        self.bullet_speed =3.0
        self.alien_speed =1.0
        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed settings."""
        self.ship_speed *=self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale





        

        
        