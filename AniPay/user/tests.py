from django.test import TestCase
from django.urls import reverse
from rest_framework import status


# Create your tests here.

class TestSignUp(TestCase):
    # arrange
    # act
    # assert

    def test_signup_returns_201(self):
        url = reverse("create_wallet")
        data = {
            "first_name": "Emmanuel",
            "last_name": "Olatunji",
            "username": "Olatunji123",
            "email": "olatunjie335@gmail.com",
            "phone_number": "07054898793",
            "password": "Pass90rd3!"
        }

        response = self.client.post(url, data , format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bad_request_returns_400(self):
            url = reverse("create_wallet")
            data = {
                "first_name": "Emmanuel",
                "last_name": "Olatunji",
                "username": "Olatunji123",
                "email": "olatunjie335",
                "phone_number": "070548993",
                "password": "Pass90rd3!"
            }

            result = self.client.post(url, data, format="json")
            self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)


    def test_that_user_can_login(self):
        url = reverse("create_wallet")
        data = {
            "first_name": "Emmanuel",
            "last_name": "Olatunji",
            "username": "Olatunji123",
            "email": "olatunjie335@gmail.com",
            "phone_number": "070548993",
            "password": "Pass90rd3!"
        }
        # result = self.client.post(url, data, format="json")
        url2 = reverse("login")
        data2 ={
            "email" : "olatunjie335@gmail.com",
            "password" : "Pass90rd3!"
        }

        response = self.client.post(url2, data2 , format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_for_invalid_login_details(self):
        url0 = reverse("create_wallet")
        data0 = {
                "first_name": "Emmanuel",
                "last_name": "Olatunji",
                "username": "Olatunji123",
                "email": "olatunjie335@gmail.com",
                "phone_number": "070548993",
                "password": "Pass90rd3!"
        }
        # result2 = self.client.post(url0, data0, format="json")

        url3 = reverse("login")
        data3 = {
                "email": "olatuie335@gmail.com",
                "password": "Pass90rd3!"
            }
        response2 = self.client.post(url3, data3, format="json")
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)