"""Sphere sample application"""
import time
import math
import pygame
import sys

from quaternion import Quaternion

from scene import Scene
from object3d import Object3d
from camera import Camera
from mesh import Mesh
from material import Material
from color import Color
from vector3 import Vector3

# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    screenX = 640
    screenY = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((screenX, screenY))

    # Create a scene
    scene = Scene("TesteCena")
    scene.camera = Camera(False, screenX, screenY)

    # Moves the camera back 2 units
    scene.camera.position -= Vector3(0, 0, 2)

    # Create a sphere and place it in a scene, at position (0,0,0)
    obj = Object3d("Object")
    obj.scale = Vector3(1, 1, 1)
    obj.position = Vector3(0, 0, 0)

    #Number of sides of the cilinder
    sides = 12

    #Create a cilinder
    obj.mesh = Mesh.create_cylinder(sides, 1, 1, None)

    #Create a sphere
    #obj.mesh = Mesh.create_sphere((1, 1, 1), 12, 12)
    
    #Create a cube
    #obj.mesh = Mesh.create_cube((5, 5, 5))
    
    obj.material = Material(Color(1, 0, 0, 1), "Material1")
    scene.add_object(obj)

    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)

    # Game loop, runs forever
    while True:
         #Busca o evento
        events = pygame.event.get()
        key = pygame.key.get_pressed()
        ang = 20

        #Quando é carregada a tecla W
        if key[pygame.K_w]:
            movement = Vector3(0, 1, 0)
            movement.normalize()
            obj.position = obj.position + movement * delta_time

        #Quando é carregada a tecla S
        if key[pygame.K_s]:
            movement = Vector3(0, -1, 0)
            movement.normalize()
            obj.position = obj.position + movement * delta_time

        #Quando é carregada a tecla A
        if key[pygame.K_a]:
            movement = Vector3(-1, 0, 0)
            movement.normalize()
            obj.position = obj.position + movement * delta_time

        #Quando é carregada a tecla D
        if key[pygame.K_d]:
            movement = Vector3(1, 0, 0)
            movement.normalize()
            obj.position = obj.position + movement * delta_time

        #Quando é carregada a tecla Q
        if key[pygame.K_q]:
            movement = Vector3(0, 0, 1)
            movement.normalize()
            obj.position = obj.position + movement * delta_time

        #Quando é carregada a tecla E
        if key[pygame.K_e]:
            movement = Vector3(0, 0, -1)
            movement.normalize()
            obj.position = obj.position + movement * delta_time
        
        #Quando é carregada a seta para a direita
        if key[pygame.K_RIGHT]:
            rot = Vector3(0, -1, 0)
            q = Quaternion.AngleAxis(rot.normalized(), math.radians(ang) * delta_time)
            obj.rotation = q * obj.rotation

        #Quando é carregada a seta para a esquerda
        if key[pygame.K_LEFT]:
            rot = Vector3(0, 1, 0)
            q = Quaternion.AngleAxis(rot.normalized(), math.radians(ang) * delta_time)
            obj.rotation = q * obj.rotation
            
        #Quando é carregada a seta para baixo
        if key[pygame.K_DOWN]:
            rot = Vector3(-1, 0, 0)
            q = Quaternion.AngleAxis(rot.normalized(), math.radians(ang) * delta_time)
            obj.rotation = q * obj.rotation

        #Quando é carregada a seta para cima
        if key[pygame.K_UP]:
            rot = Vector3(1, 0, 0)
            q = Quaternion.AngleAxis(rot.normalized(), math.radians(ang) * delta_time)
            obj.rotation = q * obj.rotation

        #Quando é carregada a tecla PgUp
        if key[pygame.K_PAGEUP]:
            rot = Vector3(0, 0, 1)
            q = Quaternion.AngleAxis(rot.normalized(), math.radians(ang) * delta_time)
            obj.rotation = q * obj.rotation

        #Quando é carregada a tecla PgDn
        if key[pygame.K_PAGEDOWN]:
            rot = Vector3(0, 0, -1)
            q = Quaternion.AngleAxis(rot.normalized(), math.radians(ang) * delta_time)
            obj.rotation = q * obj.rotation

        for event in events:
            #Quando é carregada a tecla ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                    
            #Quando é carregado o botão para sair do programa
            if event.type == pygame.QUIT:
                exit()

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0, 0, 0))

        # Rotates the object, considering the time passed (not linked to frame rate)
    #    ax = (axis * math.radians(angle) * delta_time)

    #    q = Quaternion.AngleAxis(axis, math.radians(angle) * delta_time)
    #    obj1.rotation = q * obj1.rotation

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()