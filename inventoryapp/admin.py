from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "EmpID",
        "view_full_name",
        "EmailAddress",
        "DepartmentID",
        "UserName",
        "Password",
        "view_update_date",
    )

    search_fields = (
        "EmpID",
        "FirstName",
        "LastName",
    )

    list_filter = [
        "CreatedAt",
        "UpdatedAt",
        "Status"
    ]

    fieldsets = (
        ("ข้อมูลทั่วไป", {
            "fields": (
                "EmpID",
                ("FirstName", "LastName",),)
        }),
        ("รายละเอียดเพิ่มเติม", {
            "fields": (
                ("UserName","Password",),
                "EmailAddress",
                "DepartmentID",
                "EmpFormulaID",
                "Status",
                ),
        }),
    )

    def view_full_name(self, obj):
        return f'{obj.FirstName} {obj.LastName}'
    
    def view_create_date(self, obj):
        if obj.CreatedAt:
            return obj.CreatedAt.strftime("%d/%m/%Y %H:%M:%S")
            
        return None
    
    empty_value_display = "-"
    def view_update_date(self, obj):
        if obj.UpdatedAt:
            return obj.UpdatedAt.strftime("%d/%m/%Y %H:%M:%S")
        
        return None
    
    list_per_page = 24
    view_create_date.__name__ = "วันที่บันทึก"
    view_update_date.__name__ = "แก้ไขเมื่อ"
    view_full_name.__name__ = 'ชื่อ-นามสกุล'
    pass

admin.site.register(Employee, EmployeeAdmin)