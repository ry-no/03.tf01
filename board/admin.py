from re import search
from django.contrib import admin
from .models import  Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'content', 'created_at', 'modified_at') # 리스트에 볼 필드 (모델에서 해당 필드 작성하면됨)
    list_display_links = ('id', 'title', 'author') # 리스트 첫 번째 필드만 클릭할수 있게 링크 제공, id 같은 걸 첫번째에 설정하면 클릭 불편~ 그럴때 사용함
    search_fields = ('title', 'author', 'content') # 검색기능으로 검색원하는 필드를 작성하기만 하면됨 (모델에서 작성된 필드값으로만 ~)
    readonly_fields = ('created_at', 'modified_at') # 
    list_filter = ('author', 'created_at', 'modified_at') # 해당 값에 범위에 해당되는 게시물만 볼수 있게 설정작업
    # list_editable = ('title', 'author') # 리스트 화면에서 필드를 에디팅 할수 있는기능 단!!! list_display_links 와 겹쳐쓰면 안됨
    # ordering = ('author', '-modified_at') # 정렬기능임 ( 관리자창에서 filed명을 클릭하여 사용가능)
    # list_per_page = 30 #


admin.site.register(Article, ArticleAdmin)


# from django.contrib import admin

# from .models import Article


# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'author', 'content', 'created_at', 'modified_at')
#     list_display_links = ('id', 'title', 'author')
#     search_fields = ('title', 'author', 'content')
#     readonly_fields = ('created_at', 'modified_at')
#     list_filter = ('author', 'created_at', 'modified_at')
#     # list_editable = ('title', 'author')
#     # ordering = ('author', '-modified_at')
#     # list_per_page = 30


# admin.site.register(Article, ArticleAdmin)