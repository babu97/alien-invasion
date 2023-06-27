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

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color = (60,60,60)

        self.bullets_allowed = 3
        #alien settings
        self.alien_speed = 1.0 
        self.fleet_drop_speed = 10    
        #fleet direction represent  1  represents right and -1 left respectively
        self.fleet_direction = 1



        

        
        