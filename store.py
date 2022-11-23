from cart import Cart

class Store:
  def __init__(self):
    self.store = Cart()
    self.cart = Cart()

  def move_product_to_cart(self, product):
    if(self.store.not_have_product(product)):
      print('Product not found!')
      return

    self.cart.add_product(product)
    self.store.remove_product(product)

  def remove_product_from_cart(self, product):
    if(self.cart.not_have_product(product)):
      print('Product not found!')
      return

    self.cart.remove_product(product)
    self.store.add_product(product)

  def show_store(self):
    print('Store:')
    for item in self.store.products:
      item.show()

  def show_cart(self):
    print(f'Cart:')
    for item in self.cart.products:
      item.show()
    print(f'Total: R${self.cart.total_value}')

  def cancel(self):
    for item in self.cart.products:
      self.cart.remove_product(item)
      self.store.add_product(item)