from django.db import models

STATUS_CHOICES = (
    (0, 'Step 0'),
    (1, 'Step 1'),
    (2, 'Step 2'),
    (3, 'Step 3'),
    (4, 'Step 4'),
    (5, 'Complete'),
)

# Create your models here.
class BudgetTypeBVS(models.Model):
    ID = models.BigAutoField(primary_key=True, verbose_name="ลำดับที่", db_column='id',
                             editable=False)  # id int IDENTITY(1,1) NOT NULL,
    Code = models.CharField(max_length=50, verbose_name="รหัส",
                            db_column='bt_code')  # bt_code nvarchar(50) COLLATE Thai_CI_AS NULL,
    Description = models.CharField(max_length=50, verbose_name="รายละเอียด",
                                   db_column='bt_name')  # bt_name nvarchar(50) COLLATE Thai_CI_AS NULL,
    Status = models.IntegerField(verbose_name="สถานะ", db_column="bt_status")  # bt_status int NULL,
    BgID = models.CharField(max_length=50, verbose_name="BG ID", db_column="bg_id")  # bg_id int NULL,
    BnID = models.CharField(max_length=50, verbose_name="BN ID", db_column="bn_id")  # bn_id int NULL,
    CreatedAt = models.DateField(verbose_name="Add Date", db_column="ADDDATE",
                                 auto_now_add=True)  # ADDDATE datetime NULL,

    def __str__(self) -> str:
        return f"{self.Description}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "Budget_type"
        app_label = "budgetbvs"
        verbose_name = "ข้อมูล Budget Type"
        verbose_name_plural = "Budget Type"


class BudgetBVS(models.Model):
    ID = models.BigAutoField(primary_key=True, verbose_name="ลำดับที่", db_column='id',
                             editable=False)  # id int IDENTITY(1,1) NOT NULL,
    BudgetNo = models.CharField(max_length=50, verbose_name="เลขที่เอกสาร",
                                db_column='bu_no')  # bu_no nvarchar(50) COLLATE Thai_CI_AS NULL,
    BudgetDescription = models.CharField(max_length=50, verbose_name="รายละเอียด",
                                         db_column='bu_desc')  # bu_desc nvarchar(50) COLLATE Thai_CI_AS NULL,
    Price = models.FloatField(verbose_name="ราคา", db_column='bu_price')  # bu_price numeric(18,2) NULL,
    DueDate = models.DateField(verbose_name="วันที่จ่าย", db_column="ddate")  # ddate date NULL,
    Status = models.IntegerField(verbose_name="สถานะ", db_column="status")  # status int NULL,
    DepartmentID = models.CharField(max_length=50, verbose_name="แผนก",
                                    db_column="dept_id")  # dept_id nvarchar(50) COLLATE Thai_CI_AS NULL,
    BtID = models.ForeignKey(BudgetTypeBVS, verbose_name="ประเภท", db_column='bt_id',
                             on_delete=models.CASCADE)  # bt_id nvarchar(50) COLLATE Thai_CI_AS NULL,
    TypeIncome = models.IntegerField(verbose_name="ประเภทการรับ", db_column="type_income")  # type_income int NULL,
    CreatedAt = models.DateTimeField(verbose_name="Add Date", db_column="ADDDATE",
                                     auto_now_add=True)  # ADDDATE datetime NULL,

    def __str__(self) -> str:
        return str(self.ID)

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "Budget"
        app_label = "budgetbvs"
        verbose_name = "ข้อมูล Budget"
        verbose_name_plural = "Budget"


class EmployeeBVS(models.Model):
    ID = models.BigAutoField(primary_key=True, verbose_name="ลำดับที่", db_column='id',
                             editable=False)  # id int IDENTITY(1,1) NOT NULL,
    EmpID = models.CharField(max_length=50, verbose_name="รหัสพนักงาน",
                             db_column='emp_id')  # emp_id varchar(50) COLLATE Thai_CI_AS NULL,
    FirstName = models.CharField(max_length=50, verbose_name="ชื่อ",
                                 db_column='emp_name')  # emp_name varchar(150) COLLATE Thai_CI_AS NULL,
    LastName = models.CharField(max_length=50, verbose_name="นาสกุล",
                                db_column='emp_surname')  # emp_surname varchar(150) COLLATE Thai_CI_AS NULL,
    DepartmentID = models.CharField(max_length=50, verbose_name="แผนก/ฝ่าย",
                                    db_column='emp_dept')  # emp_dept varchar(50) COLLATE Thai_CI_AS NULL,
    UserName = models.CharField(max_length=50, verbose_name="ชื่อผู้ใช้งาน",
                                db_column='emp_user')  # emp_user varchar(50) COLLATE Thai_CI_AS NULL,
    Password = models.CharField(max_length=50, verbose_name="รหัสผ่าน",
                                db_column='emp_pass')  # emp_pass varchar(50) COLLATE Thai_CI_AS NULL,
    Status = models.IntegerField(verbose_name="สถานะ", db_column="emp_status")  # emp_status int DEFAULT 0 NULL,
    CreatedByID = models.CharField(max_length=50, verbose_name="รหัสพนักงานที่ทำการบันทึก",
                                   db_column='emp_createby')  # emp_createby varchar(50) COLLATE Thai_CI_AS NULL,
    CreatedAt = models.DateTimeField(verbose_name="บันทึกเมื่อ", db_column="emp_createdate",
                                     auto_now_add=True)  # emp_createdate datetime NULL,
    UpdatedByID = models.CharField(max_length=50, verbose_name="รหัสพนักงานที่อัพเดท",
                                   db_column='emp_updateby')  # emp_updateby varchar(50) COLLATE Thai_CI_AS NULL,
    UpdatedAt = models.DateTimeField(verbose_name="แก้ไข", db_column="emp_updatedate",
                                     auto_now=True)  # emp_updatedate datetime NULL,
    EmailAddress = models.CharField(max_length=50, verbose_name="ที่อยู่ E-Mail",
                                    db_column='emp_email')  # emp_email varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,

    # EmpFormulaID=models.CharField(max_length=50, verbose_name="Formula Emp ID", db_column='FCSKID_EMP_FM', blank=True, null=True)# FCSKID_EMP_FM nvarchar(50) COLLATE Thai_CI_AS NULL,
    def __str__(self) -> str:
        return f"{self.ID}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "Employee"
        app_label = "budgetbvs"
        verbose_name = "ข้อมูล Employee"
        verbose_name_plural = "Employee"


