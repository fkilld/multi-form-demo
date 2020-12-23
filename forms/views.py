from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from forms.models import MultiStepFormModel


def multistepformexample(request):
    return render(request, "multistepformexample.html")


def multistepformexample_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("multistepformexample"))
    else:
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone = request.POST.get("phone")
        twitter = request.POST.get("twitter")
        facebook = request.POST.get("facebook")
        gplus = request.POST.get("gplus")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        cpass = request.POST.get("cpass")
        if password != cpass:
            messages.error(request, "Confirm Password Doesn't Match")
            return HttpResponseRedirect(reverse('multistepformexample'))

        try:
            multistepform = MultiStepFormModel(fname=fname, lname=lname, phone=phone, twitter=twitter,
                                               facebook=facebook, gplus=gplus, email=email, password=password)
            multistepform.save()
            messages.success(request, "Data Save Successfully")
            return HttpResponseRedirect(reverse('multistepformexample'))
        except:
            messages.error(request, "Error in Saving Data")
            return HttpResponseRedirect(reverse('multistepformexample'))

# def multipleUpload(request):
#     return render(request, "multiple_fileupload.html")
#
#
# def multipleupload_save(request):
#     name = request.POST.get("name")
#     desc = request.POST.get("desc")
#     images = request.FILES.getlist("file[]")
#     print(images)
#     product = Products(name=name, desc=desc)
#     product.save()
#
#     for img in images:
#         fs = FileSystemStorage()
#         file_path = fs.save(img.name, img)
#
#         pimage = ProductImages(product_id=product, image=file_path)
#         pimage.save()
#
#     return HttpResponse("File Uploaded")
