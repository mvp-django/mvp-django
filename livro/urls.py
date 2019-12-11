from django.urls import path
from . import views
from bibliotecapp.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload_livro'),
    path('update/<int:livro_id>', views.update_livro, name = 'update_livro'),
    path('delete/<int:livro_id>', views.delete_livro, name = 'delete_livro'),
    path('download/<int:livro_id>', views.download, name = 'download_livro'),

    
]
#DataFlair
# if DEBUG:
urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    
