from django.shortcuts import render ,redirect
from django.db import connection
from django.http import HttpResponse
import csv




def show_all_pharmacy():
    cursor = connection.cursor()
    cursor.execute('select id, name, city, lisense, day_and_night from db.pharmacy')
    pharmacy_list = cursor.fetchall()
    return pharmacy_list


def show_ph_name():
    cursor = connection.cursor()
    cursor.execute('select name from db.pharmacy')
    ph_name_list = cursor.fetchall()
    return ph_name_list

def show_med_name():
    cursor = connection.cursor()
    cursor.execute('select name from db.medic')
    med_name_list = cursor.fetchall()
    return med_name_list

def show_pill_id():
    cursor = connection.cursor()
    cursor.execute('select id from db.pills')
    pills_id_list = cursor.fetchall()
    return pills_id_list

def show_all_medics():
    cursor = connection.cursor()
    cursor.execute('select id, name, lisense, about, cooperation from db.medic')
    medic_list = cursor.fetchall()
    return medic_list

def show_all_pills():
    cursor = connection.cursor()
    cursor.execute('select id, name, consist, price, medic_id, pharmacy_id from db.pills')
    pill_list = cursor.fetchall()
    return pill_list



def write_pharmacy(request):
    cursor = connection.cursor()
    cursor.execute('TRUNCATE TABLE db.pharmacy;')
    with open("D:/BD/lab/lab2/data.csv", "r") as data_file:
        data = csv.DictReader(data_file)
        for row in data:
            cursor.execute('INSERT INTO db.pharmacy (name , city , lisense, day_and_night) VALUES(%s , %s , %s, %s)',
                                (row['name'] , row['city'] , row['lisense'], row['day_and_night']))
            result = "Аптеки успішно записані в БД!"
    pharmacy_list = show_all_pharmacy()
    context = {
        'result': result,
        'pharmacy_list': pharmacy_list,
    }

    return render(request , 'lab2/main.html' , context)



def write_medic(request):
    cursor = connection.cursor()
    cursor.execute('TRUNCATE TABLE db.medic;')
    with open("D:/BD/lab/lab2/data_med.csv", "r") as data_file:
        data = csv.DictReader(data_file)
        for row in data:
            cursor.execute('INSERT INTO db.medic (name , lisense , about, cooperation) VALUES(%s , %s , %s, %s)',
                                (row['name'] , row['lisense'] , row['about'], row['cooperation']))
            result = "Виробники успішно записані в БД!"
    medic_list = show_all_medics()
    context = {
        'result': result,
        'medic_list': medic_list,
    }

    return render(request , 'lab2/main.html' , context)


def add_pills(request):
    if request.method == "GET":
        pharmacy_list = show_all_pharmacy()
        medic_list = show_all_medics()
        pill_list = show_all_pills()
        med_name_list = show_med_name()
        ph_name_list = show_ph_name()
        pills_id_list = show_pill_id()
        context = {
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pill_list': pill_list,
            'med_name_list': med_name_list,
            'ph_name_list': ph_name_list,
            'pills_id_list': pills_id_list,

        }
        return render(request, 'lab2/add_pills.html', context)


    if request.method == "POST":
        name = request.POST['name']
        consist = request.POST['consist']
        price = request.POST['price']
        medic = request.POST['medic']
        pharmacy = request.POST['pharmacy']

        cursor = connection.cursor()

        cursor.execute("SELECT id FROM db.medic WHERE name = %s", (medic, ))
        med_id = cursor.fetchall()
        for i in med_id:
            m_id = i[0]

        cursor.execute("SELECT id FROM db.pharmacy WHERE name = %s", (pharmacy, ))
        ph_id = cursor.fetchall()
        for a in ph_id:
            p_id = a[0]

        cursor.execute("INSERT INTO db.pills (name, consist, price, medic_id, pharmacy_id) VALUES (%s,%s,%s,%s,%s)",
                       (name, consist, price, m_id,p_id)
                       )

    return redirect('/')

def delete(request,id):
    if request.method == "POST":
        cursor = connection.cursor()

        cursor.execute('DELETE FROM db.pills WHERE id = %s ', (id,))
        result = "Видалено!"

        pharmacy_list = show_all_pharmacy()
        medic_list = show_all_medics()
        pill_list = show_all_pills()
        med_name_list = show_med_name()
        ph_name_list = show_ph_name()
        pills_id_list = show_pill_id()
        context = {
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pill_list': pill_list,
            'med_name_list': med_name_list,
            'ph_name_list': ph_name_list,
            'pills_id_list': pills_id_list,

        }
    return render(request, 'lab2/content.html', context)


