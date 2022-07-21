# drf-sepctacular

def dispatch(self, request, *args, **kwargs):
    """Updates the keyword args to always have 'foo' with the value 'bar'"""
    if 'foo' in kwargs:
        # Block requests that attempt to provide their own foo value
        return HttpResponse(status_code=400)
    kwargs.update({'foo': 'bar'}) # inject the foo value
    # now process dispatch as it otherwise normally would
    return super().dispatch(request, *args, **kwargs)

def setup(self):
    self.client.login(
        username=self.the_user.username, password=TEST_PASSWORD
        )


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# host: EMAIL_HOST
# port: EMAIL_PORT 587
# username: EMAIL_HOST_USER
# password: EMAIL_HOST_PASSWORD
# use_tls: EMAIL_USE_TLS
# use_ssl: EMAIL_USE_SSL
# timeout: EMAIL_TIMEOUT
# ssl_keyfile: EMAIL_SSL_KEYFILE
# ssl_certfile: EMAIL_SSL_CERTFILE
