from django.shortcuts import render

# Create your views here.
def link1(request):
    return render(request,'happy.html')

def star(request):
    num = int(request.GET['num'])
    li = []
    for i in range(num+1):
        li.append(str('* ' * i))
    return render(request,'happy2.html',{'li' : li})

