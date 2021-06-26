from django.urls import path
from . import views
urlpatterns = [
  #admin route #
    path('profil/',views.index,name='profil'),
    path('listeFournisseur/',views.listeFournisseur,name='listeFournisseur'),
     
    #categorie#
    path('createCategories/',views.CreateCategories.as_view(),name='createcategories'),
    path('listecategories/',views.categories,name='categories'),
     path('updateCategories/<int:id>/',views.CategorietUpdateView.as_view(), name="updateCategories"),
     path('updateCategories/<int:id>/listecategories',views.categories,name='categories'),
    #sous categories#
    path('souscreateCategories/',views.CreateSousCategories.as_view(),name='souscreatecategories'),
    path('souscreateCategories/<int:id>',views.souscategories,name='souscategories'),
    path('souscreateCategories/<int:id>/souscategories',views.detailsouscategorie,name='souscategoriesliste'),
    #article#
    path('listearticles/',views.articles,name='articles'),
    path('createarticle/',views.CreateArticles.as_view(),name='createarticle'),
    path('createarticle/articles',views.articles,name='articles'),
    path('detailarticle/<int:pk>/',views.Articledetail.as_view(), name='detailarticle'),
    path('updateArticles/<int:id>/',views.ArticletUpdateView.as_view(), name="updateArticles"),
    path('updateArticles/<int:id>/listearticles',views.articles,name='articles'),
    #send email#
    path('email/',views.subscribe,name='subscribe'),
    #Apropos
    path('apropos/',views.CreateApropos.as_view(),name='Apropos'),
    path('apropos/profil',views.propos,name='profil'),
    path('update_apropos/<int:id>/', views.AproposUpdateView.as_view(), name="AproposUpdateView"),
    #pub
    path('listePublicite/',views.listepub,name='listepub'),
    path('listePublicite/<int:id>/', views.PubUpdate, name="listePublicite"),
   
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)