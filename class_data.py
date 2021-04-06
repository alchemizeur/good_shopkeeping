




class Character: ## capable of being attacked, being KO'ed, defending themselves, buying and selling, holding inventory, droppimg inventory
    def __init__(self, name,idn_poss,idn_subj,idn_verb,hp,mp,str,dfn,mdf):
        self.name = name                               ## Name of character
        self.status_name = status_name                 ## usually redundant, 'You' for the player, and any name you give to someone else.
        self.lvl = lvl                                 ## level
        self.idn_poss = idn_poss                       ## possessive for corresponding identity
        self.idn_subj = idn_subj                       ## subject for corresponding identity
        self.idn_verb = idn_verb                       ## verb for corresponding identity
        self.klass = klass                             ## main class
        self.subklass = subklass                       ## subclass (concentration)
        self.max_hp = hp                               ## max hp, static excluding levels
        self.hp = hp                                   ## current hp, determines states
        self.max_mp = mp                               ## max mp, static excluding levels
        self.mp = mp                                   ## current mp, determines states
        self.str = str                                 ## strength. push checks. Phys type weapon checks.
        self.dfn = dfn                                 ## defense. Attack saves.
        self.mdf = mdf                                 ## magic defense. Magic attack saves.
        self.wis = wis                                 ## wisdom. needed for mana regeneration
        self.itl = itl                                 ## intelligence. needed for deciphering, spellcasting and knowledge checks.
        self.cha = cha                                 ## charisma. Needed for diplomoacy, intimidation, charm and lying.
        self.luc = luc                                 ## luck. Used for looting, miss attack chance, death chance
        self.agl = agl                                 ## agility. used for dodging, acrobatics.
        self.per = per                                 ## perception. used for sight and sense.
        self.con = con                                 ## constitution. used for physical resistance checks.
        self.wil = wil                                 ## will. used for mental resistance.
        self.ini = ini                                 ## base initiative. Used for beginning conflict

        ## status section
        self.is_dead = False
        self.is_incapacitated = False
        self.incapacitated_duration = None
        self.is_shook = False
        self.is_invigorated = False
        self.is_drunk = False
        self.drunk_state = 0
        self.is_poisoned = False
        self.poison_duration = None
        self.poison_amt = None
    #    self.is_charmed = False
    #    self.is_on_fire = False
    #    self.is_hungry = False
    #    self.hunger_level = None                        ## max 10? 10 is full, 0 is starvinf

        ## can be statuses
        self.can_be_shook = False if self.klass == 'Sword of Re' else True
        self.can_be_charmed = False if self.klass == 'Sword of Re' else True
        self.can_be_poisoned = False if self.klass == 'Feraling' else True

        ## affection statuses
        self.rel_Player = None
        self.rel_landriel = None
        self.rel_kip: = None
        self.rel_undine: = None
        self.rel_elgis = None
        self.rel_lognar = None
        self.rel_endeppoli = None
        self.rel_Lumus = None


    def take_damage(self,dmg_amt,source,aggressor): ## potions take negative damage, there is no need for a heal buff
        self.hp -= dmg_amt
        if dmg_amt >= 0:
            print(f"{self.name} {self.idn_poss} taken {dmg_amt} damage from {aggressor}'s {source}!")
        else dmg_amt < 0:
            print(f"{self.name} {self.idn_poss} healed {dmg_amt} damage from {aggressor}'s {source}!")
        if self.hp <= 0:
            self.is_dead = True
        if dmg_amt > self.max_hp*.5:
            self.shake()
        if dmg_amt*-1 > self.max_hp*.5:
            self.invigorate()

    def incapacitate(self,duration): # fainting, not death
        self.is_incapacitated = True
        self.incapacitated_duration = duration

    def incapacitate_counter(self):
        if self.is_incapacitated:
            if self.incapacitated_duration >0:
                self.incapacitated_duration -= 1
            else:
                self.bounce_back()
    def bounce_back():
        self.is_incapacitated = False
        self.incapacitated_duration = None

    def shake(self):            # shake is currently 1 round, by default, Emulate poison if shook can last multiple rounds
        if self.can_be_shook:
            self.is_shook = True

    def unshake(self):
        self.is_shook = False

    def invigorate(self):
        self.is_invigorated = True

    def vigor_fade(self):
        self.is_invigorated = False

    def poison(self, duration, amt):
        if self.can_be_poisoned:
            self.is_poisoned = True
            self.poison_duration = duration
            self.poison_amt = amt

    def unpoison(self):
        self.is_poisoned = False
        self.poison_duration = None
        self.poison_amt = None

    def poison_counter(self):
        if self.is_poisoned:
            if self.poison_duration > 0:
                self.poison_duration -= 1
                self.take_damage(self.poison_amt)
            else:
                self.unpoison()

    def get_drunk(self,alc_lvl): ## use like poison counter, 1 = drunk, 2 = very drunk, 3 = wasted, 4 = beligerent (take damage)
        roller_alcohol = random.randint(1, 10)
        roller_player = random.randint(1,5)
        if self.is_drunk: # if you are drunk, check against roller stats, tick up to lvl 4 then take damage, maybe--
            if roller_alcohol > roller_player+randint(1, (self.con/2)):
            self.drunk_state + 1
                if drunk state > 4:
                    drunk_state = 4
        else:
            self.is_drunk = True
            self.drunk_state = 1

    def drunk_states(alc_lvl):
        drunk_state_dict = {1: 'drunk', 2: 'very drunk', 3: 'wasted', 4: 'beligerent'}
        if drunk_state = 4:
            self.take_damage(self.alc_lvl)
        if drunk_state = 3:
            alc_dmg = round(alc_lvl/2)
            self.take_damage(alc_dmg)






