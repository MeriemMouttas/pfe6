from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        print(modulename)
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "myAdmin.views":
                    pass
                elif modulename == "mySite.views" or modulename == "django.views.static":
                    pass
                elif modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites":
                    pass
                else:
                    return HttpResponseRedirect(reverse("profil"))
            elif user.user_type == "2":
                if modulename == "mySite.views" or modulename == "mySite.EditResultVIewClass":
                    pass
                elif modulename == "mySite.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("client_profil"))
            elif user.user_type == "3":
                if modulename == "fournisseur.views" or modulename == "django.views.static":
                    pass
                elif modulename == "mySite.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("createproduit"))
            else:
                return HttpResponseRedirect(reverse("show_login"))

        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login") or modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites" or modulename=="mySite.views":
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))