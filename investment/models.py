from django.db import models

# Create your models here.
class Investor(models.Model):
    # Investor's particulars
    photo = models.ImageField(upload_to='investors/%Y/%m/%d/', null=True, blank=True)
    surname = models.CharField(max_length=20)
    given_name = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    sub_county = models.CharField(max_length=20)
    village = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    amount_invested = models.PositiveIntegerField()
    PAYMENT_METHOD_CHOICES = (
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
        )
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='Monthly')
    source_of_income = models.CharField(max_length=30)

    join_date = models.DateField(auto_now_add=True)

    # Next of kin details
    kin_surname = models.CharField(max_length=20)
    kin_given_name = models.CharField(max_length=20)
    kin_occupation = models.CharField(max_length=20)
    kin_telephone = models.CharField(max_length=20)
    kin_district = models.CharField(max_length=20)
    kin_county = models.CharField(max_length=20)
    kin_sub_county = models.CharField(max_length=20)
    kin_village = models.CharField(max_length=20)
    kin_address = models.CharField(max_length=30)
    kin_email = models.EmailField()
    kin_note = models.TextField(null=True, blank=True)

    # Bank details
    bank_name = models.CharField(max_length=30, blank=True, null=True)
    bank_branch = models.CharField(max_length=20, blank=True, null=True)
    bank_account_number = models.PositiveIntegerField(blank=True, null=True)
    bank_telephone = models.CharField(max_length=20, blank=True, null=True)
    bank_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.surname} {self.given_name}'
    

# class Nextofkin(models.Model):
#     investor = models.OneToOneField(Investor, on_delete=models.CASCADE)
#     surname = models.CharField(max_length=20)
#     given_name = models.CharField(max_length=20)
#     occupation = models.CharField(max_length=20)
#     telephone = models.CharField(max_length=20)
#     district = models.CharField(max_length=20)
#     county = models.CharField(max_length=20)
#     sub_county = models.CharField(max_length=20)
#     village = models.CharField(max_length=20)
#     address = models.CharField(max_length=30)
#     email = models.EmailField()
#     note = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f'{self.name} {self.given_name}'



class Institution(models.Model):
    name = models.CharField(max_length=30)
    date_of_registration = models.DateField(null=True, blank=True)
    BUSINESS_TYPE_CHOICES = (
        ('For Profit', 'For Profit'),
        ('Not For Profit', 'Not For Profit'),
    )
    business_type = models.CharField(max_length=20, choices = BUSINESS_TYPE_CHOICES, default='Not For Profit')
    district = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    sub_county = models.CharField(max_length=20)
    village = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    amount_invested = models.PositiveIntegerField()
    PAYMENT_METHOD_CHOICES = (
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
        )
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='Monthly')
    source_of_income = models.CharField(max_length=30)
    join_date = models.DateField(auto_now_add=True)

    # Bank details
    bank_name = models.CharField(max_length=30, blank=True, null=True)
    bank_branch = models.CharField(max_length=20, blank=True, null=True)
    bank_account_number = models.PositiveIntegerField(blank=True, null=True)
    bank_telephone = models.CharField(max_length=20, blank=True, null=True)
    bank_email = models.EmailField(blank=True, null=True)

    signatory_one_surname = models.CharField(max_length=20)
    signatory_one_given_name = models.CharField(max_length=20)
    signatory_one_occupation = models.CharField(max_length=20)
    signatory_one_telephone = models.CharField(max_length=20)
    signatory_one_district = models.CharField(max_length=20)
    signatory_one_county = models.CharField(max_length=20)
    signatory_one_sub_county = models.CharField(max_length=20)

    signatory_two_surname = models.CharField(max_length=20)
    signatory_two_given_name = models.CharField(max_length=20)
    signatory_two_occupation = models.CharField(max_length=20)
    signatory_two_telephone = models.CharField(max_length=20)
    signatory_two_district = models.CharField(max_length=20)
    signatory_two_county = models.CharField(max_length=20)
    signatory_two_sub_county = models.CharField(max_length=20)

    signatory_three_surname = models.CharField(max_length=20)
    signatory_three_given_name = models.CharField(max_length=20)
    signatory_three_occupation = models.CharField(max_length=20)
    signatory_three_telephone = models.CharField(max_length=20)
    signatory_three_district = models.CharField(max_length=20)
    signatory_three_county = models.CharField(max_length=20)
    signatory_three_sub_county = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# class Signatory(models.Model):
#     institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
#     surname = models.CharField(max_length=20)
#     given_name = models.CharField(max_length=20)
#     occupation = models.CharField(max_length=20)
#     telephone = models.CharField(max_length=20)
#     district = models.CharField(max_length=20)
#     county = models.CharField(max_length=20)
#     sub_county = models.CharField(max_length=20)

#     def __str__(self):
#         return f'{self.name} {self.given_name}'
    
    


# class Bank(models.Model):
#     investor = models.OneToOneField(Investor, on_delete=models.CASCADE, null=True, blank=True)
#     institution = models.OneToOneField(Institution, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=30)
#     branch = models.CharField(max_length=20)
#     account_number = models.PositiveIntegerField()
#     telephone = models.CharField(max_length=20)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name
    
    