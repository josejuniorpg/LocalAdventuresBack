import json
import os
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from LocalAdventuresBack.settings.base import BASE_DIR
from apps.invoices.serializers import InvoiceFAQSerializer


# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def invoiceFAQ_info(request):
    json_file_path = os.path.join(BASE_DIR / 'apps/invoices/assets/faqSection.json')
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            invoices_data = json.load(json_file)
        serializer = InvoiceFAQSerializer(invoices_data, many=True)
        return JsonResponse(serializer.data, safe=False)
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
