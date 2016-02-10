#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Bares, Tapas


def populate():
    pillin_bar = add_bar('Bar El Pillin', address='C/Pedro Antonio de Alarcon Nº1', views=128, likes=64)

    add_tapas(bar=pillin_bar,
        title="Sandwich",
        url="http://maxpubli.com/wp-content/uploads/club-sandwich.jpg", views=80)

    add_tapas(bar=pillin_bar,
        title="Patatas con queso",
        url="http://www.divinacocina.es/wp-content/uploads/patatas-con-queso-y-bacon.jpg", views=15)

    add_tapas(bar=pillin_bar,
        title="Hamburguesa",
        url="http://www.lavidacotidiana.es/wp-content/uploads/2012/10/comida-basura-patatas-fritas-hamburguesa.jpg", views=60)

    rey_bar = add_bar("El rey de Tapas", address='C/El parque nº2', views=64, likes=32)

    add_tapas(bar=rey_bar,
        title="Lomo Queso",
        url="http://barestudiantil.net/wp-content/uploads/20130329-100143.jpg", views=50)

    add_tapas(bar=rey_bar,
        title="Pinchitos",
        url="http://www.decaminoamicocina.com/wp-content/uploads/2012/07/pinchitos-morunos.jpg", views=13)

    add_tapas(bar=rey_bar,
        title="Montaditos",
        url="http://milrecetas.net/wp-content/uploads/2015/11/Montaditos-recetas-2.jpg", views=34)

    locura_bar = add_bar("La locura", address='C/Reyes Catolicos Nº1', views=32, likes=16)

    add_tapas(bar=locura_bar,
        title="Tortilla de Patatas",
        url="http://eldesvandemaria.es/wp-content/uploads/2014/11/tortilla-de-patatas.jpg", views=12)

    add_tapas(bar=locura_bar,
        title="Panini",
        url="https://www.recetin.com/wp-content/uploads/2011/09/panini_atun.jpg", views=20)

    # Print out what we have added to the user.
    for c in Bares.objects.all():
        for p in Tapas.objects.filter(bares=c):
            print "- {0} - {1}".format(str(c), str(p))


    # Print out what we have added to the user.
    for b in Bares.objects.all():
        for t in Tapas.objects.filter(bares=b):
            print "- {0} - {1}".format(str(b), str(t))

def add_tapas(bar, title, url, views=0):
    t = Tapas.objects.get_or_create(bares=bar, title=title)[0]
    t.url=url
    t.views=views
    t.save()
    return t

def add_bar(name, address='NULL', views=0, likes=0):
    b = Bares.objects.get_or_create(name=name)[0]
    b.address=address
    b.views=views
    b.likes=likes
    b.save()
    return b

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
