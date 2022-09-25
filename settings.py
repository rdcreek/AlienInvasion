class Settings:
    #This is a class to store all of the settings for the game.

    def __init__(self):
        #initialize the game's settings

        #Ship Settings
        self.ship_speed = 2.0

        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (66, 245, 236)

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
