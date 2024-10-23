from django.test import TestCase
from AppName.viewmodels.home_viewmodel import HomeViewModel
from AppName.models import Product


class HomeViewModelTest(TestCase):
    def setUp(self):
        Product.objects.create(name='Test Product', price=99.99)

    def test_load_products(self):
        vm = HomeViewModel()
        vm.load_products()
        self.assertEqual(len(vm.products), 1)
        self.assertEqual(vm.products[0].name, 'Test Product')
