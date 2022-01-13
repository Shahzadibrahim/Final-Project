from django.contrib import admin

from marketing.models import Origins


class MarketingAdmin(admin.ModelAdmin):
    list_display = ('Origin', 'Color', 'Percentage', 'gender')
    list_filter = ('Color', 'gender', 'Percentage')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'


admin.site.register(Origins, MarketingAdmin)
