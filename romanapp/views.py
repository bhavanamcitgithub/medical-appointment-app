from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html',{})





def appointment(request):
    if request.method=="POST":
        
        first_Name = request.POST['first-Name']
        last_Name =request.POST['last-Name']
        select_Services = request.POST['select-Services']
        your_Phone = request.POST['your-Phone']
        your_Date = request.POST['your-Date']
        your_Time = request.POST['your-Time']
        your_Message = request.POST['your-Message']

       
    

        return render(request,'appointment.html',{
            'your_Message':your_Message,
            'your_Time': your_Time,
            'your_Date':your_Date,
            'your_Phone':your_Phone,
            'select_Services':select_Services,
            'last_Name':last_Name,
            'first_Name':first_Name
                
        })
    
    else:
        return render(request,'home.html',{})