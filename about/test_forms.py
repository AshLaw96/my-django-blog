from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'neo',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is invalid")

    def test_form_name_is_required(self):
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg='Name was not provided, but form is valid')

    def test_form_email_is_required(self):
        form = CollaborateForm({
            'name': 'neo',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg='Email was not provided, but form is valid')

    def test_form_message_is_required(self):
        form = CollaborateForm({
            'name': 'neo',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg='Message was not provided, but form is valid')
