# Weather Api 🌥️
### Description
In this mini project, we are going through the basics of django,a **_full stack_** framework of Python that can help us create from websites , to simple and complicated applications.Here we use also openweather api for the implementation

### Required:
To make this little project become reality,you need to:
1. Download [Django](https://www.programink.com/django-tutorial/django-download-install.html).
2. Sign up in [openweather Api](https://openweathermap.org/),in order to get a key via email.

### Folders 📁
- main 
> This is the name of the app and also where the most of things that used for controlling it take >place

- static/main
> This is the folder where every css file will be storaged.In the meanwhile it is better 
> to keep the in one file for a better organisation.Also is a static file,meaning that we must 
> every file in a specific way with the directory of the html file,not just the traditional way

- templates
> This folder keeps the html file that will be rendered in views.py

### Implementation 🧰
#### testsite
- settings.py 🛠️
1. First in installed apps add '~~nameofyourapp~~.apps.MainConfig'
>Mine is main
2. Create STATICFILES_DIRS ,that will connect the static files with the BASE_DIR.But that's not enough

- urls.py 🔗 <br>
The `urlpatterns` list routes URLs to views
1. Import include, path from django.urls
2. import settings from django.conf
3. Import static from django.conf.urls.static
4. Add `+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)` next to 'urlpatterns' list
5. Append to the list the path that to the views.py that is goinf to render your website, with functions or classes, is your choice.

