from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.forms import modelformset_factory
from .models import Item, Offer, Images, Material, Contract
from users.models import CustomUser
from .forms import PostItemForm, ImageForm
from django.contrib import messages

# Create your views here.
def index_filter(request):
    if request.method == 'POST':
        value = request.POST.get('value')

        if value == '-100':
            return render(request, 'market/index.html', {
                'items': Item.objects.filter(power__lte=100).order_by('-date_added')
            })
        if value == '100':
            return render(request, 'market/index.html', {
                'items': Item.objects.filter(power__mte=100).order_by('-date_added')
            })
        if value == '-30000':
            return render(request, 'market/index.html', {
                'items': Item.objects.filter(price__lte=30000).order_by('-date_added')
            })
        if value == '30000':
            return render(request, 'market/index.html', {
                'items': Item.objects.filter(price__mte=30000).order_by('-date_added')
            })
        if value == '0':
            return render(request, 'market/index.html', {
                'items': Item.objects.filter(choosen_offer=None).order_by('-date_added')
            })
    return HttpResponseRedirect(reverse('index'))

def index_view(request):
    if request.user.role == 'custome' or not request.user.approved:
        messages.warning(request, 'Вы не можете просматривать другие заявки')
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        pass
    return render(request, 'market/index.html', {
        'items': Item.objects.filter(choosen_offer=None).order_by('-date_added')
    })

def load_contract(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    formset = ImageFormSet(queryset=Images.objects.none())
    if request.method == 'POST':
        contract = get_object_or_404(Contract, contract_id=request.POST.get('contract_id'))
        postForm = PostItemForm()

        return render(request, 'market/new_work.html', {
                'form': postForm,
                'contract_id': contract.contract_id,
                'formset': formset,
                'contract_region': contract.region,
                'contract_locality': contract.locality,
                'contract_file': True,
                'contract_date': contract.contract_date,
                'power': contract.power
            })
    else: return render(request, 'market/new_work.html', {
        'form': postForm,
        'formset': formset
        })





# class IndexView(generic.ListView):
#     template_name = 'market/index.html'
#     context_object_name = 'items'

#     def get_queryset(self):
#         return Item.objects.filter(
#             approved=True,
#             choosen_offer=None
#         ).order_by('-date_added')

def uncontr(request):
    if request.method == 'POST' and request.user.role == 'staff':
        for contractor_id in request.POST.getlist('choosen_contractors[]'):
            # print(request.POST.getlist('choosen_contractors[]'))
            contractor = get_object_or_404(CustomUser, pk=int(contractor_id))
            contractor.approved = True
            contractor.save()
        return HttpResponseRedirect(reverse('market:uncontr'))
    else:
        return render(request, 'market/uncontr.html', {
            'contractors': CustomUser.objects.filter(
                approved=False, role='contractor'
            )
        })

def choose_contractor(request, item_id, offer_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=item_id)
        item.choosen_offer = offer_id
        item.save()

    return HttpResponseRedirect(reverse('market:offer_details', args=(item_id, offer_id, )))

class ContractorsRaiting(generic.ListView):
    template_name = 'market/contractors_raiting.html'
    context_object_name = 'contractors'

    def get_queryset(self):
        return CustomUser.objects.filter(
            role='contractor'
        )

class DetailView(generic.DetailView):
    model = Item
    template_name = 'market/detail.html'

def offer_details_view(request, item_id, offer_id):
    item = get_object_or_404(Item, pk=item_id)
    offer = get_object_or_404(Offer, pk=offer_id)

    if request.method == 'POST':
        if item.choosen_offer:
            offer.reviewed = True
            offer.save()
        else:
            item.choosen_offer = offer_id
            item.save()
        return HttpResponseRedirect(reverse('market:offer_details', args=(item_id, offer_id, )))

    if request.user in [item.owner, offer.owner]:
        return render(request, 'market/offer_details.html', {
            'item': item,
            'offer': offer
        })

    messages.warning(request, 'У вас нет доступа к чужим предложениям')
    return HttpResponseRedirect(reverse('market:details', args=(item.id, )))

def new_offer(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if not request.user.is_authenticated:
        messages.warning(request, 'Вы должны сначало авторизоваться')
        return HttpResponseRedirect(reverse('market:detail', args=(item_id, )))
    if request.user == item.owner:
        messages.warning(request, 'Вы не можете создавать предложения для себя самого')
        return HttpResponseRedirect(reverse('market:detail', args=(item_id, )))
    if request.method == 'POST':
        price = request.POST['price']
        desc = request.POST['description']

        offer = Offer(owner=request.user, item=Item.objects.get(id=item_id), price=price, desc=desc)
        offer.save()

        return HttpResponseRedirect(reverse('market:detail', args=(item.id, )))

    else:
        return render(request, 'market/new_offer.html', {
                'item': item,
        })


def new_work(request):
    if request.user.role == 'contractor':
        messages.warning(request, 'Вы не можете создавать работы, если вы являетесь подрядчиком')
        return HttpResponseRedirect(reverse('market:index'))
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    if request.method == 'POST':
        postForm = PostItemForm(request.POST)
        formset = ImageFormSet(
            request.POST,
            request.FILES,
            queryset=Images.objects.none()
        )
        if postForm.is_valid() and formset.is_valid():
            post = postForm.save(commit=False)
            post.owner = request.user
            post.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(
                        item=post,
                        image=image
                        )
                    photo.save()

            return HttpResponseRedirect(reverse('market:detail', args=(post.id, )))
        else:
            messages.error(request, 'Неправильно заполнены поля, попробуйте ещё раз')
    else:
        postForm = PostItemForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'market/new_work.html', {
        'form': postForm,
        'formset': formset
        })
    """
    Тут сделать вход данных
    """

def work_done_custome(request, item_id, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)

    offer.work_done_custome = True
    offer.save()
    return HttpResponseRedirect(reverse('market:offer_details', args=(item_id, offer_id, )))

def work_done_contractor(request, item_id, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)

    offer.work_done_contractor = True
    offer.save()
    return HttpResponseRedirect(reverse('market:offer_details', args=(item_id, offer_id, )))

def review(request, item_id, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)

    offer.review = request.POST.get('review')
    offer.raiting = int(request.POST.get('raiting'))
    offer.save()
    return HttpResponseRedirect(reverse('market:offer_details', args=(item_id, offer_id, )))

def contractor_review(request, item_id, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)

    offer.contractor_review = request.POST.get('contractor_review')
    offer.save()
    return HttpResponseRedirect(reverse('market:offer_details', args=(item_id, offer_id, )))