import pygame
import random
import os
import time
from input import pygame_textinput

pygame.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Japanese Learning Game")

level_sound = pygame.mixer.Sound('background music/orchestra.wav')
indie_flower = "Indie_Flower/IndieFlower-Regular.ttf"

BG = pygame.transform.scale(pygame.image.load("Space Invader/background-black.png"),(WIDTH,HEIGHT))
BG = pygame.transform.scale(pygame.image.load("night.jpg"),(WIDTH,HEIGHT))
hiragana = [pygame.image.load('Hiragana/a.png'),pygame.image.load('Hiragana/i.png'),pygame.image.load('Hiragana/u.png'),pygame.image.load('Hiragana/e.png')
            ,pygame.image.load('Hiragana/o.png'),pygame.image.load('Hiragana/ka.png'),pygame.image.load('Hiragana/ki.png'),pygame.image.load('Hiragana/ku.png')
            ,pygame.image.load('Hiragana/ke.png'),pygame.image.load('Hiragana/ko.png'),pygame.image.load('Hiragana/sa.png'),pygame.image.load('Hiragana/shi.png')
            ,pygame.image.load('Hiragana/su.png'),pygame.image.load('Hiragana/se.png'),pygame.image.load('Hiragana/so.png'),pygame.image.load('Hiragana/ta.png')
            ,pygame.image.load('Hiragana/chi.png'),pygame.image.load('Hiragana/tsu.png'),pygame.image.load('Hiragana/te.png'),pygame.image.load('Hiragana/to.png')
            ,pygame.image.load('Hiragana/na.png'),pygame.image.load('Hiragana/ni.png'),pygame.image.load('Hiragana/nu.png'),pygame.image.load('Hiragana/ne.png')
            ,pygame.image.load('Hiragana/no.png'),pygame.image.load('Hiragana/ha.png'),pygame.image.load('Hiragana/hi.png'),pygame.image.load('Hiragana/hu.png')
            ,pygame.image.load('Hiragana/he.png'),pygame.image.load('Hiragana/ho.png'),pygame.image.load('Hiragana/ma.png'),pygame.image.load('Hiragana/mi.png')
            ,pygame.image.load('Hiragana/mu.png'),pygame.image.load('Hiragana/me.png'),pygame.image.load('Hiragana/mo.png'),pygame.image.load('Hiragana/ya.png')
            ,pygame.image.load('Hiragana/yu.png'),pygame.image.load('Hiragana/yo.png'),pygame.image.load('Hiragana/ra.png'),pygame.image.load('Hiragana/ri.png')
            ,pygame.image.load('Hiragana/ru.png'),pygame.image.load('Hiragana/re.png'),pygame.image.load('Hiragana/ro.png'),pygame.image.load('Hiragana/wa.png')
            ,pygame.image.load('Hiragana/wo.png'),pygame.image.load('Hiragana/nn.png')]

katakana= [pygame.image.load('katakana/a.png'),pygame.image.load('katakana/i.png'),pygame.image.load('katakana/u.png'),pygame.image.load('katakana/e.png')
            ,pygame.image.load('katakana/o.png'),pygame.image.load('katakana/ka.png'),pygame.image.load('katakana/ki.png'),pygame.image.load('katakana/ku.png')
            ,pygame.image.load('katakana/ke.png'),pygame.image.load('katakana/ko.png'),pygame.image.load('katakana/sa.png'),pygame.image.load('katakana/shi.png')
            ,pygame.image.load('katakana/su.png'),pygame.image.load('katakana/se.png'),pygame.image.load('katakana/so.png'),pygame.image.load('katakana/ta.png')
            ,pygame.image.load('katakana/chi.png'),pygame.image.load('katakana/tsu.png'),pygame.image.load('katakana/te.png'),pygame.image.load('katakana/to.png')
            ,pygame.image.load('katakana/na.png'),pygame.image.load('katakana/ni.png'),pygame.image.load('katakana/nu.png'),pygame.image.load('katakana/ne.png')
            ,pygame.image.load('katakana/no.png'),pygame.image.load('katakana/ha.png'),pygame.image.load('katakana/hi.png'),pygame.image.load('katakana/hu.png')
            ,pygame.image.load('katakana/he.png'),pygame.image.load('katakana/ho.png'),pygame.image.load('katakana/ma.png'),pygame.image.load('katakana/mi.png')
            ,pygame.image.load('katakana/mu.png'),pygame.image.load('katakana/me.png'),pygame.image.load('katakana/mo.png'),pygame.image.load('katakana/ya.png')
            ,pygame.image.load('katakana/yu.png'),pygame.image.load('katakana/yo.png'),pygame.image.load('katakana/ra.png'),pygame.image.load('katakana/ri.png')
            ,pygame.image.load('katakana/ru.png'),pygame.image.load('katakana/re.png'),pygame.image.load('katakana/ro.png'),pygame.image.load('katakana/wa.png')
            ,pygame.image.load('katakana/wo.png'),pygame.image.load('katakana/nn.png')]

