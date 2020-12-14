
class NPC:
    def __init__(self, name):
        self.name = name
        self.greet()

    def say(self, phrase):
        print(f"{self.name}: {phrase}")

    def greet(self):
        self.say(f"Hi! I'm {self.name}. Good to meet you!")


class IRS:
    def __init__(self):
        pass

    def notify(amount):
        if amount > 1_000_000:
            print("IT'S THE SOUND OF THE POLICE")
            return True
        return False


class Shopkeeper(NPC):
    def __init__(self, name, gold):
        self.gold = gold
        super().__init__(name)

    def __repr__(self):
        return f"Shopkeeper {self.name}"

    def greet(self):
        super().greet()
        self.say(f"I have {self.gold} gold!")

    def donate(self, amount, recipient):
        gold = self.gold
        if recipient is self:
            self.say("Good one..")
            return
        if self.gold - amount > 0:
            self.say(f"I'm feeling generous. Here's {amount} gold pieces!")
            try:
                recipient.receive(amount)
                self.gold -= amount # equivalent to gold = gold - amount
            except ValueError:
                self.say("They didn't want it...")
        else:
            self.say(f"Do I look like I'm made of money?")

    def receive(self, amount):
        if IRS.notify(amount):
            self.say("Uh oh. Get out!")
            raise ValueError("IRS Error")
        else:
            self.say("That's very gracious, thank you!")
            self.gold += amount
