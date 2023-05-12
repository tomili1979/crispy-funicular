import pygame
import random
import asyncio
pygame.init()


async def main():
    black = (0, 0, 0)
    gold = (255, 224, 145)
    blue = (131, 153, 120)
    blue2 = (10, 10, 255)
    purple = (100, 0, 100)
    green = (25, 255, 50)
    red = (255, 0, 0)

    dis = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()

    # font
    my_font = pygame.font.SysFont("ve", 70, False, False)
    my_text_1 = my_font.render("A", True, blue2)
    my_text_2 = my_font.render("C", True, blue2)
    my_text_3 = my_font.render("B", True, red)
    my_text_4 = my_font.render("D", True, red)
    my_text_5 = my_font.render("A", True, red)
    my_text_6 = my_font.render("B", True, blue2)
    my_font_q = pygame.font.SysFont("H", 25, False, False)
    h_text = my_font_q.render("H", True, purple)

    # black box columns hole and character
    rect = pygame.Rect(501, 410, 8, 30)
    rect2 = pygame.Rect(200, 200, 90, 296)
    rect3 = pygame.Rect(205, 276, 80, 3)
    rect4 = pygame.Rect(205, 347, 80, 3)
    rect5 = pygame.Rect(205, 418, 80, 3)
    rect6 = pygame.Rect(300, 215, 3, 125)
    rect7 = pygame.Rect(300, 360, 3, 125)
    hole = pygame.Rect(585, 440, 50, 50)
    columns1 = pygame.Rect(460, 618, 50, 100)
    columns2 = pygame.Rect(710, 618, 50, 100)

    # variables for big circles font and rewards
    cr = 0
    crr = 0
    c1 = True
    c = 0
    x = 485
    y = 598
    gr = 0
    grr = 0
    g1 = True
    g = 0
    xx = 735
    yy = 598

    # variables for big circles and font in Quantum room

    Q_cr = 0
    Q_crr = 0
    Q_c1 = True
    Q_c = 0
    Q_x = 570
    Q_y = 370
    Q_gr = 0
    Q_grr = 0
    Q_g1 = True
    Q_g = 0
    Q_xx = 670
    Q_yy = 370

    # variables for character and wall
    u = 410
    wall = True

    # Variables for moving rewards
    z = True
    red_x = 330
    red_y = 278
    blue_x = 330
    blue_y = 278
    red_x_1 = 330
    red_y_1 = 418
    blue_x_1 = 330
    blue_y_1 = 418

    # Variables for moving big Quantum rewards and Qbit
    j = True
    red_xxx = 60
    red_yyy = 700
    blue_xxx = 60
    blue_yyy = 700
    red_xxx_1 = 452
    red_yyy_1 = 370
    blue_xxx_1 = 452
    blue_yyy_1 = 370
    red_blue = True
    red_blue_random = 0
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
        # character move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and rect.x < 790:
            rect.x += 2
        if keys[pygame.K_LEFT] and rect.x > 400:
            rect.x -= 2
        if keys[pygame.K_UP] and rect.y > u:
            rect.y -= 2
        if keys[pygame.K_DOWN] and rect.y < 550:
            rect.y += 2

        # blue big circle move
        if keys[pygame.K_l] and 475 < rect.x < 490 and 545 < rect.y < 550:
            c += 1
        if c > 1:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and x < 800:
                x += 2
            if keys[pygame.K_LEFT] and x > 400:
                x -= 2
            if keys[pygame.K_UP] and y > 460:
                y -= 2
            if keys[pygame.K_DOWN] and y < 600:
                y += 2

        # red big circle move
        if keys[pygame.K_l] and 725 < rect.x < 740 and 545 < rect.y < 550:
            g += 1
        if g > 1:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and xx < 800:
                xx += 2
            if keys[pygame.K_LEFT] and xx > 400:
                xx -= 2
            if keys[pygame.K_UP] and yy > 460:
                yy -= 2
            if keys[pygame.K_DOWN] and yy < 600:
                yy += 2

        dis.fill(blue)

        # if ball in the hole then get font Incomplete answer
        if c1:
            if 605 < x < 615 and 455 < y < 465 and g1:
                c1 = False
                cr = random.randint(1, 2)
            pygame.draw.circle(dis, blue2, (x, y), 20, 0)
        if not c1 and cr == 1 and g1:
            dis.blit(my_text_1, (150, 215))
            dis.blit(my_text_2, (150, 360))
        if not c1 and cr == 2 and g1:
            dis.blit(my_text_3, (150, 290))
            dis.blit(my_text_4, (150, 430))

        if g1:
            if 605 < xx < 615 and 455 < yy < 465 and c1:
                g1 = False
                gr = random.randint(1, 2)
            pygame.draw.circle(dis, red, (xx, yy), 20, 0)
        if not g1 and gr == 1 and c1:
            dis.blit(my_text_5, (150, 215))
            dis.blit(my_text_4, (150, 430))
        if not g1 and gr == 2 and c1:
            dis.blit(my_text_6, (150, 290))
            dis.blit(my_text_2, (150, 360))

        # reward by putting the second ball in the hole and get full font answer
        if not c1 and 605 < xx < 615 and 455 < yy < 465:
            g1 = False
            crr = random.randint(3, 4)
            x = 0
            y = 0
            xx = 0
            yy = 0
        if cr == 1 and crr == 3 and z:
            dis.blit(my_text_5, (150, 215))
            red_y -= 1
            blue_y -= 1
        if cr == 1 and crr == 4 and z:
            dis.blit(my_text_2, (150, 360))
            red_y_1 -= 1
            blue_y_1 -= 1
        if cr == 2 and crr == 3 and z:
            dis.blit(my_text_6, (150, 290))
            red_y -= 1
            blue_y -= 1
        if cr == 2 and crr == 4 and z:
            dis.blit(my_text_4, (150, 430))
            red_y_1 -= 1
            blue_y_1 -= 1

        if not g1 and 605 < x < 615 and 455 < y < 465:
            c1 = False
            grr = random.randint(3, 4)
            x = 0
            y = 0
            xx = 0
            yy = 0
        if gr == 1 and grr == 3 and z:
            dis.blit(my_text_1, (150, 215))
            red_y -= 1
            blue_y -= 1
        if gr == 1 and grr == 4 and z:
            dis.blit(my_text_4, (150, 430))
            red_y_1 -= 1
            blue_y_1 -= 1
        if gr == 2 and grr == 3 and z:
            dis.blit(my_text_3, (150, 290))
            red_y -= 1
            blue_y -= 1
        if gr == 2 and grr == 4 and z:
            dis.blit(my_text_2, (150, 360))
            red_y_1 -= 1
            blue_y_1 -= 1

        # A wall opens and a player can go through
        if red_y == 20 or red_y_1 == 20:
            wall = False
            u = 250
            z = False

        # rewards
        pygame.draw.circle(dis, red, (red_x, red_y), 14, 0, True, False, True, False)
        pygame.draw.circle(dis, blue2, (blue_x, blue_y), 14, 0, False, True, False, True)
        pygame.draw.circle(dis, red, (red_x_1, red_y_1), 14, 0, True, True, False, False)
        pygame.draw.circle(dis, blue2, (blue_x_1, blue_y_1), 14, 0, False, False, True, True)
        pygame.draw.circle(dis, gold, (330, 20), 18, 3, True, True, True, True)

        # character
        pygame.draw.rect(dis, black, rect)

        # hole
        pygame.draw.rect(dis, purple, hole, 7)

        # Floor walls and decorative columns
        pygame.draw.line(dis, green, (350, 720), (850, 720), 5)
        if wall:
            pygame.draw.line(dis, gold, (400, 405), (1000, 405), 5)
        pygame.draw.line(dis, gold, (391, 408), (391, 0), 15)
        pygame.draw.line(dis, green, (391, 408), (391, 720), 15)
        pygame.draw.rect(dis, gold, columns1)
        pygame.draw.rect(dis, gold, columns2)

        # arrows
        pygame.draw.line(dis, black, (217, 265), (270, 265), 3)
        pygame.draw.line(dis, black, (217, 218), (270, 218), 3)
        pygame.draw.line(dis, black, (217, 291), (270, 336), 3)
        pygame.draw.line(dis, black, (217, 336), (270, 291), 3)
        pygame.draw.line(dis, black, (217, 362), (270, 362), 3)
        pygame.draw.line(dis, black, (217, 407), (270, 362), 3)
        pygame.draw.line(dis, black, (217, 433), (270, 478), 3)
        pygame.draw.line(dis, black, (217, 478), (270, 478), 3)

        # frames and cursor
        pygame.draw.rect(dis, black, rect2, 5)
        pygame.draw.rect(dis, black, rect3)
        pygame.draw.rect(dis, black, rect4)
        pygame.draw.rect(dis, black, rect5)
        pygame.draw.rect(dis, purple, rect6)
        pygame.draw.rect(dis, purple, rect7)

        # small circle like dots
        pygame.draw.circle(dis, red, (217, 265), 5, 0)
        pygame.draw.circle(dis, red, (217, 336), 5, 0)
        pygame.draw.circle(dis, red, (217, 407), 5, 0)
        pygame.draw.circle(dis, red, (217, 478), 5, 0)
        pygame.draw.circle(dis, blue2, (217, 218), 5, 0)
        pygame.draw.circle(dis, blue2, (217, 291), 5, 0)
        pygame.draw.circle(dis, blue2, (217, 362), 5, 0)
        pygame.draw.circle(dis, blue2, (217, 433), 5, 0)
        pygame.draw.circle(dis, red, (270, 265), 5, 0)
        pygame.draw.circle(dis, red, (270, 336), 5, 0)
        pygame.draw.circle(dis, red, (270, 407), 5, 0)
        pygame.draw.circle(dis, red, (270, 478), 5, 0)
        pygame.draw.circle(dis, blue2, (270, 218), 5, 0)
        pygame.draw.circle(dis, blue2, (270, 291), 5, 0)
        pygame.draw.circle(dis, blue2, (270, 362), 5, 0)
        pygame.draw.circle(dis, blue2, (270, 433), 5, 0)

        # Least significant bit
        pygame.draw.circle(dis, black, (900, 100), 85, 2)
        pygame.draw.circle(dis, red, (900, 15), 10, 0)
        pygame.draw.circle(dis, gold, (900, 15), 12, 3)
        pygame.draw.circle(dis, red, (900, 185), 10, 0)
        pygame.draw.circle(dis, black, (900, 185), 12, 3)
        pygame.draw.circle(dis, blue2, (815, 100), 10, 0)
        pygame.draw.circle(dis, black, (815, 100), 12, 3)
        pygame.draw.circle(dis, blue2, (985, 100), 10, 0)
        pygame.draw.circle(dis, gold, (985, 100), 12, 3)
        pygame.draw.circle(dis, red, (960, 42), 10, 0, True, True, False, False)
        pygame.draw.circle(dis, blue2, (960, 42), 10, 0, False, False, True, True)
        pygame.draw.circle(dis, gold, (960, 42), 12, 3)
        pygame.draw.circle(dis, red, (840, 158), 10, 0, True, True, False, False)
        pygame.draw.circle(dis, blue2, (840, 158), 10, 0, False, False, True, True)
        pygame.draw.circle(dis, black, (840, 158), 12, 3)
        pygame.draw.circle(dis, red, (840, 42), 11, 0, True, False, True, False)
        pygame.draw.circle(dis, blue2, (840, 42), 11, 0, False, True, False, True)
        pygame.draw.circle(dis, red, (960, 158), 11, 0, False, True, False, True)
        pygame.draw.circle(dis, blue2, (960, 158), 11, 0, True, False, True, False)

        # Most significant bit
        pygame.draw.circle(dis, black, (900, 300), 85, 2)
        pygame.draw.circle(dis, red, (900, 215), 10, 0)
        pygame.draw.circle(dis, gold, (900, 215), 12, 3)
        pygame.draw.circle(dis, red, (900, 385), 10, 0)
        pygame.draw.circle(dis, black, (900, 385), 12, 3)
        pygame.draw.circle(dis, blue2, (815, 300), 10, 0)
        pygame.draw.circle(dis, black, (815, 300), 12, 3)
        pygame.draw.circle(dis, blue2, (985, 300), 10, 0)
        pygame.draw.circle(dis, gold, (985, 300), 12, 3)
        pygame.draw.circle(dis, red, (960, 242), 10, 0, True, True, False, False)
        pygame.draw.circle(dis, blue2, (960, 242), 10, 0, False, False, True, True)
        pygame.draw.circle(dis, gold, (960, 242), 12, 3)
        pygame.draw.circle(dis, red, (840, 358), 10, 0, True, True, False, False)
        pygame.draw.circle(dis, blue2, (840, 358), 10, 0, False, False, True, True)
        pygame.draw.circle(dis, black, (840, 358), 12, 3)
        pygame.draw.circle(dis, red, (840, 242), 11, 0, True, False, True, False)
        pygame.draw.circle(dis, blue2, (840, 242), 11, 0, False, True, False, True)
        pygame.draw.circle(dis, red, (960, 358), 11, 0, False, True, False, True)
        pygame.draw.circle(dis, blue2, (960, 358), 11, 0, True, False, True, False)

        # new gate
        pygame.draw.line(dis, black, (450, 172), (730, 172), 2)
        pygame.draw.circle(dis, blue2, (450, 172), 7, 0)
        pygame.draw.circle(dis, red, (730, 172), 7, 0)
        pygame.draw.line(dis, black, (450, 122), (730, 122), 2)
        pygame.draw.circle(dis, blue2, (450, 122), 7, 0)
        pygame.draw.circle(dis, blue2, (730, 122), 7, 0)
        pygame.draw.line(dis, black, (450, 72), (730, 72), 2)
        pygame.draw.circle(dis, blue2, (450, 72), 7, 0)
        pygame.draw.circle(dis, black, (730, 72), 7, 0)
        pygame.draw.circle(dis, gold, (730, 72), 4, 0)
        pygame.draw.line(dis, black, (450, 22), (730, 22), 2)
        pygame.draw.circle(dis, blue2, (450, 22), 7, 0)
        pygame.draw.circle(dis, black, (730, 22), 7, 0)
        pygame.draw.circle(dis, gold, (730, 22), 4, 0)
        pygame.draw.line(dis, purple, (425, 120), (425, 173), 5)
        pygame.draw.line(dis, purple, (425, 20), (425, 73), 5)
        pygame.draw.line(dis, black, (475, 300), (730, 300), 2)
        pygame.draw.circle(dis, black, (730, 300), 7, 0)
        pygame.draw.circle(dis, gold, (730, 300), 4, 0)
        pygame.draw.circle(dis, black, (452, 300), 25, 4)
        pygame.draw.line(dis, black, (520, 62), (520, 300), 2)
        pygame.draw.circle(dis, black, (521, 72), 10, 2)
        pygame.draw.line(dis, black, (590, 12), (590, 300), 2)
        pygame.draw.circle(dis, black, (591, 22), 10, 2)
        pygame.draw.line(dis, black, (655, 65), (666, 79), 2)
        pygame.draw.line(dis, black, (655, 79), (666, 65), 2)
        pygame.draw.circle(dis, black, (661, 72), 10, 2)
        pygame.draw.line(dis, black, (655, 165), (666, 179), 2)
        pygame.draw.line(dis, black, (655, 179), (666, 165), 2)
        pygame.draw.circle(dis, black, (661, 172), 10, 2)

        # blue big circle move in Quantum room
        if keys[pygame.K_l] and 560 < rect.x < 580 and 315 < rect.y < 322:
            Q_c += 1
        if Q_c > 1:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and Q_x < 800:
                Q_x += 2
            if keys[pygame.K_LEFT] and Q_x > 400:
                Q_x -= 2
            if keys[pygame.K_UP] and Q_y > 300:
                Q_y -= 2
            if keys[pygame.K_DOWN] and Q_y < 600:
                Q_y += 2

        # red big circle move in Quantum room
        if keys[pygame.K_l] and 660 < rect.x < 680 and 315 < rect.y < 322:
            Q_g += 1
        if Q_g > 1:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and Q_xx < 800:
                Q_xx += 2
            if keys[pygame.K_LEFT] and Q_xx > 400:
                Q_xx -= 2
            if keys[pygame.K_UP] and Q_yy > 300:
                Q_yy -= 2
            if keys[pygame.K_DOWN] and Q_yy < 600:
                Q_yy += 2

        # if ball in the hole then get font Incomplete answer Quantum room
        if Q_c1:
            if 445 < Q_x < 460 and 295 < Q_y < 305 and Q_g1:
                Q_c1 = False
                Q_cr = random.randint(5, 6)
            pygame.draw.circle(dis, blue2, (Q_x, Q_y), 20, 0)
        if not Q_c1 and Q_cr == 5 and Q_g1:
            dis.blit(my_text_1, (750, 2))
            dis.blit(my_text_2, (750, 102))
        if not Q_c1 and Q_cr == 6 and Q_g1:
            dis.blit(my_text_3, (750, 52))
            dis.blit(my_text_4, (750, 152))

        if Q_g1:
            if 445 < Q_xx < 460 and 295 < Q_yy < 305 and Q_c1:
                Q_g1 = False
                Q_gr = random.randint(5, 6)
            pygame.draw.circle(dis, red, (Q_xx, Q_yy), 20, 0)
        if not Q_g1 and Q_gr == 5 and Q_c1:
            dis.blit(my_text_5, (750, 2))
            dis.blit(my_text_4, (750, 152))
        if not Q_g1 and Q_gr == 6 and Q_c1:
            dis.blit(my_text_6, (750, 52))
            dis.blit(my_text_2, (750, 102))

        # second ball in the hole and get full font answer Quantum room and Quantum circle reward move
        if not Q_c1 and 445 < Q_xx < 460 and 295 < Q_yy < 305:
            Q_g1 = False
            Q_crr = random.randint(7, 8)
            Q_x = 0
            Q_y = 0
            Q_xx = 0
            Q_yy = 0
        if Q_cr == 5 and Q_crr == 7 and j:
            dis.blit(my_text_5, (750, 2))
            red_yyy -= 2
            blue_yyy -= 2
        if Q_cr == 5 and Q_crr == 8 and j:
            dis.blit(my_text_2, (750, 102))
            red_yyy -= 2
            blue_yyy -= 2
        if Q_cr == 6 and Q_crr == 7 and j:
            dis.blit(my_text_6, (750, 52))
            red_yyy -= 2
            blue_yyy -= 2
        if Q_cr == 6 and Q_crr == 8 and j:
            dis.blit(my_text_4, (750, 152))
            red_yyy -= 2
            blue_yyy -= 2

        if not Q_g1 and 445 < Q_x < 460 and 295 < Q_y < 305:
            Q_c1 = False
            Q_grr = random.randint(7, 8)
            Q_x = 0
            Q_y = 0
            Q_xx = 0
            Q_yy = 0
        if Q_gr == 5 and Q_grr == 7 and j:
            dis.blit(my_text_1, (750, 2))
            red_yyy -= 2
            blue_yyy -= 2
        if Q_gr == 5 and Q_grr == 8 and j:
            dis.blit(my_text_4, (750, 152))
            red_yyy -= 2
            blue_yyy -= 2
        if Q_gr == 6 and Q_grr == 7 and j:
            dis.blit(my_text_3, (750, 52))
            red_yyy -= 2
            blue_yyy -= 2
        if Q_gr == 6 and Q_grr == 8 and j:
            dis.blit(my_text_2, (750, 102))
            red_yyy -= 2
            blue_yyy -= 2

        # big last Quantum circle
        if red_yyy == 30 and blue_yyy == 30:
            j = False
            pygame.draw.circle(dis, red, (red_xxx_1, red_yyy_1), 20, 0, False, True, False, True)
            pygame.draw.circle(dis, blue2, (blue_xxx_1, blue_yyy_1), 20, 0, True, False, True, False)
            pygame.draw.circle(dis, red, (450, 172), 8, 0, False, True, False, True)
            pygame.draw.circle(dis, blue2, (450, 172), 8, 0, True, False, True, False)
            pygame.draw.circle(dis, black, (730, 172), 7, 3)
            pygame.draw.circle(dis, red, (730, 172), 5, 0)
            pygame.draw.circle(dis, red, (450, 122), 8, 0, False, True, False, True)
            pygame.draw.circle(dis, blue2, (450, 122), 8, 0, True, False, True, False)
            pygame.draw.circle(dis, gold, (730, 122), 7, 3)
            pygame.draw.circle(dis, red, (730, 122), 5, 0)
            pygame.draw.circle(dis, red, (450, 72), 8, 0, False, True, False, True)
            pygame.draw.circle(dis, blue2, (450, 72), 8, 0, True, False, True, False)
            pygame.draw.circle(dis, black, (730, 72), 7, 3)
            pygame.draw.circle(dis, red, (730, 72), 5, 0)
            pygame.draw.circle(dis, red, (450, 22), 8, 0, False, True, False, True)
            pygame.draw.circle(dis, blue2, (450, 22), 8, 0, True, False, True, False)
            pygame.draw.circle(dis, gold, (730, 22), 7, 3)
            pygame.draw.circle(dis, red, (730, 22), 5, 0)
            dis.blit(h_text, (700, 300))
            dis.blit(h_text, (700, 172))
            dis.blit(h_text, (700, 122))
            dis.blit(h_text, (700, 72))
            dis.blit(h_text, (700, 22))
            pygame.draw.line(dis, green, (590, 200), (590, 280), 2)
            pygame.draw.circle(dis, green, (591, 280), 5, 0)
            pygame.draw.line(dis, green, (520, 200), (520, 280), 2)
            pygame.draw.circle(dis, green, (521, 280), 5, 0)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and red_blue:
                red_yyy_1 -= 2
                blue_yyy_1 -= 2
            if red_yyy_1 == 300 and blue_yyy_1 == 300 and red_blue:
                red_blue_random = random.randint(9, 12)
                red_blue = False
            if red_blue_random == 9 and not red_blue:
                pygame.draw.line(dis, green, (960, 254), (960, 346), 3)
                pygame.draw.line(dis, purple, (960, 254), (978, 290), 3)
                pygame.draw.line(dis, purple, (902, 25), (954, 146), 3)
                pygame.draw.circle(dis, blue2, (900, 300), 18, 0)
                pygame.draw.circle(dis, red, (900, 100), 18, 0)
                pygame.draw.circle(dis, blue2, (730, 300), 4, 0)
                pygame.draw.circle(dis, blue2, (753, 300), 7, 0)
                pygame.draw.circle(dis, red, (753, 22), 7, 0)
                pygame.draw.circle(dis, blue2, (412, 60), 7, 0)
                pygame.draw.circle(dis, red, (412, 32), 7, 0)
                pygame.draw.line(dis, green, (782, 300), (882, 300), 3)
                pygame.draw.line(dis, purple, (790, 342), (881, 304), 3)
                pygame.draw.line(dis, purple, (790, 142), (881, 104), 3)
            if red_blue_random == 10 and not red_blue:
                pygame.draw.line(dis, green, (960, 254), (960, 346), 3)
                pygame.draw.line(dis, purple, (960, 254), (978, 290), 3)
                pygame.draw.line(dis, black, (845, 50), (952, 147), 3)
                pygame.draw.line(dis, black, (812, 186), (886, 114), 3)
                pygame.draw.line(dis, purple, (843, 50), (897, 176), 3)
                pygame.draw.circle(dis, blue2, (900, 300), 18, 0)
                pygame.draw.circle(dis, red, (900, 100), 18, 0)
                pygame.draw.circle(dis, blue2, (730, 300), 4, 0)
                pygame.draw.circle(dis, blue2, (753, 300), 7, 0)
                pygame.draw.circle(dis, red, (753, 72), 7, 0)
                pygame.draw.circle(dis, blue2, (412, 60), 7, 0)
                pygame.draw.circle(dis, red, (412, 32), 7, 0)
                pygame.draw.line(dis, green, (782, 300), (882, 300), 3)
                pygame.draw.line(dis, purple, (790, 342), (881, 304), 3)
                pygame.draw.line(dis, purple, (790, 142), (881, 107), 3)
            if red_blue_random == 11 and not red_blue:
                pygame.draw.line(dis, purple, (902, 225), (954, 346), 3)
                pygame.draw.line(dis, purple, (790, 342), (881, 304), 3)
                pygame.draw.line(dis, purple, (902, 25), (954, 146), 3)
                pygame.draw.line(dis, purple, (790, 142), (881, 104), 3)
                pygame.draw.circle(dis, red, (900, 300), 18, 0)
                pygame.draw.circle(dis, red, (900, 100), 18, 0)
                pygame.draw.circle(dis, red, (730, 300), 4, 0)
                pygame.draw.circle(dis, red, (753, 300), 7, 0)
                pygame.draw.circle(dis, red, (753, 122), 7, 0)
                pygame.draw.circle(dis, red, (412, 160), 7, 0)
                pygame.draw.circle(dis, red, (412, 132), 7, 0)
            if red_blue_random == 12 and not red_blue:
                pygame.draw.line(dis, purple, (902, 225), (954, 346), 3)
                pygame.draw.line(dis, purple, (790, 342), (881, 304), 3)
                pygame.draw.circle(dis, red, (900, 300), 18, 0)
                pygame.draw.circle(dis, red, (900, 100), 18, 0)
                pygame.draw.circle(dis, red, (730, 300), 4, 0)
                pygame.draw.circle(dis, red, (753, 300), 7, 0)
                pygame.draw.circle(dis, red, (753, 172), 7, 0)
                pygame.draw.circle(dis, red, (412, 160), 7, 0)
                pygame.draw.circle(dis, red, (412, 132), 7, 0)
                pygame.draw.line(dis, black, (845, 50), (952, 147), 3)
                pygame.draw.line(dis, black, (812, 186), (886, 114), 3)
                pygame.draw.line(dis, purple, (843, 50), (897, 176), 3)
                pygame.draw.line(dis, purple, (790, 142), (881, 107), 3)
            if keys[pygame.K_r]:
                red_blue = True
                red_yyy_1 = 370
                blue_yyy_1 = 370

        # big last Quantum circle reward
        pygame.draw.circle(dis, red, (red_xxx, red_yyy), 30, 0, False, True, False, True)
        pygame.draw.circle(dis, blue2, (blue_xxx, blue_yyy), 30, 0, True, False, True, False)
        pygame.draw.circle(dis, gold, (60, 30), 30, 3)

        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())



