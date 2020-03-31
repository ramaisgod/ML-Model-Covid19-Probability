from django.shortcuts import render
from .forms import TestForm
import pickle


def corona_test(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if 'btn_reset' in request.POST:
            form = TestForm()
            return render(request, 'index.html', {'form': form})
        if form.is_valid():
            age = form.cleaned_data['age']
            fever = form.cleaned_data['fever']
            body_pain = form.cleaned_data['body_pain']
            runny_nose = form.cleaned_data['runny_nose']
            diff_breathing = form.cleaned_data['diff_breathing']
            travel_history = form.cleaned_data['travel_history']
            # Open Pickle file
            file = open("model.pkl", "rb")
            # Load pickle
            clf = pickle.load(file)
            file.close()
            inputFeatures = [fever, int(body_pain), int(age), int(runny_nose), int(diff_breathing), int(travel_history)]
            print(inputFeatures)
            infProb = clf.predict_proba([inputFeatures])
            infProb = "%.2f" % (infProb[0][1] * 100)
            # print(infProb)
            return render(request, 'index.html', {'form': form, 'infProb': infProb})
    return render(request, 'index.html', {'form': form})