##        drunk_indicators = (f'{status_name} {idn_verb} drunk. Movements slow and speech is impaired.',f'Seeing double, are we? It looks like {status_name} {idn_verb} lost sobriety.',f'{status_name} {idn_verb} now drunk.',f'Drink the Ale and pay the price, {status_name} {idn_verb} now drunk.','')
##        very_drunk_indicators = ()
##        beligerant_indicators =('What are you trying to do? {status_name} {idn_verb}')
        if self.is_belligerent:
            poison_amt = alc_lvl*2
            self.take_damage(self.poison_amt)
        if self.is_wasted:
            if roller_alcohol > roller_player+randint(1, (self.con/2)):
                self.is_belligerent = True
        if self.is_v_drunk:


# check your constitution, luck, max_hp if you dont beat the constitution threshold, you start to take damage.

            print("You have become beligerant")
        if self.is_drunk = True
        self.get_very_drunk()
        else:
            if is_hungry:
            player_check = self.con*(.10*self.hunger_level)+roller_player
            else:
            player_check = self.con * roller_player
        if player_check < alc_lvl * roller_alcohol:
                self.is_drunk = True

    def get_very_drunk(self):
        if self.is_very_drunk = True
        self.get_wasted()

    def get_wasted(self):
        if get_
    def drunk_timer(self):



    def self_awareness(self):
        print(f"I am {self.name}.")

    def attack(self, other_character):
        self.equipped_weapon.deal_damage(other_character)

# poisonedWeapon.attack(playerCharacter)

class Weapon:
    def deal_damage(self, character):
        character.take_damage(self.attack_value)
        character.poison(self.poison_duration, self.poison_amt)

class Player(Character):
    def __init__(self):
        super().__init__(name="traveller", hp=10, m)

class Npc(Character):

class Beast(Character): ## capable of being tamed, looted or



class Item: ## can be held in inventory, or

class weapon(Item):

class armor(Item):

class ammunition(Item):

class gift(Item):

class pet(Item):

#### ITEM(MISC)

    player_data = {}
