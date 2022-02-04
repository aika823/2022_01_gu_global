from django.shortcuts import render

def notice(request):
  return render(request, "notice.html")


def certification(request):
  return render(request, "certification.html")


def download(request):
  return render(request, "download.html")


def video(request):
  return render(request, "video.html")


def contact(request):
  return render(request, "contact.html")