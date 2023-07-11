from datetime import datetime
from django.contrib import admin
from .models import BudgetAAA, EmployeeAAA,RTApproveAAA

class StatusAdmin(admin.ModelAdmin):
    pass

class BudgetTypeAdmin(admin.ModelAdmin):
    pass

class BudgetAdmin(admin.ModelAdmin):
    search_fields = (
        "BudgetNo",
        "BudgetDescription"
    )

    list_filter = [
        "DueDate",
        "CreatedAt",
        "Status"
    ]

    list_display = (
        # "ID",
        "BudgetNo",
        "BudgetDescription",
        "view_due_date",
        "view_price",
        "BtID",
        "Status",
        "view_create_date",
    )

    fieldsets = (
        ("ข้อมูลทั่วไป", {
            "fields": (
                ("BudgetNo",
                "BudgetDescription",),)
        }),
        ("รายละเอียดเพิ่มเติม", {
            "fields": (
                ("DueDate","Price",),
                ("DepartmentID","BtID",),
                "Status",
                ),
        }),
    )

    ordering = ("DueDate","BudgetNo", )
    def get_readonly_fields(self, request, obj=None):
        dte = datetime.now()
        read_only = ('BudgetNo','BudgetDescription', 'DueDate')

        if int(obj.DueDate.strftime("%Y")) >= int(dte.strftime("%Y")) and int(obj.DueDate.strftime("%m")) >= int(dte.strftime("%m")):
            return read_only
        
        return read_only + ('Price', "DepartmentID","BtID","Status",)

    # date_hierarchy = "CreatedAt"
    empty_value_display = "-"
    # @admin.display(empty_value="???")
    def view_create_date(self, obj):
        if obj.CreatedAt:
            return obj.CreatedAt.strftime("%d/%m/%Y %H:%M:%S")
        
        return None
    
    def view_price(self, obj):
        return f'{obj.Price:,}'
    
    def view_due_date(self, obj):
        return obj.DueDate.strftime("%d/%m/%Y")
    
    view_price.__name__ = 'ราคา'
    view_due_date.__name__ = 'วันที่จ่าย'
    view_create_date.__name__ = "วันที่บันทึก"
    list_per_page = 12
    pass

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
                # "EmpFormulaID",
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
    
    view_create_date.__name__ = "วันที่บันทึก"
    view_update_date.__name__ = "แก้ไขเมื่อ"
    view_full_name.__name__ = 'ชื่อ-นามสกุล'
    pass

class RTApproveAdmin(admin.ModelAdmin):
    list_display = (
        "DepartmentID",
        "Step",
        "Email",
        "ApproveName",
        "ImageSignal",
    )

    search_fields = (
        "Email",
        "ApproveName",
        "ImageSignal",
    )

    list_filter = [
        "DepartmentID",
        "Step",
        "FType",
        # "BgAmount",
        # "Position",
    ]

    fields = (
        "DepartmentID",
        "Step",
        "Email",
        "ApproveName",
        "ImageSignal",
    )
    pass

# Register your models here.
# admin.site.register(BudgetType, BudgetTypeAdmin)
# admin.site.register(Status, StatusAdmin)
admin.site.register(BudgetAAA, BudgetAdmin)
admin.site.register(EmployeeAAA, EmployeeAdmin)
admin.site.register(RTApproveAAA, RTApproveAdmin)