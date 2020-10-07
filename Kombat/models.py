from django.db import models

# Create your models here.

class KanoBasicAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.PositiveIntegerField()
    Recovery = models.PositiveIntegerField()
    HitAdv = models.PositiveIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

#Kano Basic Attacks

#Kano Kombo Attacks
class KanoStringAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.PositiveIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

#Kano Special Moves

class KanoSpecialAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class KanoRipperAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.PositiveIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class KanoDirtbagAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move


class NightwolfBasicAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class NightwolfStringAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class NightwolfSpecialAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class NightwolfMatokaAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class NightwolfAncestralAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move
class JadeBasicAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class JadeStringAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()
    
    def __str__(self):
        return self.Move

class JadeSpecialAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class JadeEmeraldAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class JadeJadedAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class SubZeroBasicAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class SubZeroStringAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class SubZeroSpecialAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class SubZeroDeadofWinterAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move

class SubZeroThinIceAttack(models.Model):
    Move = models.CharField(max_length=50)
    MoveType = models.CharField(max_length=50,default="None")
    Buttons = models.CharField(max_length=50,default="N/A")
    Startup = models.PositiveIntegerField()
    Active = models.SmallIntegerField()
    Recovery = models.SmallIntegerField()
    HitAdv = models.SmallIntegerField()
    BlockAdv = models.SmallIntegerField()
    FBlockAdv = models.SmallIntegerField()

    def __str__(self):
        return self.Move





#Each databasae includes:
    #Startup
    #Active
    #Recovery
    #Hit Advantage
    #Block Advantage

#python mange.py makemigrations
#python mange.py migrate