class RTApproveBVS(models.Model):
    ID = models.BigAutoField(primary_key=True, verbose_name="ลำดับที่", db_column='id',
                             editable=False)  # id int IDENTITY(1,1) NOT NULL,
    DepartmentID = models.CharField(max_length=50, verbose_name="แผนก/ฝ่าย",
                                    db_column='dept_id')  # dept_id varchar(50) COLLATE Thai_CI_AS NULL,
    Step = models.IntegerField(verbose_name="ลำดับที่", db_column="step")  # step int NULL,
    Email = models.CharField(max_length=50, verbose_name="ที่อยู่ E-Mail",
                             db_column='email')  # email nvarchar(MAX) COLLATE Thai_CI_AS NULL,
    ApproveName = models.CharField(max_length=250, verbose_name="ชื่อผู้อนุมัติ",
                                   db_column='appr_name')  # appr_name nvarchar(MAX) COLLATE Thai_CI_AS NULL,
    ImageSignal = models.CharField(max_length=250, verbose_name="ลายเซ็นต์",
                                   db_column='image_sig')  # image_sig nvarchar(MAX) COLLATE Thai_CI_AS NULL,
    FType = models.IntegerField(verbose_name="FType", db_column="ftype", null=True,
                                default=0)  # ftype int DEFAULT 0 NOT NULL,

    # BgAmount=models.DecimalField(decimal_places=4, max_digits=4, verbose_name="จำนวน", db_column='bg_amount', null=True,default=0)# bg_amount numeric(18,4) NULL,
    # Position=models.CharField(max_length=250, verbose_name="ตำแหน่ง", db_column='position', null=True, blank=True)# position nvarchar(MAX) COLLATE Thai_CI_AS NULL

    def __str__(self) -> str:
        return f"{self.ID}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "RT_APPROVE"
        app_label = "budgetbvs"
        verbose_name = "ข้อมูล RT Approve"
        verbose_name_plural = "RT Approve"


class PRHeadBVS(models.Model):
    # FCDATASER char(4) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    ID = models.CharField(primary_key=True, max_length=8, db_column='FCSKID', editable=False)
    FDDate = models.DateField(verbose_name="วันที่", db_column="FDDATE")
    CreateAt = models.DateTimeField(verbose_name="วันที่บันทึก", db_column="FDRECEDATE", auto_now_add=True)
    RefNo=models.CharField(max_length=35, verbose_name="เลขที่เอกสาร", db_column='FCREFNO')
    Amt = models.FloatField(verbose_name="จำนวน", db_column="FNAMT")
    FCCREATEBY = models.CharField(max_length=8,verbose_name="รหัสพนักงาน", db_column="FCCREATEBY")
    LastUpdated = models.DateTimeField(verbose_name="อัพเดทล่าสุด", db_column="FTLASTUPD", auto_now=True)
    # StatusApp = models.IntegerField(verbose_name="ขั้นตอนที่", db_column="STATUS_APP")# STATUS_APP int DEFAULT 0 NOT NULL,
    StatusApp = models.IntegerField(verbose_name="ขั้นตอนที่", db_column="STATUS_APP", choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return f"{self.ID}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "PR_H"
        app_label = "budgetbvs"
        verbose_name = "ข้อมูล Purchase"
        verbose_name_plural = "Purchase"


class LogStepSendMailBVS(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int IDENTITY(1,1) NOT NULL,
    RefNo=models.CharField(max_length=50, verbose_name="เลขที่เอกสาร", db_column='FCREFNO')#FCREFNO nvarchar(50) COLLATE Thai_CI_AS NULL,
    ApproveID=models.CharField(max_length=50, verbose_name="เลขที่การอนุมัติ", db_column='APPROVE_ID')#APPROVE_ID nvarchar(50) COLLATE Thai_CI_AS NULL,
    StepID=models.CharField(max_length=50, verbose_name="ลำดับที่", db_column='step_id')#step_id nvarchar(50) COLLATE Thai_CI_AS NULL,
    ApproveComment=models.CharField(max_length=255, verbose_name="ข้อเสนอแนะ", db_column='APPROVE_comment', null=True, blank=True)#APPROVE_comment nvarchar(255) COLLATE Thai_CI_AS NULL,
    CreatedAt=models.DateTimeField(verbose_name="วันที่บันทึก", db_column="create_date", auto_now_add=True)#create_date datetime DEFAULT getdate() NULL,
    Remark=models.TextField(verbose_name="หมายเหตุ", db_column='REMARK', null=True, blank=True)#REMARK text COLLATE Thai_CI_AS DEFAULT NULL NULL,
    BookID=models.CharField(max_length=50, verbose_name="เลขที่เล่ม", db_column='FCBOOK')#FCBOOK varchar(50) COLLATE Thai_CI_AS NULL

    def __str__(self) -> str:
        return f"{self.RefNo}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "log_step_sendmail"
        app_label = "budgetbvs"
        verbose_name = "ข้อมูล Step SendMail"
        verbose_name_plural = "Step SendMail"