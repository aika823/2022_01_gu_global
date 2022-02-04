from django.shortcuts import render

def notice(request):
  return render(request, "notice.html")


def certification(request):
  return render(request, "certification.html")


def download(request):
  return render(request, "support_download.html")


def video(request):
  return render(request, "support_video.html")


def contact(request):
  return render(request, "support_contact.html")