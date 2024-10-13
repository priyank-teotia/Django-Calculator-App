from django.shortcuts import render



# Create your views here.
def index(request):
  if request.method=="POST":
    num1=request.POST.get('first_number')
    num2=request.POST.get('second_number')
    operation=request.POST.get('operation')
    if operation is not None:
      num1=int(num1)
      num2=int(num2)
    if operation=="add":
      answer=num1+num2
    elif operation=="subtract":
      answer=num1-num2
    elif operation=="multiply":
      answer=num1*num2
    else:
      if num2!=0:
        answer=num1/num2
      else:
        answer="infinite"
    return render(request,'index.html',{'answer':answer})
  return render(request,'index.html')

