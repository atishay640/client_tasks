from django.test import TestCase
from django.urls import reverse


class ListCarFormTest(TestCase):

  def test_open_list_car_page(self):
    response = self.client.get('/listcar/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.template_name, ['list_car.html'])

  
  def test_list_a_car(self):
    data = {
      "make": "make",
      "model": "model",
      "year": 1978,
      "price": 10000,
      "seller_name": "ABC",
      "seller_mobile": "1122334455",
      
    }
    response = self.client.post(reverse('listcar'), data)
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/success/')


  def test_list_a_car_incomplete(self):
    data = {
      "make": "make",
      "model": "model",
      "year": 1978,
      "price": 1, # Price not in range 1000 to 100000
      "seller_name": "ABC",
      "seller_mobile": "1122334455",
      
    }
    response = self.client.post(reverse('listcar'), data)
    self.assertEqual(False, response.context["form"].is_valid())
    self.assertNotEqual(response, '/success/')
