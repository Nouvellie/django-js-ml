from django.shortcuts import render
from django.views.generic import TemplateView

import requests


class VerifyRegistrationView(TemplateView):

    template_name = 'apiregistration/verify-registration.html'

    def get(self, request, *args, **kwargs):
        get_data = request.__dict__
        get_values = get_data['environ']['QUERY_STRING']
        
        # Verify account dict for validation with request.
        verify_account_dict = {}

        # Creation of dict with WSGIRequest Get data.
        i = 0
        while i < 2: 
            start = get_values.find('=') + len('=')
            end = get_values.find('&')
            subdata = get_values[start:end]
            
            if i == 0:
                verify_account_dict.update({'user_id': subdata})
                to_delete = ('user_id=' + str(subdata) + "&timestamp")
            else:
                verify_account_dict.update({'timestamp': subdata})
                to_delete = ('=' + str(subdata) + "&signature=")

            get_values = get_values.replace(str(to_delete), '')
            
            i += 1
            if i == 2:
                verify_account_dict.update({'signature': get_values}) 
        
        url = 'http://127.0.0.1:8005/api/v1/accounts/verify-registration/'

        validation_reg = requests.post(url, verify_account_dict).json()
        
        return render(request, self.template_name, context=validation_reg)