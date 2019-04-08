"""
docstring просто чтобы pylint не показывал предупреждение
"""
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import CustomUser
from market.models import Item, Offer
from .forms import PersonRoleForm, CustomUserChangeForm
from django.contrib import messages
# Create your views here.

def my_reviews(request):
    if request.user.role == 'contractor':
        user = CustomUser.objects.get(pk=request.user.id)
        offers = user.offer_set.all()
        return render(request, 'users/my_reviews.html', {
            'offers': offers
        })
    else:
        return HttpResponseRedirect(reverse('index'))


class UserView(generic.DetailView):
    """
    view для пользователя
    """
    context_object_name = 'User'
    model = CustomUser
    template_name = 'users/user.html'

def role_register(request):
    if not request.user.role or not request.user.person:
        if request.method == 'POST':
            user = get_object_or_404(CustomUser, pk=request.user.id)
            form = PersonRoleForm(request.POST, request.FILES)
            if form.is_valid():
                role = form.cleaned_data['role']
                if role == 'contractor':
                    person = 'entity'
                else:
                    person = form.cleaned_data['person']
                user.entity_name = form.cleaned_data['entity_name']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.person = person
                user.role = role
                user.save()
                return HttpResponseRedirect(reverse('users:user', args=(user.id, )))
        else:
            form = PersonRoleForm()
            return render(request, 'users/role_register.html', {'form': form})
    else:
        messages.warning(request, 'Ваша роль уже задана, для её изменения свяжитесь с тех. поддержкой')
        return HttpResponseRedirect(reverse('index'))

def settings(request):
    form = CustomUserChangeForm()
    if request.method == 'POST':
        pass
    else:
        return render(request, 'users/settings.html', {
            'form': form
        })

# class MyWorksView(generic.ListView):
#     context_object_name = 'items'
#     models = Item
#     template_name = 'users/my_works.html'

#     def get_queryset(self):
#         return Item.objects.filter(
#             owner=self.request.user
#         ).order_by('-date_added')

def my_works_view(request):
    if request.user.role == 'custome':
        return render(request, 'users/my_works.html', {
            'items':  Item.objects.filter(owner=request.user).order_by('-date_added')
        })
    elif request.user.role == 'contractor':
        return render(request, 'users/my_works.html', {
            'offers':  Offer.objects.filter(owner=request.user).order_by('-date_added')
        })