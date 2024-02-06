

class PlayablePudge:
    width_cm: float = 170
    hook_length_cm: float = 32
    AtakSpeadOnUlty: float = 400
    
    def init(
        self,
        width_cm: float = 170,
        hook_length_cm: float = 32,
       AtakSpeadOnUlty: float = 400
    ):
        self.width_cm: float = width_cm
        self.hook_length: float = hook_length_cm
        self.passive_stacks: float =AtakSpeadOnUlty
        print('Yes,its Marsy')
        
class  Marsy(
    PlayablePudge,
    MixinRot,
    MixinSwimable,
    MixinTalkable
):
    pass

class ToyMarsy:
    stinky: bool = False
    size_cm3: float = 12
    width_cm: float = 8
    
    def init( 
        self,
        stinky: bool = False,
        size_cm3: float = 12,
        width_cm: float = 8
    ):
        self.stinky: bool  = stinky
        self.size_cm3: float = size_cm3
        self.width_cm: float = width_cm
        print('RubberToy Initialized')

    def stand(self):
        print('прицеливается хоком)')
        
    def head_turn(self):
        print('Поломался')


class MixinRot:
    def rot(self):
        print('Дышите глубже, ребята...')

class MixinSwimable:
    def swim(self):
        print('Холодец)')

class MixinTalkable:
    def make_noise(self):
        print('Фарш не провернуть назад... И мясо из котлет не восстановишь...')


class MixinAbilityUsage:
    def rot(self):
        print('Ability')

class MixinSwimable:
    def swim(self):
        print('Холодец)')

class MixinTalkable:
    def make_noise(self):
        print('Фарш не провернуть назад... И мясо из котлет не восстановишь...')
        
class MixinFall:
    def fall(self):
        print('Пол проломился')
        
class MixinBreakable:
    def breakable(self):
        print('Ouch')
        
class MixinWalkable:
    def walk(self):
        print('Перекатываюсь')

Илья Волков, [21.09.2023 13:23]
class Characters:
    def init(
        self,
        width_cm: float,
        height_cm: float
    ):
        self.width_cm: float = width_cm
        self.height_cm: float = height_cm
        
class Playable(MixinAbilityUsage, MixinWalkable, MixinTalkable):
    pass
        
class Toy(MixinBreakable, MixinSwimable, MixinFall):
    pass
        
class Pudge(Characters, Playable):
    width_cm: float = 100000
    hook_length_cm: float = 32000
   AtakSpeadOnUlty: float = 10
    
    def init(
        self,
        width_cm: float = 100000,
        hook_length_cm: float = 32000,
       AtakSpeadOnUlty: float = 10
    ):
        self.width_cm: float = width_cm
        self.hook_length: float = hook_length_cm
        self.passive_stacks: float =AtakSpeadOnUlty
        print('True Pudge Initialized')
        
class ToyPudge(Characters, Toy):
    stinky: bool = False
    size_cm3: float = 12
    width_cm: float = 8
    
    def init( 
        self,
        stinky: bool = False,
        size_cm3: float = 12,
        width_cm: float = 8
    ):
        self.stinky: bool  = stinky
        self.size_cm3: float = size_cm3
        self.width_cm: float = width_cm
        print('Toy')

    def stand(self):
        print('прицеливается хоком)')
        
    def head_turn(self):
        print('Поломался')