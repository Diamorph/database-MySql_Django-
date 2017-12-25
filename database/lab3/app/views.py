from django.shortcuts import render
from .models import Pharmacy,Medic,Pills
from .forms import PharmacyForm, MedicForm, PillsForm
from django.views import View

# def add_ph(request):
#     result = "Successful add!"
#     if request.method == "GET":
#         return render(request,'add-pharmacy.html')
#     if (request.method == "POST" and request.POST['name'] and request.POST['city']
#         and request.POST['lisense'] and request.POST['day_and_night']):
#         Pharmacy.objects.create(name=request.POST['name'],
#                                 city=request.POST['city'],
#                                 lisense=request.POST['lisense'],
#                                 day_and_night=request.POST['day_and_night'])
#     return render(request,'main.html',{'result':result})

class PharmacyView(View):
    form_pharmacy  = PharmacyForm
    def post(self , request):
        form = PharmacyForm(request.POST)
        if form.is_valid():
            data  = form.cleaned_data
            Pharmacy.objects.create(name=data['name'],
                                    city=data['city'],
                                    lisense=data['lisense'],
                                    day_and_night=data['day_and_night']
                                    )
            result  = "Add ok!"
            context = {
                'result':result
            }
            return render(request, 'main.html', context)
        else:
            context  = {
                'form_pharmacy': self.form_pharmacy
            }
            return render(request, 'add_pharmacy.html', context)

    def get(self ,request):
        context = {
            'form_pharmacy': self.form_pharmacy
        }
        return render(request, 'add_pharmacy.html', context)


class MedicView(View):
    form_medic  = MedicForm
    def post(self , request):
        form = MedicForm(request.POST)
        if form.is_valid():
            data  = form.cleaned_data
            Medic.objects.create(name=data['name'],
                                    lisense=data['lisense'],
                                    about=data['about'],
                                    cooperation=data['cooperation']
                                    )
            result  = "Add ok!"
            context = {
                'result':result
            }
            return render(request, 'main.html', context)
        else:
            context  = {
                'form_medic': self.form_medic
            }
            return render(request, 'add_medic.html', context)

    def get(self ,request):
        context = {
            'form_medic': self.form_medic
        }
        return render(request, 'add_medic.html', context)


class PillsView(View):
    form_pills  = PillsForm
    def post(self , request):
        form = PillsForm(request.POST)
        if form.is_valid():
            data  = form.cleaned_data
            Pills.objects.create(name=data['name'],
                                    consist=data['consist'],
                                    price=data['price'],
                                    medic=data['medic'],
                                    pharmacy=data['pharmacy']
                                    )
            result  = "Add ok!"
            context = {
                'result':result
            }
            return render(request, 'main.html', context)
        else:
            context  = {
                'form_pills': self.form_pills
            }
            return render(request, 'add_pills.html', context)

    def get(self ,request):
        context = {
            'form_pills': self.form_pills
        }
        return render(request, 'add_pills.html', context)



def del_pharmacy(request,id):
    if request.method=="POST":
        Pharmacy.objects.get(id=int(id)).delete()
        pharmacy_list = Pharmacy.objects.all()
        medic_list = Medic.objects.all()
        pills_list = Pills.objects.all()
        context = {
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pills_list': pills_list,
        }
        return render(request,'content.html',context)

def del_medic(request,id):
    if request.method=="POST":
        Medic.objects.get(id=int(id)).delete()
        pharmacy_list = Pharmacy.objects.all()
        medic_list = Medic.objects.all()
        pills_list = Pills.objects.all()
        context = {
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pills_list': pills_list,
        }
        return render(request,'content.html',context)


def del_pill(request,id):
    if request.method=="POST":
        Pills.objects.get(id=int(id)).delete()
        pharmacy_list = Pharmacy.objects.all()
        medic_list = Medic.objects.all()
        pills_list = Pills.objects.all()
        context = {
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pills_list': pills_list,
        }
        return render(request,'content.html',context)

def edit_pharmacy(request,id):
    if request.method=="GET":
        return render(request,'edit_pharmacy.html')
    if request.method=="POST":
        if "day_and_night_edit" in request.POST:
            day_and_night = 1
        else:
            day_and_night = 0
        name = request.POST['name_edit']
        city = request.POST['city_edit']
        lisense = request.POST['lisense_edit']

        print(day_and_night)
        Pharmacy.objects.filter(id=id).update(name=name, city=city, lisense=lisense, day_and_night=day_and_night)
        pharmacy_list = Pharmacy.objects.all()
        medic_list = Medic.objects.all()
        pills_list = Pills.objects.all()
        context = {
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pills_list': pills_list,
        }
        return render(request,'content.html',context)


def edit_medic(request,id):
    if request.method=="GET":
        return render(request,'edit_medic.html')
    if request.method=="POST":
        if "cooperation" in request.POST:
            cooperation = 1
        else:
            cooperation = 0
        name = request.POST['name_edit']
        lisense = request.POST['lisense_edit']
        about = request.POST['about_edit']
        Medic.objects.filter(id=id).update(name=name,lisense=lisense, about=about,  cooperation=cooperation)
        pharmacy_list = Pharmacy.objects.all()
        medic_list = Medic.objects.all()
        pills_list = Pills.objects.all()
        context = {
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pills_list': pills_list,
        }
        return render(request,'content.html',context)


def edit_pill(request,id):
    if request.method=="GET":
        pharmacy_list = Pharmacy.objects.all()
        medic_list = Medic.objects.all()
        context = {
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list
        }
        return render(request,'edit_pill.html',context)

    if request.method == "POST":
        name = request.POST['name_edit']
        consist = request.POST['consist_edit']
        price = request.POST['price_edit']
        medic = request.POST['medic_edit']
        pharmacy = request.POST['pharmacy_edit']
        Pills.objects.filter(id=id).update(name=name,consist=consist, price=price, medic=medic,pharmacy=pharmacy)
        pharmacy_list = Pharmacy.objects.all()
        medic_list = Medic.objects.all()
        pills_list = Pills.objects.all()
        context = {
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pills_list': pills_list,
        }
        return render(request,'content.html',context)


def main(request):
    pharmacy_list = Pharmacy.objects.all()
    medic_list = Medic.objects.all()
    pills_list = Pills.objects.all()
    context ={
        'pharmacy_list': pharmacy_list,
        'medic_list': medic_list,
        'pills_list': pills_list,
    }
    return render(request,'content.html',context)