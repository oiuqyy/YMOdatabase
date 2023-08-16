#RealWorldEngineV1.0byoiuqyy
#TODO:
#精细化更新（物体移动更精细）；
#力学更新（使用F=ma）；
#场学更新（支持各种场）；
#控制台更新（更方便的指令）；
#单位制更新（一切单位落实）；
#显示更新（优化界面）
import turtle, time

TextDisplay = True
ObjCounter = 0
obl=[]  #ObjectList，物体列表

def ListAdd(l1, l2):    #[1, 4, 2]+[2, 3, 4]=[3, 7, 6]
    if len(l1) != len(l2):
        print('Error!Invalid input!')
    else:
        try:
            l3=[]
            for i in range(len(l1)):
                l3.append(l1[i]+l2[i])
        except:
            print('Error!Invalid input!')
        return l3

class obj:  #物体类
    id=-1
    name=''
    v=[]
    pos=[]
    a=[]
    shape=''
    lf=[]
    def __init__(self, id, name='unnamed', v=[0,0], pos=[0,0], a=[0,0], shape='rect'):
        self.id=id
        self.name=name
        self.v=v
        self.pos=pos
        self.a=a
        self.shape=shape
        self.ttl=turtle.Turtle()
        self.ttl.setpos(self.pos)
        if TextDisplay==True:
            print('An object with name:{}, id:{}, v:{}, pos:{}, a:{}, shape:{} ahas been successfully generated!'.format(name, id, v, pos, a, shape))
    def info(self):
        print("Object named '{}' has id:{}, v:{}, pos:{}, a:{}, shape:{}.".format(self.name, self.id, self.v, self.pos, self.a, self.shape))
    def addv(self, dv):
        self.v=ListAdd(self.v, dv)
        if TextDisplay==True:
            print('Now object {} has v:{}.'.format(self.name, self.v))
    def setv(self, v):
        self.v=v
        if TextDisplay==True:
            print('Now object {} has v:{}.'.format(self.name, self.v))
    def addpos(self, dpos):
        self.pos=ListAdd(self.pos, dpos)
        if TextDisplay==True:
            print('Now object {} has pos:{}.'.format(self.name, self.pos))
    def setpos(self, pos):
        self.pos=pos
        if TextDisplay==True:
            print('Now object {} has pos:{}.'.format(self.name, self.pos))
    def adda(self, da):
        self.a=ListAdd(self.a, da)
        if TextDisplay==True:
            print('Now object {} has a:{}.'.format(self.name, self.a))
    def seta(self, a):
        self.a=a
        if TextDisplay==True:
            print('Now object {} has a:{}.'.format(self.name, self.a))
    def Update(self, times=1):  #更新物体状态
        for i in range(times):
            self.addv(self.a)
            self.addpos(self.v)
            self.ttl.setpos(self.pos)
            if self.pos[0] >= turtle.screensize()[0]/2:
                self.v[0]=-abs(self.v[0])
                if TextDisplay==True:
                    print('{} hit the wall.'.format(self.name))
            if self.pos[0] <= -turtle.screensize()[0]/2:
                self.v[0]=abs(self.v[0])
                if TextDisplay==True:
                    print('{} hit the wall.'.format(self.name))
            if self.pos[1] >= turtle.screensize()[1]/2:
                self.v[1]=-abs(self.v[1])
                if TextDisplay==True:
                    print('{} hit the wall.'.format(self.name))
            if self.pos[1] <= -turtle.screensize()[1]/2:
                self.v[1]=abs(self.v[1])
                if TextDisplay==True:
                    print('{} hit the wall.'.format(self.name))
def Generate(id=-1, name='unnamed', v=[0,0], pos=[0,0], a=[0,0], shape='rect'): #生成物体
    global ObjCounter
    ObjCounter += 1
    obl.append(obj(id=ObjCounter, name=name, v=v, pos=pos, a=a, shape=shape))
def UpdateAll(times=1):#全局更新
    for j in range(times):
        for i in obl:
            i.Update()
def drawedge():
    x, y=turtle.screensize()
    x+=20
    y+=20
    Tool=turtle.Turtle()
    Tool.ht()
    Tool.speed(0)
    Tool.penup()
    Tool.setpos(x/2, y/2)
    Tool.pendown()
    Tool.setpos(-x/2, y/2)
    Tool.setpos(-x/2, -y/2)
    Tool.setpos(x/2, -y/2)
    Tool.setpos(x/2, y/2)

TextDisplay = False
turtle.screensize(400, 300)
drawedge()
Generate(name='S1', v=[13, 15], a=[1, -2])
Generate(name='S2', v=[30, 43], a=[0, -4])
UpdateAll(1000)
