from PlanetClass import *

pygame.init()
pygame.display.set_caption("Gravity")

x = 1400
y = 800
center_x = 0
center_y = 0
screen = pygame.display.set_mode((x, y))

G = 0.05  # constant which gets multiplied by all the forces to make things work differently
new_mass = 64

planets = [Planet(2000, 0, 0, 0, 0)]

screen.fill((0, 0, 0))
for planet in planets:
    planet.draw(screen, x, y, center_x, center_y)

total_planets = len(planets)  # stores the number of bodies for the counter in the top left
font = pygame.font.Font('freesansbold.ttf', 32)
body_text = font.render(f"Bodies: {total_planets}", True, (255, 255, 255), (0, 0, 0))
body_text_rect = body_text.get_rect()
body_text_rect.top = 0
body_text_rect.left = 0
screen.blit(body_text, body_text_rect)
g_text = font.render(f"G: {G}", True, (255, 255, 255), (0, 0, 0))
g_text_rect = g_text.get_rect()
g_text_rect.top = 0
g_text_rect.left = 250
screen.blit(g_text, g_text_rect)
new_mass_text = font.render(f"New Mass: {new_mass}", True, (255, 255, 255), (0, 0, 0))
new_mass_text_rect = new_mass_text.get_rect()
new_mass_text_rect.top = 0
new_mass_text_rect.right = x - 100
screen.blit(new_mass_text, new_mass_text_rect)
paused_text = font.render("Paused", True, (255, 255, 255), (0, 0, 0))
paused_text_rect = paused_text.get_rect()
paused_text_rect.bottom = y
paused_text_rect.right = x
screen.blit(paused_text, paused_text_rect)

done = False
running = False
trail = False
drawing = False
throw_ready = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # toggle the program's functionality
                if running:
                    running = False
                    screen.blit(paused_text, paused_text_rect)
                else:
                    screen.fill((0, 0, 0))
                    running = True
            elif event.key == pygame.K_t:  # toggle trails
                trail = not trail
            elif event.key == pygame.K_c:  # center the screen on the biggest mass
                screen.fill((0, 0, 0))
                maximum_mass = 0
                for planet in planets:
                    if planet.mass > maximum_mass:
                        maximum_mass = planet.mass
                for planet in planets:
                    if planet.mass == maximum_mass:
                        center_x = planet.pos_x
                        center_y = planet.pos_y
            elif event.key == pygame.K_m:  # move the camera at the same speed as the largest object (essentially change reference frame)
                screen.fill((0, 0, 0))
                maximum_mass = 0
                for planet in planets:
                    if planet.mass > maximum_mass:
                        maximum_mass = planet.mass
                for planet in planets:
                    if planet.mass == maximum_mass:
                        for other_planet in planets:
                            other_planet.vel_x -= planet.vel_x
                            other_planet.vel_y -= planet.vel_y
                        break
            elif event.key == pygame.K_UP:
                G += 0.01
            elif event.key == pygame.K_DOWN:
                G -= 0.01
            elif event.key == pygame.K_LEFT and new_mass >= 2:
                new_mass /= 2
            elif event.key == pygame.K_RIGHT:
                new_mass *= 2
            elif event.key == pygame.K_r:
                screen.fill((0, 0, 0))
                planets = [Planet(2000, 0, 0, 0, 0)]
                center_x = 0
                center_y = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            origin_x = pygame.mouse.get_pos()[0]
            origin_y = pygame.mouse.get_pos()[1]
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            destination_x = pygame.mouse.get_pos()[0]
            destination_y = pygame.mouse.get_pos()[1]
            throw_ready = True
    if running:
        if not trail:
            screen.fill((0, 0, 0))
        if drawing:
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, (255, 255, 255), (origin_x, origin_y), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        elif throw_ready:
            screen.fill((0, 0, 0))
            planets.append(Planet(new_mass, origin_x - x / 2 + center_x, origin_y - y / 2 + center_y, (destination_x - origin_x) / 20, (destination_y - origin_y) / 20))
            total_planets += 1
            throw_ready = False
        for planet in planets:
            if planet.alive:
                if planet.colliding(planets):  # detects planetary collisions
                    total_planets -= 1
                    other_planet = planet.colliding(planets)
                    planet.alive = False
                    other_planet.alive = False
                    combined_mass = planet.mass + other_planet.mass  # calculates the properties of the new combined planet
                    bigger_planet = max(planet, other_planet)
                    x_momentum_before_collision = planet.mass * planet.vel_x + other_planet.mass * other_planet.vel_x
                    y_momentum_before_collision = planet.mass * planet.vel_y + other_planet.mass * other_planet.vel_y
                    new_vel_x = x_momentum_before_collision / combined_mass
                    new_vel_y = y_momentum_before_collision / combined_mass
                    planets.append(Planet(combined_mass, bigger_planet.pos_x, bigger_planet.pos_y, new_vel_x, new_vel_y))
                planet.calculate(planets, G)  # calculates all gravitational forces on a body
                planet.draw(screen, x, y, center_x, center_y)
            planet.vectors = []  # resets the forces for recalculation in the next frame
    body_text = font.render(f"Bodies: {total_planets}", True, (255, 255, 255), (0, 0, 0))  # redraws the text every frame
    screen.blit(body_text, body_text_rect)
    g_text = font.render(f"G: {round(G, 2)}", True, (255, 255, 255), (0, 0, 0))
    screen.blit(g_text, g_text_rect)
    new_mass_text = font.render(f"New Mass: {round(new_mass)}", True, (255, 255, 255), (0, 0, 0))
    screen.blit(new_mass_text, new_mass_text_rect)
    pygame.display.update()
