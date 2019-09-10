from django.shortcuts import render, get_object_or_404, redirect
from .forms import FamilyMemberFormSet, ProfileForm, LanguageModelFormset, LanguageInlineFormset, ProgrammerForm, LanguageFormset
from .models import Profile, Programmer, Language

def profile_list(request):
    profiles = Profile.objects.all()
    template_name = 'core/profile-list.html'
    context = {'profiles': profiles}
    return render(request, template_name, context)

def profile_edit(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    if request.method == 'POST':
        form = FamilyMemberFormSet(request.POST, instance=profile)
    else:
        form = FamilyMemberFormSet(instance=profile)

    template_name = ''
    context = {

    }

    return render(request, template_name, context)

def profile_create(request):
    if request.method == 'POST':
        family_member_form = FamilyMemberFormSet(request.POST)
        profile_form = ProfileForm(request.POST)

        if family_member_form.is_valid() & profile_form.is_valid():
            pass
    else:
        family_member_form = FamilyMemberFormSet()
        profile_form = ProfileForm()

    template_name = 'core/profile-create.html'
    context = {
        'family_member_form': family_member_form,
        'profile_form': profile_form
    }

    return render(request, template_name, context)

def programmer_list(request):
    programmers = Programmer.objects.all()
    template_name = 'core/programmer/programmer-list.html'
    context ={
        'programmers': programmers
    }
    return render(request, template_name, context)

def programmer_create(request):
    if request.method == 'POST':
        programmer_form = ProgrammerForm(request.POST)
        formset = LanguageFormset(request.POST)
        if programmer_form.is_valid() and formset.is_valid():
            programmer = programmer_form.save()
            # print(programmer)
            for form in formset:
                name = form.cleaned_data.get('name')
                if name:
                    Language(name=name, programmer=programmer).save()

            # return redirect('programmer_create')
            return redirect('programmer_update', programmer_id=programmer.id)
    else:
        programmer_form = ProgrammerForm()
        formset = LanguageFormset()
    template_name = 'core/programmer/programmer-create.html'
    context = {
        'formset': formset,
        'programmer_form': programmer_form
    }
    return render(request, template_name, context)

def programmer_update(request, programmer_id):
    programmer = get_object_or_404(Programmer, id=programmer_id)

    if request.method == 'POST':
        # formset = LanguageModelFormset(request.POST, queryset=Language.objects.filter(programmer=programmer))
        formset = LanguageInlineFormset(request.POST, instance=programmer)
        programmer_form = ProgrammerForm(request.POST, instance=programmer)
        if formset.is_valid() and programmer_form.is_valid():
            # instances = formset.save(commit=False)
            # for instance in instances:
            #     instance.programmer = programmer
            #     instance.save()
            programmer_form.save()
            formset.save()

            return redirect('programmer_update', programmer_id=programmer.id)
    else:
        # formset = LanguageModelFormset(queryset=Language.objects.filter(programmer=programmer))
        formset = LanguageInlineFormset(instance=programmer)
        programmer_form = ProgrammerForm(instance=programmer)

    template_name = 'core/programmer/programmer-update.html'
    context = {
        'formset': formset,
        'programmer_form': programmer_form
    }
    return render(request, template_name, context)