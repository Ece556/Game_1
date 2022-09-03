import pygame,random

#paketleri açma
pygame.init()
#pencere oluşumu
yukseklik,genislik = 600,750
pencere = pygame.display.set_mode((yukseklik,genislik))

#arkaplan şarkısı ve ses efectleri

pygame.mixer.music.load("oyun_arka_plan.wav")
pygame.mixer.music.play(-1,0,0)

seviye_yukseltme_sesi = pygame.mixer.Sound("level_up.wav")
yeme_sesi = pygame.mixer.Sound("jump.wav")

#FPS ayarlama
Hiz = 10
saat = pygame.time.Clock()
FPS = 30

#karakter ve yem eklemesi
canavar = pygame.image.load("2.png")
canavar_koordinat = canavar.get_rect()
canavar_koordinat.topleft = (yukseklik/2,genislik/2)

yem = pygame.image.load("cent1.png")
yem_koordinat = canavar.get_rect()
yem_koordinat.topleft = (150,150)

arka_plan = pygame.image.load("background.jpg")

#font ayarlama

font = pygame.font.SysFont("consolas", 64)

#değişenn değişken

y = 0

#Skor

Skor = 0
#oyun döngüsü

durum = True
while durum:
     for etkinlik in pygame.event.get():
         if etkinlik.type == pygame.QUIT:
             durum = False
     pencere.blit(arka_plan,(0,0))
     pencere.blit(canavar,canavar_koordinat)
     pencere.blit(yem, yem_koordinat)
     yazi = font.render("Skor: " +str(Skor), True,(255,0,0), (255,255,255))
     yazi_koordinat = yazi.get_rect()
     yazi_koordinat.topleft = (20,20)
     pygame.draw.line(pencere,(255,0,255),(0,90),(600,90),3)
     pencere.blit(yazi,yazi_koordinat)
     tus = pygame.key.get_pressed()
     if tus[pygame.K_LEFT] and canavar_koordinat.left>0:
         canavar_koordinat.x -= Hiz
     elif tus[pygame.K_RIGHT] and canavar_koordinat.right<yukseklik:
         canavar_koordinat.x += Hiz
     elif tus[pygame.K_UP] and canavar_koordinat.top>0:
         canavar_koordinat.y -= Hiz
     elif tus[pygame.K_DOWN] and canavar_koordinat.bottom < genislik:
         canavar_koordinat.y += Hiz
     if canavar_koordinat.colliderect(yem_koordinat):
         yeme_sesi.play()
         yem_koordinat.x = random.randint(0,yukseklik-32)
         yem_koordinat.y = random.randint(91, genislik-32)
         Skor +=1
     if Skor>10:
         canavar = pygame.image.load("1.png")
         if y ==0:
            seviye_yukseltme_sesi.play()
            canavar_koordinat = canavar.get_rect()
            canavar_koordinat.topleft = (195,195)
            y += 1
         tus = pygame.key.get_pressed()
         if tus[pygame.K_LEFT] and canavar_koordinat.left > 0:
             canavar_koordinat.x -= Hiz
         elif tus[pygame.K_RIGHT] and canavar_koordinat.right < yukseklik:
              canavar_koordinat.x += Hiz
         elif tus[pygame.K_UP] and canavar_koordinat.top > 0:
             canavar_koordinat.y -= Hiz
         elif tus[pygame.K_DOWN] and canavar_koordinat.bottom < genislik:
             canavar_koordinat.y += Hiz
         if canavar_koordinat.colliderect(yem_koordinat):
             yeme_sesi.play()
             yem_koordinat.x = random.randint(0, yukseklik - 32)
             yem_koordinat.y = random.randint(91, genislik - 32)
             Skor += 1

     pygame.display.update()
     saat.tick(FPS)








