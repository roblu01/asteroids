import pygame, sys
from constants import *   
from player import Player
from shot import Shot
from asteroid import Asteroid
from circleshape import CircleShape
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()   #pygame groups
    drawable = pygame.sprite.Group()    #pygame groups
    Player.containers = (updatable,drawable)    #pygame groups

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        #player.update(dt)
        #player.draw(screen)
        updatable.update(dt)  #pygame groups
        for obj in drawable:  #pygame groups
            obj.draw(screen)  #pygame groups
        for obj in asteroids:
            if obj.collision(player) == True:
                sys.exit("Game over!")

        pygame.display.flip()
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
