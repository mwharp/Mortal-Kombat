from django.shortcuts import render
from django.http import HttpResponse
from .models import KanoBasicAttack
from .models import KanoStringAttack
from .models import KanoSpecialAttack
from .models import KanoRipperAttack
from .models import KanoDirtbagAttack
from .models import NightwolfBasicAttack
from .models import NightwolfStringAttack
from .models import NightwolfSpecialAttack
from .models import NightwolfMatokaAttack
from .models import NightwolfAncestralAttack
from .models import JadeBasicAttack
from .models import JadeStringAttack
from .models import JadeSpecialAttack
from .models import JadeEmeraldAttack
from .models import JadeJadedAttack
from .models import SubZeroBasicAttack
from .models import SubZeroStringAttack
from .models import SubZeroSpecialAttack
from .models import SubZeroDeadofWinterAttack
from .models import SubZeroThinIceAttack

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Max'})

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html') #the about page

def character(request):
    #return HttpResponse('character')
    return render(request, 'character.html')

def frames(request):
    #return HttpResponse('frames')
    return render(request,'frames.html')

def KanoHome(request):
    #return HttpResponse('Kano')
    KanoBasicFrames = KanoBasicAttack.objects.all()
    KanoStringFrames = KanoStringAttack.objects.all()
    KanoSpecialFrames = KanoSpecialAttack.objects.all()
    KanoRipperFrames = KanoRipperAttack.objects.all()
    KanoDirtbagFrames = KanoDirtbagAttack.objects.all()
    return render(request, 'KanoHome.html',
     {'KanoBasicFrames': KanoBasicFrames ,'KanoStringFrames': KanoStringFrames ,
      'KanoSpecialFrames': KanoSpecialFrames, 'KanoRipperFrames':KanoRipperFrames, 'KanoDirtbagFrames': KanoDirtbagFrames})

def NightwolfHome(request):
    #return HttpResponse('Nightwolf')
    NightwolfBasicFrames = NightwolfBasicAttack.objects.all()
    NightwolfStringFrames = NightwolfStringAttack.objects.all()
    NightwolfSpecialFrames = NightwolfSpecialAttack.objects.all()
    NightwolfMatokaFrames = NightwolfMatokaAttack.objects.all()
    NightwolfAncestralFrames = NightwolfAncestralAttack.objects.all()
    return render(request, 'NightwolfHome.html', {'NightwolfBasicFrames': NightwolfBasicFrames,'NightwolfStringFrames': NightwolfStringFrames
    ,'NightwolfSpecialFrames': NightwolfSpecialFrames,'NightwolfMatokaFrames': NightwolfMatokaFrames,'NightwolfAncestralFrames': NightwolfAncestralFrames})

def JadeHome(request):
    #return HttpResponse('Jade')
    JadeBasicFrames = JadeBasicAttack.objects.all()
    JadeStringFrames = JadeStringAttack.objects.all()
    JadeSpecialFrames = JadeSpecialAttack.objects.all()
    JadeEmeraldFrames = JadeEmeraldAttack.objects.all()
    JadeJadedFrames =JadeJadedAttack.objects.all()
    return render(request, 'JadeHome.html',{'JadeBasicFrames': JadeBasicFrames,'JadeStringFrames': JadeStringFrames,
    'JadeSpecialFrames':JadeSpecialFrames,'JadeEmeraldFrames':JadeEmeraldFrames,'JadeJadedFrames':JadeJadedFrames})

def SubZeroHome(request):
    #return HttpResponse('SubZero')
    SubZeroBasicFrames = SubZeroBasicAttack.objects.all()
    SubZeroStringFrames = SubZeroStringAttack.objects.all()
    SubZeroSpecialFrames = SubZeroSpecialAttack.objects.all()
    SubZeroDeadofWinterFrames = SubZeroDeadofWinterAttack.objects.all()
    SubZeroThinIceFrames = SubZeroThinIceAttack.objects.all()
    return render(request, 'SubZeroHome.html',{'SubZeroBasicFrames': SubZeroBasicFrames,'SubZeroStringFrames': SubZeroStringFrames,
    'SubZeroSpecialFrames':SubZeroSpecialFrames,'SubZeroDeadofWinterFrames':SubZeroDeadofWinterFrames,'SubZeroThinIceFrames':SubZeroThinIceFrames})