def edit(request,id):
    if request.method == "GET":
        pharmacy_list = show_all_pharmacy()
        medic_list = show_all_medics()
        pill_list = show_all_pills()
        med_name_list = show_med_name()
        ph_name_list = show_ph_name()
        pills_id_list = show_pill_id()
        context = {
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pill_list': pill_list,
            'med_name_list': med_name_list,
            'ph_name_list': ph_name_list,
            'pills_id_list': pills_id_list,

        }
        return render(request,'lab2/edit_pill.html',context)

    if request.method == "POST":
        name = request.POST['name_edit']
        consist = request.POST['consist_edit']
        price = request.POST['price_edit']
        medic = request.POST['medic_edit']
        pharmacy = request.POST['pharmacy_edit']
        cursor = connection.cursor()

        cursor.execute("SELECT id FROM db.medic WHERE name = %s", (medic,))
        med_id = cursor.fetchall()
        for i in med_id:
            m_id = i[0]

        cursor.execute("SELECT id FROM db.pharmacy WHERE name = %s", (pharmacy,))
        ph_id = cursor.fetchall()
        for a in ph_id:
            p_id = a[0]
        cursor.execute(
            "UPDATE db.pills SET name = %s, consist = %s, price = %s, medic_id = %s, pharmacy_id = %s WHERE id = %s",
            (name, consist, price, m_id, p_id, id)
            )

    return redirect('/')


def search_ph(request):
    if request.method == "GET":
        pharmacy_list = show_all_pharmacy()
        context = {
            'pharmacy_list': pharmacy_list
        }
        return render(request,'lab2/search-ph.html',context)

    if request.method == "POST":
        city = request.POST['city_search']
        day_and_night = request.POST['day_and_night_search']
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM db.pharmacy WHERE city = %s AND day_and_night = %s',
                       (city,day_and_night))
        result_list = cursor.fetchall()
        if len(result_list) == 0:
            empty = "Нічого не знайдено"
            return render(request, 'lab2/main.html', {'empty': empty})

        pharmacy_list = show_all_pharmacy()
        medic_list = show_all_medics()
        pill_list = show_all_pills()
        med_name_list = show_med_name()
        ph_name_list = show_ph_name()
        pills_id_list = show_pill_id()
        context = {
            'result_list': result_list,
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pill_list': pill_list,
            'med_name_list': med_name_list,
            'ph_name_list': ph_name_list,
            'pills_id_list': pills_id_list,
        }
        return render(request, 'lab2/result_search-ph.html', context)



def search_med(request):
    if request.method == "GET":
        medic_list = show_all_medics()
        context = {
            'medic_list': medic_list
        }
        return render(request,'lab2/search-med.html',context)

    if request.method == "POST":
        lisense = request.POST['lisense_search']
        cooperation = request.POST['cooperation_search']
        cursor = connection.cursor()
        cursor.execute('SELECT id, name, lisense, about, cooperation FROM db.medic WHERE lisense = %s AND cooperation = %s',
                       (lisense,cooperation))
        result_list = cursor.fetchall()
        if len(result_list) == 0:
            empty = "Нічого не знайдено"
            return render(request, 'lab2/main.html', {'empty': empty})

        pharmacy_list = show_all_pharmacy()
        medic_list = show_all_medics()
        pill_list = show_all_pills()
        med_name_list = show_med_name()
        ph_name_list = show_ph_name()
        pills_id_list = show_pill_id()
        context = {
            'result_list': result_list,
            'pharmacy_list': pharmacy_list,
            'medic_list': medic_list,
            'pill_list': pill_list,
            'med_name_list': med_name_list,
            'ph_name_list': ph_name_list,
            'pills_id_list': pills_id_list,
        }
        return render(request, 'lab2/result_search-med.html', context)


def search_boolean(request):
    if request.method == "GET":
        pill_list = show_all_pills()
        context = {
            'pill_list': pill_list
        }
        return render(request, 'lab2/search_pills.html', context)
    if request.method == "POST":
        search = request.POST['search_bool']
        cursor = connection.cursor()
        cursor.execute(""" SELECT * FROM db.pills WHERE MATCH (name,consist) 
        AGAINST (%s IN BOOLEAN MODE);""",(search,))
        result_list = cursor.fetchall()
        if len(result_list) == 0:
            empty = "Нічого не знайдено"
            return render(request, 'lab2/main.html', {'empty': empty})
        context = {
            'result_list': result_list
        }
        return render(request, 'lab2/result_search-pills.html', context)


def index(request):
    pharmacy_list = show_all_pharmacy()
    medic_list = show_all_medics()
    pill_list = show_all_pills()
    med_name_list = show_med_name()
    ph_name_list = show_ph_name()
    pills_id_list = show_pill_id()
    context = {
        'pharmacy_list':pharmacy_list,
        'medic_list':medic_list,
        'pill_list':pill_list,
        'med_name_list': med_name_list,
        'ph_name_list': ph_name_list,
        'pills_id_list': pills_id_list,

    }
    return render(request, 'lab2/content.html', context)