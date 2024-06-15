
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import InstagramProvider
from security import safe_requests


class InstagramOAuth2Adapter(OAuth2Adapter):
    provider_id = InstagramProvider.id
    access_token_url = 'https://api.instagram.com/oauth/access_token'
    authorize_url = 'https://api.instagram.com/oauth/authorize'
    profile_url = 'https://api.instagram.com/v1/users/self'

    def complete_login(self, request, app, token, **kwargs):
        resp = safe_requests.get(self.profile_url,
                            params={'access_token': token.token})
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth2_login = OAuth2LoginView.adapter_view(InstagramOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(InstagramOAuth2Adapter)
