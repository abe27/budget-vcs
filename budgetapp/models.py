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
class BudgetType(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int IDENTITY(1,1) NOT NULL,
    Code=models.CharField(max_length=50, verbose_name="รหัส", db_column='bt_code')# bt_code nvarchar(50) COLLATE Thai_CI_AS NULL,
    Description=models.CharField(max_length=50, verbose_name="รายละเอียด", db_column='bt_name')# bt_name nvarchar(50) COLLATE Thai_CI_AS NULL,
    Status=models.IntegerField(verbose_name="สถานะ", db_column="bt_status")# bt_status int NULL,
    BgID=models.CharField(max_length=50, verbose_name="BG ID", db_column="bg_id")# bg_id int NULL,
    BnID=models.CharField(max_length=50, verbose_name="BN ID", db_column="bn_id")# bn_id int NULL,
    CreatedAt=models.DateField(verbose_name="Add Date", db_column="ADDDATE", auto_now_add=True)# ADDDATE datetime NULL,
    def __str__(self) -> str:
        return f"{self.Description}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "Budget_type"
        app_label = "budgetapp"
        verbose_name = "ข้อมูล Budget Type"
        verbose_name_plural = "Budget Type"

class Status(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int NOT NULL,
    Title=models.CharField(max_length=50, verbose_name="หัวข้อ", db_column='Name_statusPR')# Name_statusPR nvarchar(50) COLLATE Thai_CI_AS NULL

    def __str__(self) -> str:
        return f"{self.Title}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "status_pr"
        app_label = "budgetapp"
        verbose_name = "ข้อมูล Status PR"
        verbose_name_plural = "Status PR"

class Budget(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int IDENTITY(1,1) NOT NULL,
    BudgetNo=models.CharField(max_length=50, verbose_name="เลขที่เอกสาร", db_column='bu_no')# bu_no nvarchar(50) COLLATE Thai_CI_AS NULL,
    BudgetDescription=models.CharField(max_length=50, verbose_name="รายละเอียด", db_column='bu_desc')# bu_desc nvarchar(50) COLLATE Thai_CI_AS NULL,
    Price=models.FloatField(verbose_name="ราคา", db_column='bu_price')# bu_price numeric(18,2) NULL,
    DueDate=models.DateField(verbose_name="วันที่จ่าย", db_column="ddate")# ddate date NULL,
    Status=models.ForeignKey(Status, verbose_name="สถานะ", db_column="status",on_delete=models.CASCADE)# status int NULL,
    DepartmentID=models.CharField(max_length=50, verbose_name="แผนก", db_column="dept_id")# dept_id nvarchar(50) COLLATE Thai_CI_AS NULL,
    BtID=models.ForeignKey(BudgetType, verbose_name="ประเภท", db_column='bt_id', on_delete=models.CASCADE)# bt_id nvarchar(50) COLLATE Thai_CI_AS NULL,
    TypeIncome=models.IntegerField(verbose_name="ประเภทการรับ", db_column="type_income")# type_income int NULL,
    CreatedAt=models.DateTimeField(verbose_name="Add Date", db_column="ADDDATE", auto_now_add=True)# ADDDATE datetime NULL,
    def __str__(self) -> str:
        return str(self.ID)

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "Budget"
        app_label = "budgetapp"
        verbose_name = "ข้อมูล Budget"
        verbose_name_plural = "Budget"

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
        app_label = "budgetapp"
        verbose_name = "ข้อมูล Employee"
        verbose_name_plural = "Employee"


class RTApprove(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="ลำดับที่", db_column='id', editable=False)# id int IDENTITY(1,1) NOT NULL,
    DepartmentID=models.CharField(max_length=50, verbose_name="แผนก/ฝ่าย", db_column='dept_id')# dept_id varchar(50) COLLATE Thai_CI_AS NULL,
    Step=models.IntegerField(verbose_name="ลำดับที่", db_column="step")# step int NULL,
    Email=models.CharField(max_length=50, verbose_name="ที่อยู่ E-Mail", db_column='email')# email nvarchar(MAX) COLLATE Thai_CI_AS NULL,
    ApproveName=models.CharField(max_length=250, verbose_name="ชื่อผู้อนุมัติ", db_column='appr_name')# appr_name nvarchar(MAX) COLLATE Thai_CI_AS NULL,
    ImageSignal=models.CharField(max_length=250, verbose_name="ลายเซ็นต์", db_column='image_sig')# image_sig nvarchar(MAX) COLLATE Thai_CI_AS NULL,
    FType=models.IntegerField(verbose_name="FType", db_column="ftype", null=True, default=0)# ftype int DEFAULT 0 NOT NULL,
    BgAmount=models.DecimalField(decimal_places=4, max_digits=4, verbose_name="จำนวน", db_column='bg_amount', null=True,default=0)# bg_amount numeric(18,4) NULL,
    Position=models.CharField(max_length=250, verbose_name="ตำแหน่ง", db_column='position', null=True, blank=True)# position nvarchar(MAX) COLLATE Thai_CI_AS NULL
        
    def __str__(self) -> str:
        return f"{self.ID}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "RT_APPROVE"
        app_label = "budgetapp"
        verbose_name = "ข้อมูล RT Approve"
        verbose_name_plural = "RT Approve"

class PRHead(models.Model):
    # FCDATASER char(4) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    ID = models.CharField(primary_key=True, max_length=8, db_column='FCSKID', editable=False)## FCSKID char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCUDATE char(2) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCUTIME char(2) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCLUPDAPP char(2) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCRFTYPE char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCREFTYPE char(2) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCORP char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCBRANCH char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDEPT char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCSECT char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCJOB char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCSTAT char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCSTEP char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    FDDate = models.DateField(verbose_name="วันที่", db_column="FDDATE")# FDDATE datetime DEFAULT getdate() NOT NULL,
    # FDDUEDATE datetime DEFAULT NULL NULL,
    CreateAt = models.DateTimeField(verbose_name="วันที่บันทึก", db_column="FDRECEDATE", auto_now_add=True)# FDRECEDATE datetime DEFAULT NULL NULL,
    # FCBOOK char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCODE char(30) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    RefNo=models.CharField(max_length=35, verbose_name="เลขที่เอกสาร", db_column='FCREFNO')# FCREFNO char(35) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNDISCAMT1 decimal(20,4) DEFAULT 0 NOT NULL,
    # FNDISCAMT2 decimal(20,4) DEFAULT 0 NOT NULL,
    # FNDISCAMTI decimal(20,4) DEFAULT 0 NOT NULL,
    # FNDISCPCN1 decimal(12,2) DEFAULT 0 NOT NULL,
    # FNDISCPCN2 decimal(12,2) DEFAULT 0 NOT NULL,
    # FNDISCPCN3 decimal(12,2) DEFAULT 0 NOT NULL,
    Amt = models.FloatField(verbose_name="จำนวน", db_column="FNAMT")# FNAMT decimal(20,4) DEFAULT 0 NOT NULL,
    # FNAMT2 decimal(20,4) DEFAULT 0 NOT NULL,
    # FCVATISOUT char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCVATTYPE char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNVATRATE decimal(10,1) DEFAULT 0 NOT NULL,
    # FNVATAMT decimal(20,4) DEFAULT 0 NOT NULL,
    # FCCOOR char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCEMPL char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCEMZONE char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCISCASH char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNCREDTERM decimal(10,0) DEFAULT 0 NOT NULL,
    FCCREATEBY = models.CharField(max_length=8,verbose_name="รหัสพนักงาน", db_column="FCCREATEBY")# FCCREATEBY char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCORRECTB char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCANCELBY char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCACSTEP char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FMMEMDATA varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FCHASRET char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCVATDUE char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCRECVMAN char(30) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCREATETY char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCEAFTERR char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCSELTAG char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FTDATETIME datetime DEFAULT getdate() NOT NULL,
    # FIMILLISEC int DEFAULT 0 NOT NULL,
    # FCSTEP2 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCPROJ char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDISCSTR char(20) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCURRENCY char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNAMTKE decimal(20,4) DEFAULT 0 NOT NULL,
    # FNVATAMTKE decimal(20,4) DEFAULT 0 NOT NULL,
    # FNDISCAMTK decimal(20,4) DEFAULT 0 NOT NULL,
    # FNXRATE decimal(20,8) DEFAULT 0 NOT NULL,
    # FCFRWHOUSE char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCTOWHOUSE char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCAPPROVEB char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDELICOOR char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FDAPPROVE datetime DEFAULT NULL NULL,
    # FCMSTEP char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCSUBBR char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCPLANT char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    LastUpdated = models.DateTimeField(verbose_name="อัพเดทล่าสุด", db_column="FTLASTUPD", auto_now=True)# FTLASTUPD datetime DEFAULT getdate() NULL,
    # FCPRIORITY char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCHASCHAIN char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCXFERSTEP char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FTXFER datetime DEFAULT NULL NULL,
    # FMMEMDATA2 varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FMMEMDATA3 varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FMMEMDATA4 varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FCSHOWPLED char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCSTEPX1 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FMMEMDATA5 varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FCTRADETRM char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FTLASTEDIT datetime DEFAULT NULL NULL,
    # FCREASONRQ char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCPAYTERM char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FDREQDATE datetime DEFAULT NULL NULL,
    # FCREQMEN char(100) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCREATEAP char(2) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCREQPERSN char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNDAYASSUR decimal(8,0) DEFAULT 0 NOT NULL,
    # FCISPDPART char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCPERSON char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCLINKAPP1 char(12) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCLINKSTP1 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCLINKAPP2 char(12) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCLINKSTP2 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCOUNTER char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCPDBRAND char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCRNGTIME char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCTRANTYPE char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCU1ACC char(20) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDATAIMP char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCRECOMENB char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FDRECOMENB datetime DEFAULT NULL NULL,
    # FMMEMDATA6 varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FMMEMDATA7 varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FMMEMDATA8 varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FMMEMDATA9 varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FMMEMDATAA varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FCRECALBY char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FTLASRECAL datetime DEFAULT NULL NULL,
    # FCCARTYPE char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDELIBY char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCVEHICLE char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCTHRDPTY char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCROUTEDEL char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDOCSTEP char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDOCAPRVB char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FDDOCAPRV datetime NULL,
    # FCCRSTEP char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCRAPRVB char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FDCRAPRV datetime NULL,
    # FCU1STATUS char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCU2STATUS char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDTYPE1 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNU1CNT decimal(4,0) DEFAULT 0 NOT NULL,
    # FCDTYPE2 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNU2CNT decimal(4,0) DEFAULT 0 NOT NULL,
    # FCU3STATUS char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDTYPE3 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNU3CNT decimal(4,0) DEFAULT 0 NOT NULL,
    # FCU4STATUS char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDTYPE4 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNU4CNT decimal(4,0) DEFAULT 0 NOT NULL,
    # FCU5STATUS char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDTYPE5 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNU5CNT decimal(4,0) DEFAULT 0 NOT NULL,
    # FCU6STATUS char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDTYPE6 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNU6CNT decimal(4,0) DEFAULT 0 NOT NULL,
    # FCU7STATUS char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDTYPE7 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNU7CNT decimal(4,0) DEFAULT 0 NOT NULL,
    # FCU8STATUS char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDTYPE8 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNU8CNT decimal(4,0) DEFAULT 0 NOT NULL,
    # FCU9STATUS char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDTYPE9 char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FNU9CNT decimal(4,0) DEFAULT 0 NOT NULL,
    # FCDOCFLOWI char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FMDOCFLOW varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FCBOICARD char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCBOIGROUP char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCONTACTN char(70) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FTSRCUPD datetime NULL,
    # FCSRCUPD char(30) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCGID char(128) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCARRIER char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCCARRYTYP char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCDELIEMPL char(8) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FCSTATAPPV char(1) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # FTSTATAPPV datetime DEFAULT getdate() NULL,
    # FMEXTRATAG text COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # FCORGCODE varchar(128) COLLATE Thai_CI_AS DEFAULT '' NOT NULL,
    # FCCUACC varchar(128) COLLATE Thai_CI_AS DEFAULT '' NOT NULL,
    # FCAPPNAME varchar(128) COLLATE Thai_CI_AS DEFAULT '' NOT NULL,
    # StatusApp = models.IntegerField(verbose_name="ขั้นตอนที่", db_column="STATUS_APP")# STATUS_APP int DEFAULT 0 NOT NULL,
    StatusApp = models.IntegerField(verbose_name="ขั้นตอนที่", db_column="STATUS_APP", choices=STATUS_CHOICES)
    # Sendmail int DEFAULT 0 NOT NULL,
    # Send_BY varchar(500) COLLATE Thai_CI_AS DEFAULT NULL NULL,
    # Send_Datetime datetime DEFAULT NULL NULL,
    # createByEmp char(30) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,
    # editByEmp char(30) COLLATE Thai_CI_AS DEFAULT ' ' NOT NULL,

    def __str__(self) -> str:
        return f"{self.ID}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "PR_H"
        app_label = "budgetapp"
        verbose_name = "ข้อมูล Purchase"
        verbose_name_plural = "Purchase"


class LogStepSendMail(models.Model):
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
        app_label = "budgetapp"
        verbose_name = "ข้อมูล Step SendMail"
        verbose_name_plural = "Step SendMail"