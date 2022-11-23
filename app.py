from store import Store
from product import Product


def app():
  loja = Store()
  produto1 = Product(1, 'Cueca Premium', 79.99, 1)
  produto2 = Product(2, 'Cueca Básica', 9.90, 1)
  produto3 = Product(3, 'Calça Jeans', 129.90, 1)
  produto4 = Product(4, 'Calça Skinny Rosa', 119.90, 1)

  loja.store.add_product(Product(1, 'Cueca Premium', 79.99, 5))
  loja.store.add_product(Product(2, 'Cueca Básica', 9.90, 5))
  loja.store.add_product(Product(3, 'Calça Jeans', 129.90, 5))
  loja.store.add_product(Product(4, 'Calça Skinny Rosa', 119.90, 5))


  while True:
      print('Select the option below which you want to do:')
      option = int(input('1 - Add product to cart\n2 - Remove product from cart\n3 - Show cart\n5 - Finish\n6 - Cancel\n7 - Exit\n'))

      if (option == 1):
        loja.show_store()
        id = int(input('Select the product id: '))
        if(id == 1):
          loja.move_product_to_cart(produto1)
        elif(id == 2):
          loja.move_product_to_cart(produto2)
        elif(id == 3):
          loja.move_product_to_cart(produto3)
        elif(id == 4):
          loja.move_product_to_cart(produto4)
        else:
          print('Invalid product id')
      elif(option == 2):
        if(len(loja.cart.products) <= 0):
          print('Cart is empty\n')
          continue

        loja.show_cart()
        id = int(input('Select the product id: '))
        if(id == 1):
          loja.remove_product_from_cart(produto1)
        elif(id == 2):
          loja.remove_product_from_cart(produto2)
        elif(id == 3):
          loja.remove_product_from_cart(produto3)
        elif(id == 4):
          loja.remove_product_from_cart(produto4)
        else:
          print('Invalid product id')
      elif(option == 3):
        loja.show_cart()
      elif(option == 5):
        loja.show_cart()
        print('Thank you for your purchase!')
        break
      elif(option == 6):
        loja.cancel()
        pass
      elif(option == 7):
        loja.cancel()
        loja.show_cart()
        loja.show_store()
        print('Thanks for using our store!')	
        break
      else:
        print('Invalid option')
