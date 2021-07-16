from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):

    return render(request, 'index.html')


def analyze(request):
    """Get and analyse this text"""
    djtext = request.POST.get('textarea')
    djremovepunc = request.POST.get('removepunc', 'off')
    djallupper = request.POST.get('uppercase', 'off')
    djcount = request.POST.get('count', 'off')
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed = djtext
    purpose = ""
    if djallupper == 'on':
        purpose += "| UPPERCASE"
        analyzed = djtext.upper()
    if djremovepunc == 'on':
        djtext = analyzed
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed += char
        purpose += "| Remove Punctuations"

    if djcount == 'on':
        purpose += "| Count Characters"
        analyzed += str(f" \n\nNo. of characters: => {len(analyzed)}")

    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
