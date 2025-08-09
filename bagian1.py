import pygame
pygame.init()

""" variabel global """
lebar_scene = 500
tinggi_scene = 500
judul_scene = "PING PONG MODERN"
gambar_latar = "latar1.jpg"
gambar_pemain1 = "TANK.png"
GAME_ON = True # artinya game sedang on
GAME_OVER = False # artinya game sedang berjalan

""" scene """
SCENE = pygame.display.set_mode((lebar_scene, tinggi_scene))
pygame.display.set_caption(judul_scene)
LATAR = pygame.transform.scale(pygame.image.load(gambar_latar),
    (lebar_scene, tinggi_scene))

""" musik """

""" kelas """
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, gambar, x, y, lebar, tinggi, kecepatan):
        super().__init__()
        self.lebar = lebar
        self.tinggi = tinggi
        self.kecepatan = kecepatan
        self.image = pygame.transform.scale(pygame.image.load(gambar),
            (self.lebar, self.tinggi))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def tampil(self):
        SCENE.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def gerak_kiri(self):
        TOMBOL = pygame.key.get_pressed()
        if TOMBOL[pygame.K_w] and self.rect.y > 0: # atas
            self.rect.y -= self.kecepatan
        if TOMBOL[pygame.K_s] and self.rect.y < tinggi_scene-self.tinggi: # bawah
            self.rect.y += self.kecepatan
    def gerak_kanan(self):
        TOMBOL = pygame.key.get_pressed()
        if TOMBOL[pygame.K_UP] and self.rect.y > 0: # atas
            self.rect.y -= self.kecepatan
        if TOMBOL[pygame.K_DOWN] and self.rect.y < tinggi_scene-self.tinggi: # bawah
            self.rect.y += self.kecepatan
        
""" objek sprite """
PEMAIN1 = Player(gambar_pemain1, 50, 100, 50, 100, 20)
PEMAIN2 = Player(gambar_pemain1, 400, 100, 50, 100, 20)

""" game loop """
FPS = pygame.time.Clock()
while GAME_ON:
    """ event handler untuk QUIT """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_ON = False # artinya gamenya OFF

    """ bagian tampilan dan gerakkan """
    if GAME_OVER == False:
        SCENE.blit(LATAR, (0,0))

        PEMAIN1.tampil()
        PEMAIN2.tampil()
        PEMAIN1.gerak_kiri()
        PEMAIN2.gerak_kanan()

    """ bagian penting """
    FPS.tick(60)
    pygame.display.update()







