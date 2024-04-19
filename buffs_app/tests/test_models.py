from django.test import TestCase
from buffs_app.models import Shift

class ShiftModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Shift.objects.create(date='2024-04-29', time='18:30:00', is_available='True', position='1st Bar', username=' ')

    def test_date(self):
        shift = Shift.objects.get(id=1)
        field_label = Shift._meta.get_field('date').verbose_name
        print(field_label)
        self.assertEqual(field_label, 'date')

    def test_time(self):
        shift = Shift.objects.get(id=1)
        field_label = Shift._meta.get_field('time').verbose_name
        self.assertEqual(field_label, 'time')

    def test_time(self):
        shift = Shift.objects.get(id=1)
        field_label = Shift._meta.get_field('position').verbose_name
        self.assertEqual(field_label, 'position')

    def test_username_length(self):
        shift = Shift.objects.get(id=1)
        max_length = Shift._meta.get_field('username').max_length
        self.assertEqual(max_length, 200)

    def test_self_str(self):
        shift = Shift.objects.get(id=1)
        expected_string = '1st Bar 2024-04-29  '
        self.assertEqual(expected_string, shift.__str__())

    def test_get_absolute_url(self):
        shift = Shift.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(Shift.get_absolute_url(shift), '/shift/1')