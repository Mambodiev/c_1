from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import views
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('selectlanguage', views.selectlanguage, name='selectlanguage'),
    # path('selectcurrency', views.selectcurrency, name='selectcurrency'),
    path('savelangcur', views.savelangcur, name='savelangcur'),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(_('accounts/'), include('allauth.urls')),
    path('', views.home, name='home'),
    path(_('about/'), views.about, name='about'),
    path(_('privacy_policy/'), views.privacy_policy, name='privacy_policy'),
    path(_('shipping_returns/'), views.shipping_returns, name='shipping_returns'),
    path(_('contact/'), views.ContactView.as_view(), name='contact'),
    path(_('faq/'), views.faq, name='faq'),
    path(_('terms_of_use/'), views.terms_of_use, name='terms_of_use'),
    path(_('cart/'), include('cart.urls', namespace='cart')),
    path(_('staff/'), include('staff.urls', namespace='staff')),
    path(_('profile/'), views.ProfileView.as_view(), name='profile'),
    path('_ckeditor/', include('ckeditor_uploader.urls')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
