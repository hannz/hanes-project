from django.contrib import admin

# Register your models here.
from hanes_project_app.models import Add_Post_Details
from hanes_project_app.models import Menu_Category
from hanes_project_app.models import Sub_Category
from hanes_project_app.models import Region
from hanes_project_app.models import Post_Images

class Menu_CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Menu_Category, Menu_CategoryAdmin)


class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ('menu_category','sub_category')
    pass

admin.site.register(Sub_Category, Sub_CategoryAdmin)
class RegionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Region, RegionAdmin)


class Add_Post_DetailsAdmin(admin.ModelAdmin):
    list_display = ('title','description','menu_category','sub_category','region','name','contact','tel','company_name','set_timer','post_time')
    pass

admin.site.register(Add_Post_Details, Add_Post_DetailsAdmin)


class Post_ImagesAdmin(admin.ModelAdmin):
    list_display = ('post','post_image')
    pass

admin.site.register(Post_Images, Post_ImagesAdmin)
