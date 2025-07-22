from django.test import TestCase
from product.models import Product
from material.models import Material
from django.utils import timezone

class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(
            quantity=10,
            product_name="Chairs",
            type="Furniture",
            price=2500,
            listed_at=timezone.now()
        )
        self.assertEqual(product.product_name, "Chairs")
        self.assertEqual(product.quantity, 10)
        self.assertEqual(str(product), f"{product.type} ({product.product_id})")

    
class MaterialModelTest(TestCase):
    def test_create_material(self):
        material = Material.objects.create(
            material_type="cotton",
            price_per_kg=150.75
        )
        self.assertEqual(material.material_type, "cotton")
        self.assertEqual(material.price_per_kg, 150.75)
        self.assertIsNotNone(material.created_at)
        self.assertEqual(str(material), f"{material.material_type} ({material.material_id})")
        
