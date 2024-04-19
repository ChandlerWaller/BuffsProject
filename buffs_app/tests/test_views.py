from django.test import TestCase
from django.urls import reverse

from buffs_app.models import *

class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_shifts = 13

        for shift_id in range(number_of_shifts):
            Shift.objects.create(
                date='2024-04-29',
                time='18:45:00',
                username=f'{shift_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/shifts')
        self.assertEqual(response.status_code, 301)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('shifts'))
        self.assertEqual(response.status_code, 200)