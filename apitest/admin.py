from django.contrib import admin
from apitest.models import ApiTest, ApiStep, Apis


class ApiStepAdmin(admin.TabularInline):
    list_display = ["api_name", "api_url", "api_param_value", "api_method",
                    "api_result", "api_status", "create_time", "id", "api_test"]
    model = ApiStep
    extra = 1


class ApiTestAdmin(admin.ModelAdmin):
    list_display = ["apitest_name", "apitester", "apitest_result", "create_time", "id"]
    inlines = [ApiStepAdmin]


class ApisAdmin(admin.TabularInline):
    list_display = ["api_name", "api_url", "api_param_value", "api_method",
                    "api_result", "api_status", "create_time", "id", "product"]


admin.site.register(ApiTest, ApiTestAdmin)
admin.site.register(Apis)