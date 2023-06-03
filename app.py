def main():
    import pygame,sys,time,tkinter
    from tkinter import messagebox as m
    pygame.init()
    data={1:(175,16),2:(171, 511),3:(415, 266),4:(657, 21),5:(657, 515)}
    window=pygame.display.set_mode((704,552))
    pygame.display.set_caption('憋死牛')
    num=0
    num2=0
    class mouse(pygame.sprite.Sprite):
        def __init__(self):
            self.image=pygame.Surface((1,1))
            self.rect=self.image.get_rect()
            self.rect.center=pygame.mouse.get_pos()
        def update(self):
            self.rect.center=pygame.mouse.get_pos()
            window.blit(self.image,self.rect)
    class computer(pygame.sprite.Sprite):
        def __init__(self,pos):
            self.image=pygame.Surface((40,40))
            self.image.fill('red')
            self.rect=self.image.get_rect()
            self.rect.center=data[pos]
            self.t=pos
        def update(self):
            window.blit(self.image,self.rect)
        def work(self,pos):
            self.rect.center=data[pos]
            self.t=pos
    class user(pygame.sprite.Sprite):
        def __init__(self,pos):
            self.image=pygame.Surface((40,40))
            self.image.fill('blue')
            self.rect=self.image.get_rect()
            self.rect.center=data[pos]
            self.t=pos
        def update(self):
            window.blit(self.image,self.rect)
        def work(self,num,pos):
            if (not num) and (self.t==1):
                pass
            elif (pos in [1,2]) and (self.t in [1,2]):
                return 0
            elif ((pos==1) and (self.t==5)) or ((pos==4) and (self.t==2)) or ((pos==2) and (self.t==4)) or ((pos==5) and (self.t==1)):
                return 0
            self.rect.center=data[pos]
            self.t=pos
            return 1
    a1=user(1)
    a2=user(2)
    c1=computer(4)
    c2=computer(5)
    mouse1=mouse()
    ls=[1,2,3,4,5]
    n=1
    while 1:
        ls.remove(c1.t)
        ls.remove(c2.t)
        ls.remove(a1.t)
        ls.remove(a2.t)
        ok=ls[0]
        if not n:
            if a1.t==3:
                c1.work(ok)
            elif a2.t==3:
                c2.work(ok)
            elif ((a1.t in [2,5]) and (a2.t in [2,5])) or ((a1.t in [1,4]) and (a2.t in [1,4])):
                if c1.t==3 or c2.t==3:
                    c2.work(ok)
                    pygame.display.set_caption('电脑胜')
                    break
                else:
                    c1.work(ok)
            elif ((ok in [2,5]) and (c2.t in [2,5])) or ((ok in [1,4]) and (c2.t in [1,4])):
                c2.work(ok)
            else:
                c1.work(ok)
            num2=1
            n=1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_mask(mouse1,a1) and n:
                t3=a1.work(num,ok)
                if t3:
                    num=1
                    n=0
            elif event.type==pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_mask(mouse1,a2) and n:
                t3=a2.work(num,ok)
                if t3:
                    num=1
                    n=0
        rootimage=pygame.image.load(r'.\data\desktop.png')
        window.blit(rootimage,(0,0))
        mouse1.update()
        c1.update()
        c2.update()
        a1.update()
        a2.update()
        pygame.display.update()
        ls=[1,2,3,4,5]
    w=tkinter.Tk()
    w.withdraw()
    m.showinfo('电脑胜','电脑胜')
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
