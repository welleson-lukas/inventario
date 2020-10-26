from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Equipamento, Garantia
from .forms import EquipamentoForm


def cadastrar_equipamento(request):
    if request.method == "POST":
        form_equipamento = EquipamentoForm(request.POST, request.FILES)

        if form_equipamento.is_valid():
            form_equipamento.save()
            return redirect('index')

    else:
        form_equipamento = EquipamentoForm()
    return render(request, 'core/form_equipamento.html', {"form_equipamnto": form_equipamento})


class ListaEquipamento(ListView):
    model = Equipamento
    template_name = 'core/index.html'
    context_object_name = 'equipamentos'

class ComputadoresView(ListView):
    model = Equipamento
    template_name = 'core/desktop.html'
    context_object_name = 'computadores'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(tipo='Desktop')

        return qs


class LaptopView(ListView):
    model = Equipamento
    template_name = 'core/laptop.html'
    context_object_name = 'laptops'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(tipo='Laptop')

        return qs


class MonitorView(ListView):
    model = Equipamento
    template_name = 'core/laptop.html'
    context_object_name = 'monitor'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(tipo='Monitor')

        return qs


class NobreakView(ListView):
    model = Equipamento
    template_name = 'core/nobreak.html'
    context_object_name = 'nobreaks'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(tipo='Nobreak')

        return qs


class RoteadorView(ListView):
    model = Equipamento
    template_name = 'core/roteador.html'
    context_object_name = 'roteadores'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(tipo='Roteador')

        return qs


class SwitchView(ListView):
    model = Equipamento
    template_name = 'core/switch.html'
    context_object_name = 'switchs'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(tipo='Switch')

        return qs


class SmartphoneView(ListView):
    model = Equipamento
    template_name = 'core/smartphone.html'
    context_object_name = 'smartphones'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(tipo='Smartphone')

        return qs


class InativosView(ListView):
    model = Equipamento
    template_name = 'core/inativos.html'
    context_object_name = 'equipamentos'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(status=False)

        return qs