hvoiced =  [pygame.image.load('HVoiced/ga.png'),pygame.image.load('HVoiced/gi.png'),pygame.image.load('HVoiced/gu.png'),pygame.image.load('HVoiced/ge.png'),
            pygame.image.load('HVoiced/go.png'),pygame.image.load('HVoiced/za.png'),pygame.image.load('HVoiced/ji.png'),pygame.image.load('HVoiced/zu.png'),
            pygame.image.load('HVoiced/ze.png'),pygame.image.load('HVoiced/zo.png'),pygame.image.load('HVoiced/da.png'),pygame.image.load('HVoiced/di.png'),
            pygame.image.load('HVoiced/du.png'),pygame.image.load('HVoiced/de.png'),pygame.image.load('HVoiced/do.png'),pygame.image.load('HVoiced/ba.png'),
            pygame.image.load('HVoiced/bi.png'),pygame.image.load('HVoiced/bu.png'),pygame.image.load('HVoiced/be.png'),pygame.image.load('HVoiced/bo.png'),
            pygame.image.load('HVoiced/pa.png'),pygame.image.load('HVoiced/pi.png'),pygame.image.load('HVoiced/pu.png'),pygame.image.load('HVoiced/pe.png'),
            pygame.image.load('HVoiced/po.png')]

kvoiced =  [pygame.image.load('KVoiced/ga.png'),pygame.image.load('KVoiced/gi.png'),pygame.image.load('KVoiced/gu.png'),pygame.image.load('KVoiced/ge.png'),
            pygame.image.load('KVoiced/go.png'),pygame.image.load('KVoiced/za.png'),pygame.image.load('KVoiced/ji.png'),pygame.image.load('KVoiced/zu.png'),
            pygame.image.load('KVoiced/ze.png'),pygame.image.load('KVoiced/zo.png'),pygame.image.load('KVoiced/da.png'),pygame.image.load('KVoiced/di.png'),
            pygame.image.load('KVoiced/du.png'),pygame.image.load('KVoiced/de.png'),pygame.image.load('KVoiced/do.png'),pygame.image.load('KVoiced/ba.png'),
            pygame.image.load('KVoiced/bi.png'),pygame.image.load('KVoiced/bu.png'),pygame.image.load('KVoiced/be.png'),pygame.image.load('KVoiced/bo.png'),
            pygame.image.load('KVoiced/pa.png'),pygame.image.load('KVoiced/pi.png'),pygame.image.load('KVoiced/pu.png'),pygame.image.load('KVoiced/pe.png'),
            pygame.image.load('KVoiced/po.png')]



romanji = ["a","i","u","e","o",'ka','ki','ku','ke','ko','sa','shi','su','se','so','ta','chi','tsu','te','to','na','ni',
          'nu','ne','no','ha','hi','hu','he','ho','ma','mi','mu','me','mo','ya','yu','yo','ra','ri','ru','re','ro','wa',
          'wo','nn']
romanji_voiced = ['ga','gi','gu','ge','go','za',['zi','ji'],'zu','ze','zo','da',['di','ji'],['du','zu'],'de','do',
                  'ba','bi','bu','be','bo','pa','pi','pu','pe','po']

music_list = ['<- EachAndAll ->','<- Summertime ->', '<- Windblow ->', '<- My Home Town ->']
music_list_index = 4

