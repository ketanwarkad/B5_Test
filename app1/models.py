from django.db import models

# Create your models here.
class Common_Class(models.Model):
    def __str__(self):
        #return f"{self.__dict__}"
        if type(self)==Employee:
            return f"{self.id}--{self.name}"
        elif type(self)==License:
            return f"{self.license_no}--{self.expiry_date}"
        elif type(self)==Task:
            return f"{self.__dict__}"
        elif type(self)==Project:
            #return f"{self.project_id}--{self.name}"
            return f"{self.__dict__}"

    def __repr__ (self):
        return str(self)
    
    class Meta:
        abstract =True


class Employee(Common_Class):  #table name
    name=models.CharField(max_length=100)
    salary=models.FloatField()
    adr=models.CharField(max_length=500)
    company=models.CharField(max_length=100,default="Infosys")

    class Meta:
        db_table = "emp"

    def get_task_count(self):
        return len(self.task_set.all())

#change made u
#ALTER TABLE `app1_employee` RENAME COLUMN `address` TO `adr`;
# ALTER TABLE `app1_employee` ADD COLUMN `company` varchar(100) DEFAULT 'Infosys' NOT NULL;
# ALTER TABLE `app1_employee` ALTER COLUMN `company` DROP DEFAULT;

    

    def name_salary(self):
        return f"Nmae :-{self.name}  Salary :-{self.salary}"


class License(Common_Class):
    license_no =models.CharField(primary_key=True,max_length=16) #ALTER TABLE `Licene` DROP COLUMN `id`;ALTER TABLE `Licene` ADD CONSTRAINT `Licene_license_no_89a9050d_pk` PRIMARY KEY (`license_no`);
    expiry_date=models.DateField()
    d1_type=models.CharField(max_length=10)
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE)

    class Meta:
        db_table= "Licene"

    def get_employee(self):
        return self.employee

    def change_address(self,new_adr):
        self.employee.adr=new_adr
        self.employee.save()
        print("Adress updated")

    # def get_license_obj(id):
    #     return Employee.objects.get(id=id)
    @classmethod
    def get_license_obj(cls,license_no):
        return cls.objects.get(license_no=license_no)


class Task(Common_Class):
    task_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    timeline=models.DateTimeField(null=True)
    task_create_date=models.DateTimeField(auto_now_add=True)
    employee=models.ForeignKey(Employee,null=True,on_delete=models.SET_NULL,related_name="tasks") # if we set null we have to mention null=True otherwise it will raise

    class Meta:
        db_table="task"

    def get_employee(self):
        return self.employee

#create table Employee(id int auto increment,name varchar(50),salary float,primary key(id))

#CREATE TABLE "app1_employee" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "salary" real NOT NULL, "address" varchar(500) NOT NULL);
#COMMI

#Create model Task

#CREATE TABLE `task` (`task_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(100) NOT NULL, `timeline` datetime(6) NOT NULL, `task_create_date` datetime(6) NOT NULL, `employee_id` bigint NULL);
#ALTER TABLE `task` ADD CONSTRAINT `task_employee_id_0035587e_fk_emp_id` FOREIGN KEY (`employee_id`) REFERENCES `emp` (`id`);

class Project(Common_Class):
    project_id=models.AutoField(primary_key=True)
    description=models.TextField(null=True)
    name=models.CharField(max_length=15)
    duration=models.CharField(max_length=16)
    client=models.CharField(max_length=16)
    employee=models.ManyToManyField(Employee,db_table="emp_projects")

    class Meta:
        db_table="projects"


#**************************************************

class Common_Pizza(models.Model):

    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    class Meta:
        abstract=True

class Topping(Common_Pizza):
    pass
    

class Pizza(Common_Pizza):

    
    toppings = models.ManyToManyField('Topping',related_name='pizzas')

# class Test:
#     models.CharField(max_length=100)    
#  adding a new line

class Master(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=50,null=True)
    instrument = models.CharField(max_length=500)

