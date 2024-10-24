from django.urls import path

from apps.invoices.views import invoiceFAQ_info

urlpatterns = [
    path('FAQ/', invoiceFAQ_info, name='invoiceFAQ_info'),  # Ruta para acceder a la API
]