total_character = []
total_answer = []
total_number = 0

#icons
health = pygame.transform.scale(pygame.image.load("icons/health.png"), (40,40))
game_level = pygame.transform.scale(pygame.image.load("icons/game_level.png"),(50,30))
music_icon = pygame.transform.scale(pygame.image.load("icons/Music.png"), (40,40))
text_input_box = pygame.transform.scale(pygame.image.load("icons/textinput.png"), (300,60))
checkmark = pygame.transform.scale(pygame.image.load("icons/checkmark.png"), (35,35))

class Button:
    def __init__(self,color,x,y,width,height,text = '',textsize = 20,textcolor = (255,255,255),font = 'comicsans'):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.switch = False
        self.textsize = textsize
        self.textcolor = textcolor
        self.font = font

    def draw(self, window, outline = None):
        if outline:
            pygame.draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(window ,self.color, (self.x, self.y, self.width, self.height),0)

        if self.text != '':
            if self.font == 'comicsans':
                font = pygame.font.SysFont(self.font, self.textsize)
            elif self.font == indie_flower:
                font = pygame.font.Font(self.font,self.textsize)
                font.set_bold(True)
            text = font.render(self.text,1, self.textcolor)
            window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height/2 - text.get_height() / 2)))

    def isOver(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self. width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


class Enemy:
    def __init__(self, x, y, vel, index):
        self.x = x
        self.y = y
        self.vel = vel
        self.index = index
        self.img = pygame.transform.scale(total_character[index], (50, 50))

    def draw(self, window):
        window.blit(self.img, (self.x,self.y))

    def move(self, vel):
        self.y += vel

    def get_height(self):
        return self.img.get_height()


def main():
    global music_list_index
    global total_character
    global total_answer
    global total_number
    # music = pygame.mixer.music.load('background music/windblow.mp3')
    consecutive_wrong = 0

    run = True
    FPS = 60
    clock = pygame.time.Clock()
    enemies = []
    level = 0
    lives = 2
    enemies_vel = 0.5
    wave_length = 2
    switched_music = True

    main_font = pygame.font.SysFont("comicsans", 35)
    comic_font = pygame.font.Font(indie_flower, 25)
    comic_font.set_bold(True)
    comic_font_small = pygame.font.Font(indie_flower, 18)
    comic_font_small.set_bold(True)
    lost_font = pygame.font.SysFont("Ubuntu", 60)
    small_font = pygame.font.SysFont("comicsans", 20)
    test_font = pygame.font.SysFont("ヒラキノ角コシックw8ttc", 30)

    lowest_character_index = 0

    lost = False
    lost_count = 0

    removed = False

    textinput = pygame_textinput.TextInput(font_family= indie_flower, text_color = (0,0,0),cursor_color= (0,0,0),
                                           repeat_keys_initial_ms = -2,font_size= 20)

    asking_input = comic_font.render("Input Romanji:", 1, (0,0,0))


    pause_game = Button((0,219,255), WIDTH - 120, 20, 100, 30, 'Pause Game')
    pause_music = Button((16,165,245), WIDTH - 120, 60, 100, 30, "Pause Music")
    return_menu = Button((250, 218, 94), 5, HEIGHT - 30 , 100, 30, "Back to Menu", textcolor = (0,0,0))


    def music_pause(pause_music):
        if pause_music.switch == False:
            pygame.mixer.music.pause()
            pause_music.text = 'Resume music'
            pause_music.switch = True
        elif pause_music.switch == True:
            pygame.mixer.music.unpause()
            pause_music.text = 'Pause music'
            pause_music.switch = False

    def pause():
        paused = True
        paused_button = Button((255,191,0), WIDTH / 2 - 150, HEIGHT / 2, 300, 100, "Click or Press p to resume game",25 )
        while paused:
            pygame.mixer.music.pause()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if paused_button.isOver(pos):
                    paused_button.color = (255,103,0)
                if not paused_button.isOver(pos):
                    paused_button.color = (255,191,0)

                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if paused_button.isOver(pos):
                        paused = False



                paused_button.draw(WIN, (255, 83, 73))
                pygame.display.update()

        pygame.mixer.music.unpause()


    def rechoose_music():
        global music_list_index
        sub_index = music_list_index % 4
        if sub_index == 0:
            #pygame.mixer.music.fadeout(10)
            music = pygame.mixer.music.load('background music/EachAndAll.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)
        elif sub_index == 1:
            #pygame.mixer.music.fadeout(10)
            music = pygame.mixer.music.load('background music/summertime.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)
        elif sub_index == 2:
            #pygame.mixer.music.fadeout(10)
            music = pygame.mixer.music.load('background music/windblow.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)
        elif sub_index == 3:
            #pygame.mixer.music.fadeout(10)
            music = pygame.mixer.music.load('background music/myhometown.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)


    def redraw_window(events):
        global run
        answer = ""
        if lost:
            lost_label = lost_font.render("You Lost!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
            pygame.display.update()
            return ' '

        WIN.blit(BG,(0,0))
        pause_game.draw(WIN,(255,255,255))
        pause_music.draw(WIN, (255,255,255))
        return_menu.draw(WIN,(0,0,0))

        #sub_message = small_font.render(music_list[music_list_index % 4], 1, (255, 255, 255))
        #WIN.blit(sub_message, (0, 60))

        live_number = comic_font.render(f'{lives}',1, (0,0,0))
        level_number = comic_font.render(f'Level: {level}', 1, (255,255,255))
        current_music = comic_font_small.render(music_list[music_list_index % 4], 1, (0,0,0))

        for enemy in enemies:
            enemy.draw(WIN)

        if textinput.update(events):
            answer = textinput.get_text()
            textinput.clear_text()




        pygame.draw.rect(WIN, (250, 218, 94), (health.get_width() - 10, 15, 70, 20))
        WIN.blit(health,(5,5))
        WIN.blit(live_number, (57, 9))

        pygame.draw.rect(WIN, (52,107,49), (game_level.get_width() , 55, 100, 20))
        WIN.blit(game_level, (5, 50))
        WIN.blit(level_number, (50, 47))

        pygame.draw.rect(WIN, (252, 242, 216), (music_icon.get_width()- 15, 90, 200, 20))
        WIN.blit(music_icon, (5, 80))

        WIN.blit(current_music,(45, 88))

        WIN.blit(text_input_box,(WIDTH / 2 - 60, HEIGHT - 40))
        WIN.blit(textinput.get_surface(), (WIDTH / 2 - 30, HEIGHT - 25))
        WIN.blit(asking_input, (WIDTH / 2 - 220, HEIGHT - 30))

        pygame.display.update()

        return answer

    while run:
        is_correct = False

        clock.tick(FPS)

        events = pygame.event.get()
        #pause_game = Button((0, 219, 255), WIDTH - 120, 20, 100, 30, 'Pause Game')
        #pause_music = Button((16, 165, 245), WIDTH - 120, 60, 100, 30, "Pause Music")
        for event in events:
            pos = pygame.mouse.get_pos()
            if pause_game.isOver(pos):
                pause_game.color = (0, 0, 0)
            if pause_music.isOver(pos):
                pause_music.color = (0, 0, 0)
            if not pause_game.isOver(pos):
                pause_game.color = (0, 219, 255)
            if not pause_music.isOver(pos):
                pause_music.color = (16, 165, 245)

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    music_list_index -= 1
                    switched_music = True
                elif keys[pygame.K_RIGHT]:
                    music_list_index -= 1
                    switched_music = True
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if pause_game.isOver(pos):
                    pause()

                elif pause_music.isOver(pos):
                    #pause_music.color = (0,0,0)
                    music_pause(pause_music)

                elif return_menu.isOver(pos):
                    run = False
                    pygame.mixer.music.stop()
                    main_menu()




        answer = redraw_window(events)


        if switched_music and pause_music.switch == False:
            rechoose_music()
            switched_music = False

        '''
                for enemy in enemies:
            if answer == romanji[enemy.index] and enemy.get_height() > 20:
                enemies.remove(enemy)
                is_correct = True
                consecutive_wrong = 0
                break
        '''
        temp = None
        max_height = 0
        final_index = 0

        for enemy in enemies[:]:
            is_equal = False
            correct_answer = total_answer[enemy.index]
            if isinstance(correct_answer, list):
                a = correct_answer[0]
                b = correct_answer[1]
                if answer ==  a or answer == b:
                    is_equal = True
            elif answer == correct_answer:
                is_equal = True
            if is_equal == True and enemy.y > max_height and enemy.get_height() > 20:
                max_height = enemy.y
                temp = enemy

        for enemy in enemies:
            if temp == enemy:
                is_correct = True
                consecutive_wrong = 0
                enemies.remove(enemy)



        if is_correct == False and answer != "":
            consecutive_wrong += 1
        if consecutive_wrong >= 3:
            lives -= 1
            consecutive_wrong = 0

        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue


        if len(enemies) == 0:
            if level != 0 and lost == False:
                level_sound.play()
            level += 1
            lives += 1
            enemies_vel += 0.2
            wave_length += 3
            if level == 1 :
                top_range = -400
            elif level == 2:
                top_range = -1000
            else:
                top_range = - 1500
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(top_range,-100),
                              enemies_vel, random.randint(0,total_number - 1))
                enemies.append(enemy)

        for enemy in enemies[:]:
            enemy.move(enemies_vel)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)



def main_menu():

    global music_list_index
    global total_answer
    global total_character
    global total_number
    global start_text_change



    pygame.display.update()
    FPS = 60
    clock2 = pygame.time.Clock()
    run = True

    title_font = pygame.font.Font(indie_flower,40)

    sub_font = pygame.font.Font(indie_flower, 25)
    sub_font_2 = pygame.font.Font(indie_flower, 18)
    sub_font_2.set_bold(True)
    title_cloud = pygame.transform.scale(pygame.image.load("icons/title_cloud.png"), (500, 300))

    instruction_button = Button((0,219,255), WIDTH -   300, 250, 200, 40, 'In-game Instructions',textsize = 27)
    choice_button = Button((255,79,0), 50,250, 250, 40, 'Choose your combination!', textsize = 27)
    Hiragana_button = Button((7,47,95), 50 + choice_button.width / 2 - 80,320, 160, 40, 'Hiragana Voiceless', textsize = 18,font = indie_flower)
    Hiragana_button_voiced = Button((250, 218, 94), 50 + choice_button.width / 2 - 80, 390, 160, 40, 'Hiragana Voiced',
                             textsize=18,font = indie_flower, textcolor = (0,0,0))
    Katakana_voiceless = Button((52,107,49), 50 + choice_button.width / 2 - 80, 450, 160, 40, 'Katakana Voiceless',
                                    textsize=18,font = indie_flower)
    Katakana_voiced= Button((252, 242, 216), 50 + choice_button.width / 2 - 80, 520, 160, 40, 'Katakana Voiced',
                                textsize=18,font = indie_flower, textcolor = (0,0,0))




    while run:
        clock2.tick(FPS)
        WIN.blit(BG,(0,0))

        total_character = []
        total_answer = []
        total_number = 0

        music_instruction = sub_font.render("Press <- or ->  to switch songs", 1, (0, 0, 0))
        sub_message = sub_font.render(music_list[music_list_index % 4], 1, (11,181,255))
        gg = pygame.transform.scale(pygame.image.load("icons/cloud_2.png"), (music_instruction.get_width() + 100 , 300))


        WIN.blit(gg, (WIDTH - gg.get_width() , -80))
        WIN.blit(music_instruction, (WIDTH - 200 - music_instruction.get_width() / 2,   40))

        WIN.blit(sub_message, (WIDTH - 200 - sub_message.get_width() / 2, music_instruction.get_height() + 40))
        WIN.blit(title_cloud, (-50,-50))


        title_message_0 = title_font.render("Learn",1,(0,0,0))
        title_message = title_font.render("Japanese 50 Sounds",1, (0,0,0))
        WIN.blit(title_message_0, (120, 75 - title_message.get_height() + 20))
        WIN.blit(title_message, (10, 75 ))


        instruction_button.draw(WIN, (255,255,255))
        choice_button.draw(WIN, (0,0,0))
        Hiragana_button.draw(WIN, (0,0,0))
        Hiragana_button_voiced.draw(WIN, (0, 0, 0))
        Katakana_voiceless.draw(WIN, (0,0,0))
        Katakana_voiced.draw(WIN,(0,0,0))

        if Hiragana_button.switch:
            WIN.blit(checkmark, (270, 320))
        if Hiragana_button_voiced.switch:
            WIN.blit(checkmark, (270, 390))
        if Katakana_voiceless.switch:
            WIN.blit(checkmark, (270, 450))
        if Katakana_voiced.switch:
            WIN.blit(checkmark, (270, 520))



        Start_button = Button((255, 105, 180), WIDTH / 2 - 300, HEIGHT - 150, 600, 100, 'CHOOSE AT LEAST ONE TO START GAME!',
                              textsize=25, font=indie_flower, textcolor=(0, 0, 0))

        if (Hiragana_button.switch or Hiragana_button_voiced.switch or Katakana_voiceless.switch or Katakana_voiced.switch):
            Start_button.text = 'START GAME!'
        else:
            Start_button.text = 'CHOOSE AT LEAST ONE TO START GAME!'


        Start_button.draw(WIN, (0,0,0))

        pygame.draw.rect(WIN, (0,0,0), (WIDTH - 357, 308, 344, 264), 0)
        pygame.draw.rect(WIN, (255,227,227), (WIDTH - 355,310, 340, 260),0)


        text1 = sub_font_2.render("Type Romanji to interact with objects",1, (0,0,0))
        text2 = sub_font_2.render("Three consecutive mistakes = live - 1",1, (0,0,0))
        text3 = sub_font_2.render("Passing a level increases live by 1",1, (0,0,0))
        text4 = sub_font_2.render("Order of clearing doesn't matter",1, (0,0,0))

        WIN.blit(text1, (WIDTH - 345, 330))
        WIN.blit(text2, (WIDTH - 345, 390))
        WIN.blit(text3, (WIDTH - 345, 450))
        WIN.blit(text4, (WIDTH - 345, 510))


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if Start_button.isOver(pos):
                    if (Hiragana_button.switch or Hiragana_button_voiced.switch or Katakana_voiceless.switch or Katakana_voiced.switch):

                        Start_button.color = (255,255,255)
                        Start_button.draw(WIN,(0,0,0))
                        pygame.display.update()
                        if Hiragana_button.switch:
                            total_character += hiragana
                            total_answer += romanji
                            total_number += 46
                        if Hiragana_button_voiced.switch:
                            total_character += hvoiced
                            total_answer += romanji_voiced
                            total_number += 25
                        if Katakana_voiceless.switch:
                            total_character += katakana
                            total_answer += romanji
                            total_number += 46
                        if Katakana_voiced.switch:
                            total_character += kvoiced
                            total_answer += romanji_voiced
                            total_number += 25

                        main()
                        pygame.mixer.music.stop()
                elif Hiragana_button.isOver(pos):
                    if Hiragana_button.switch == False:
                        Hiragana_button.switch = True
                        WIN.blit(checkmark, (270, 320))
                        #pygame.display.update()
                    else:
                        Hiragana_button.switch = False
                        #pygame.display.update()
                elif Hiragana_button_voiced.isOver(pos):
                    if Hiragana_button_voiced.switch == False:
                        Hiragana_button_voiced.switch = True
                        WIN.blit(checkmark, (270, 390))
                        #pygame.display.update()
                    else:
                        Hiragana_button_voiced.switch = False
                        #pygame.display.update()
                elif Katakana_voiceless.isOver(pos):
                    if Katakana_voiceless.switch == False:
                        Katakana_voiceless.switch = True
                        WIN.blit(checkmark, (270, 450))
                        #pygame.display.update()
                    else:
                        Katakana_voiceless.switch = False
                        #pygame.display.update()
                elif Katakana_voiced.isOver(pos):
                    if Katakana_voiced.switch == False:
                        Katakana_voiced.switch = True
                        WIN.blit(checkmark, (270, 520))
                        #pygame.display.update()
                    else:
                        Katakana_voiced.switch = False
                        #pygame.display.update()


            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    music_list_index -= 1
                elif keys[pygame.K_RIGHT]:
                    music_list_index -= 1


    main_menu()




main_menu()