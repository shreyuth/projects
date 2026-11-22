class Asset:
    def __init__(self, assetnum, description, age):
        self.assetnum = assetnum
        self.description = description
        self.age = age

    def maintenance_check(self):
        if self.age > 10:
            print(self.assetnum, "needs maintenance.")
        else:
            print(self.assetnum, "is in good condition.")

class pumpAsset(Asset):
    def display_info(self):
        print("Asset Number:", self.assetnum)


class generatorAsset(Asset):
    def generator_info(self):
        print("Asset Description:", self.description)

asset1 = Asset("A1234", "Generator", 12)
asset2 = Asset("B1234", "Pump", 8)
asset3 = Asset("C1234", "Compressor", 15)

asset1.maintenance_check()
asset2.maintenance_check()
asset3.maintenance_check()

pump = pumpAsset("P1234", "Pump1", 5)
pump.display_info()

generator = generatorAsset("G1234", "Generator1", 20)
generator.generator_info()