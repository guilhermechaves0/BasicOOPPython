class Cart:
  def __init__(self):
    self.products = []
    self.total_value = 0.0
  
  def add_product(self, product):
    if(self.not_have_product(product)):
      self.products.append(product)
      self.total_value += product.price
    else:
      for item in self.products:
        if(item.id == product.id):
          item.add(product.quantity)
          self.total_value += product.price

  def not_have_product(self, product):
    for item in self.products:
      if(item.id == product.id):
        return False
    return True

  def remove_product(self, product):
    for item in self.products:
      if(item.id == product.id):
        item.remove(product.quantity)
        self.total_value -= product.price

        if(item.quantity == 0):
          self.products.remove(item)

  def clean(self):
    self.products = []
    self.total_value = 0.0