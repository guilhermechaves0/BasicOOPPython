class Product:
  def __init__(self, id, name, price, quantity):
    self.id = int(id)
    self.name = str(name)
    self.price = float(price)
    self.quantity = int(quantity)

  def add(self, quantity):
    self.quantity += quantity if quantity > 0 else 1

  def remove(self, quantity):
    self.quantity -= quantity if quantity > 0 else 1

  def show(self):
    print(f'\n {self.id}| {self.name} | R${self.price}| {self.quantity}')