from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json

class CompanyView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if id>0 :
            companies = list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company = companies[0]
                datos = {'message': 'Success', 'company': company}
            else:
                datos = {'message': 'Companies not found...'}
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                datos = {'message': 'Success', 'companies': companies}
            else:
                datos = {'message': 'Companies not found...'}
            return JsonResponse(datos)
            
    def post(self, request):
        jd = json.loads(request.body)
        Company.objects.create(name=jd['name'],website=jd['website'],fundation=jd['fundation'])
        datos = {'message': 'Success'}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company= Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.fundation = jd['fundation']
            company.save()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Companies not found...'}
        return JsonResponse(datos)
        
    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            Company.objects.filter(id=id).delete()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Companies not found...'}
        return JsonResponse(datos)
    
    

