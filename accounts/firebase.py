import firebase_admin
from firebase_admin import credentials, auth
from django.conf import settings

cred = credentials.Certificate(settings.FIREBASE_CERT_PATH)
firebase_admin.initialize_app(cred)

