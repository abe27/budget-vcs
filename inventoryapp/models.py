from django.db import models

# Create your models here.
class Employee(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int IDENTITY(1,1) NOT NULL,
    EmpID=models.CharField(max_length=50, verbose_name="รหัสพนักงาน", db_column='emp_id')# emp_id varchar(50) COLLATE Thai_CI_AS NULL,
    FirstName=models.CharField(max_length=50, verbose_name="ชื่อ", db_column='emp_name')# emp_name varchar(150) COLLATE Thai_CI_AS NULL,
    LastName=models.CharField(max_length=50, verbose_name="นาสกุล", db_column='emp_surname')# emp_surname varchar(150) COLLATE Thai_CI_AS NULL,
    DepartmentID=models.CharField(max_length=50, verbose_name="แผนก/ฝ่าย", db_column='emp_dept')# emp_dept varchar(50) COLLATE Thai_CI_AS NULL,
    UserName=models.CharField(max_length=50, verbose_name="ชื่อผู้ใช้งาน", db_column='emp_user')# emp_user varchar(50) COLLATE Thai_CI_AS NULL,
    Password=models.CharField(max_length=50, verbose_name="รหัสผ่าน", db_column='emp_pass')# emp_pass varchar(50) COLLATE Thai_CI_AS NULL,
    Status=models.IntegerField(verbose_name="สถานะ", db_column="emp_status")# emp_status int DEFAULT 0 NULL,
    CreatedByID=models.CharField(max_length=50, verbose_name="รหัสพนักงานที่ทำการบันทึก", db_column='emp_createby')# emp_createby varchar(50) COLLATE Thai_CI_AS NULL,
    CreatedAt=models.DateTimeField(verbose_name="บันทึกเมื่อ", db_column="emp_createdate", auto_now_add=True)# emp_createdate datetime NULL,
    UpdatedByID=models.CharField(max_length=50, verbose_name="รหัสพนักงานที่อัพเดท", db_column='emp_updateby')# emp_updateby varchar(50) COLLATE Thai_CI_AS NULL,
    UpdatedAt=models.DateTimeField(verbose_name="แก้ไข", db_column="emp_updatedate", auto_now=True)# emp_updatedate datetime NULL,
    EmailAddress=models.CharField(max_length=50, verbose_name="ที่อยู่ E-Mail", db_column='emp_email')# emp_email varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    EmpFormulaID=models.CharField(max_length=50, verbose_name="Formula Emp ID", db_column='FCSKID_EMP_FM', blank=True, null=True)# FCSKID_EMP_FM nvarchar(50) COLLATE Thai_CI_AS NULL,
    def __str__(self) -> str:
        return f"{self.ID}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "Employee"
        app_label = "inventoryapp"
        verbose_name = "ข้อมูล Employee"
        verbose_name_plural = "Employee"