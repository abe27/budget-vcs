from datetime import datetime
from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import BudgetBVS, EmployeeBVS,RTApproveBVS,LogStepSendMailBVS, PRHeadBVS

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
        # "DepartmentID",
        "BtID",
        # "TypeIncome",
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

    # exclude=("headline ",)
    # readonly_fields=('BudgetNo','BudgetDescription', 'DueDate',)
    ordering = ("BudgetNo", "DueDate",)
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

class LogStepSendMailBVSAdmin(admin.ModelAdmin):
    change_form_template = "budget/change_form.html"

    search_fields = (
        "RefNo",
    )

    list_filter = (
        "StepID",
        "CreatedAt",
    )

    list_display = (
            "RefNo",
            "ApproveID",
            "ApproveComment",
            "StepID",
            "Remark",
            # "BookID",
            "view_create_date",
            )
    
    fields = (
        "RefNo",
        "ApproveID",
        "ApproveComment",
        "StepID",
        "Remark",
    )

    def view_create_date(self, obj):
        if obj.CreatedAt:
            return obj.CreatedAt.strftime("%d/%m/%Y %H:%M:%S")
            
        return None
    
    def response_change(self, request, object):
        if "_resend-mail" in request.POST:
            stepTotal = int(object.StepID) - 1
            prHead = PRHeadBVS.objects.get(RefNo=object.RefNo)
            prHead.StatusApp = stepTotal
            prHead.save()
            # if stepTotal == 0:
            #     LogStepSendMailBVS.objects.filter(RefNo=object.RefNo).delete()
            # else:
            #     LogStepSendMailBVS.objects.filter(
            #         RefNo=object.RefNo, StepID=object.StepID).delete()
            LogStepSendMailBVS.objects.filter(RefNo=object.RefNo, StepID__gte=stepTotal).delete()
            urls = f"http://110.164.218.143:11227/web_sevice_bvs/web_Approve.aspx?EMP_ID={(prHead.FCCREATEBY).strip()}&P={(object.RefNo).strip()}&STEP={stepTotal}&BOOK=1"
            return HttpResponseRedirect(urls)
        
        return super().response_change(request, object)
    
    def has_delete_permission(self, request, obj=None):
        return False


    view_create_date.__name__ = "วันที่บันทึก"
    empty_value_display = "-"
    ordering = ('-CreatedAt','RefNo','StepID',)
    list_per_page = 24
    pass

class PRHeadBVSAdmin(admin.ModelAdmin):
    search_fields = (
        "RefNo",
    )

    list_filter = (
        "FDDate",
        "LastUpdated",
    )
    list_display = (
        "view_create_date",
        "RefNo",
        "Amt",
        "StatusApp",
        "view_last_date",
    )

    def view_create_date(self, obj):
        if obj.FDDate:
            return obj.FDDate.strftime("%d/%m/%Y")
            
        return None
    
    def view_last_date(self, obj):
        if obj.LastUpdated:
            return obj.LastUpdated.strftime("%d/%m/%Y %H:%M:%S")
            
        return None
    
    view_create_date.__name__ = "วันที่"
    view_last_date.__name__ = "แก้ไขล่าสุดเมื่อ"
    empty_value_display = "-"
    ordering = ('-FDDate','RefNo')
    list_per_page = 24
    pass

# Register your models here.
# admin.site.register(BudgetType, BudgetTypeAdmin)
# admin.site.register(Status, StatusAdmin)
admin.site.register(BudgetBVS, BudgetAdmin)
admin.site.register(EmployeeBVS, EmployeeAdmin)
admin.site.register(RTApproveBVS, RTApproveAdmin)
admin.site.register(LogStepSendMailBVS, LogStepSendMailBVSAdmin)
admin.site.register(PRHeadBVS, PRHeadBVSAdmin)