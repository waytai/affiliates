from django.test.client import RequestFactory

from funfactory.urlresolvers import reverse
from mock import Mock, patch
from nose.tools import eq_

from affiliates.base import views
from affiliates.base.tests import TestCase


class ErrorPageTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self._in_facebook_app_patch = patch('affiliates.base.views.in_facebook_app')
        self.in_facebook_app = self._in_facebook_app_patch.start()

    def tearDown(self):
        self._in_facebook_app_patch.stop()

    def test_404(self):
        request = self.factory.get('/')
        self.in_facebook_app.return_value = False

        with patch('affiliates.base.views.page_not_found') as page_not_found:
            eq_(views.handler404(request), page_not_found.return_value)

            self.in_facebook_app.assert_called_with(request)
            page_not_found.assert_called_with(request)

    def test_facebook_404(self):
        request = self.factory.get('/')
        self.in_facebook_app.return_value = True

        with patch('affiliates.base.views.render') as render:
            eq_(views.handler404(request), render.return_value)

            self.in_facebook_app.assert_called_with(request)
            render.assert_called_with(request, 'facebook/error.html', status=404)

    def test_500(self):
        request = self.factory.get('/')
        self.in_facebook_app.return_value = False

        with patch('affiliates.base.views.server_error') as server_error:
            eq_(views.handler500(request), server_error.return_value)

            self.in_facebook_app.assert_called_with(request)
            server_error.assert_called_with(request)

    def test_facebook_500(self):
        request = self.factory.get('/')
        self.in_facebook_app.return_value = True

        with patch('affiliates.base.views.render') as render:
            eq_(views.handler500(request), render.return_value)

            self.in_facebook_app.assert_called_with(request)
            render.assert_called_with(request, 'facebook/error.html', status=500)


class LandingTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_not_authenticated(self):
        """
        If the current user isn't authenticated, render the landing
        page.
        """
        request = self.factory.get('/')
        request.user = Mock()
        request.user.is_authenticated.return_value = False

        with patch('affiliates.base.views.render') as render:
            eq_(views.landing(request), render.return_value)
            render.assert_called_with(request, 'base/landing.html')

    def test_authenticated(self):
        """
        If the current user is authenticated, redirect to the dashboard.
        """
        request = self.factory.get('/')
        request.user = Mock()
        request.user.is_authenticated.return_value = True

        response = views.landing(request)
        self.assertRedirectsNoFollow(response, reverse('base.dashboard'))
