class Tapok:
    color: str
    size: int
    location: str
    mood: str

    def introduce(self):
        print(f"я {self.color} тапок {self.size} сантиметров, мя завут марк бабенко")

    def search_pair(self):
        print(f"у мя потерялся мой парный тапок, где то {self.location}.")

    def complain(self):
        print(f"мое состояние {self.mood} поч я без альтушечки")

    def dream(self):
        print(f"я мечтаю пойти в {self.location} и найти мой парный тапок чтобы быть счастливым")


if __name__ == "__main__":
    tapochok1 = Tapok("сини", 42, "в диване", "грустный")
    tapochok2 = Tapok("червоний", 38, "на крыше", "душныйфуффф")
    tapochok3 = Tapok("зелений", 40, "в тапочковом раю", "суспишосовый")

    tapochky = [tapochok1, tapochok2, tapochok3]

    for tapochok in tapochky:
        print("\n--- рамс тапочка ---")
        tapochok.introduce()
        tapochok.search_pair()
        tapochok.complain()
        tapochok.dream()