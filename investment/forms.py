from django import forms
from .models import Institution, Investor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, HTML, Div, MultiField, Field



class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        # fields = ('name', 'email', 'body')
        exclude = ('join_date', 'date_of_registration',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'add_institution'
        self.helper.layout = Layout(
        Fieldset(
                'Institution Particulars',
            
            Div(
                Div(
                    Div(
                        Field('name', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    
                    Div(
                        Field('business_type', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('district', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                   
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('sub_county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('village', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('address', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('email', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('amount_invested', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('payment_method', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('source_of_income', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'
                ),
                css_class = 'row'
            )
           ),
           Fieldset(
               'Bank Details',
                Div(
                Div(
                    Div(
                        Field('bank_name', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('bank_branch', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('bank_account_number', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('bank_telephone', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('bank_email', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'
                ),
                css_class = 'row'
            )
           ),
           Fieldset(
               'Signatory One Particulars',
                Div(
                Div(
                    Div(
                        Field('signatory_one_surname', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_one_given_name', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_one_occupation', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('signatory_one_telephone', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_one_district', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    
                    Div(
                        Field('signatory_one_county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_one_sub_county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'
                ),
                css_class = 'row'
            )
           ),
           Fieldset(
               'Signatory Two Particulars',
                Div(
                Div(
                    Div(
                        Field('signatory_two_surname', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_two_given_name', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_two_occupation', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('signatory_two_telephone', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_two_district', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    
                    Div(
                        Field('signatory_two_county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_two_sub_county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'
                ),
                css_class = 'row'
            )
           ),
           Fieldset(
               'Signatory Three Particulars',
                Div(
                Div(
                    Div(
                        Field('signatory_three_surname', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_three_given_name', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_three_occupation', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('signatory_three_telephone', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_three_district', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    
                    Div(
                        Field('signatory_three_county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('signatory_three_sub_county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'
                ),
                css_class = 'row'
            )
           ),
            Submit('submit', 'Submit', css_class='button white')
        )

class InvestorForm(forms.ModelForm):
    
    class Meta:
        model = Investor
        # fields = '__all__'
        exclude = ('join_date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = 'add_investor'
        # self.helper.add_input(Submit('submit', 'Submitt'))
        self.helper.layout = Layout(
            Fieldset(
                'Investor Particulars',
            
            Div(
                Div(
                    Div(
                        Field('photo', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('surname', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('given_name', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('district', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    
                    Div(
                        Field('sub_county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('village', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('telephone', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('address', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('email', css_class='form-control'),
                        css_class = 'form-group'
                    ),

                    Div(
                        Field('amount_invested', css_class='form-control'),
                        css_class = 'form-group'
                    ),

                    Div(
                        Field('payment_method', css_class='form-control'),
                        css_class = 'form-group'
                    ),

                    Div(
                        Field('source_of_income', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'
                ),
                css_class = 'row'
            )
           ),
           Fieldset(
               'Next of kin details',
               Div(
                Div(
                    Div(
                        Field('kin_surname', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('kin_given_name', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('kin_occupation', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('kin_telephone', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('kin_district', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('kin_county', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('kin_sub_county', css_class='form-control'),
                        css_class = 'form-group'
                    ),

                    Div(
                        Field('kin_village', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('kin_address', css_class='form-control'),
                        css_class = 'form-group'
                    ),

                    Div(
                        Field('kin_email', css_class='form-control'),
                        css_class = 'form-group'
                    ),

                    Div(
                        Field('kin_note', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'
                ),
                css_class = 'row'
            )
           ),
           Fieldset(
               'Bank Details',
                Div(
                Div(
                    Div(
                        Field('bank_name', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('bank_branch', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('bank_account_number', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    Div(
                        Field('bank_telephone', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'

                ),
                Div(
                    Div(
                        Field('bank_email', css_class='form-control'),
                        css_class = 'form-group'
                    ),
                    css_class = 'col-md-4'
                ),
                css_class = 'row'
            )
           ),
           
            Submit('submit', 'Submit', css_class='button white')
        )

# class BankForm(forms.ModelForm):
    
#     class Meta:
#         model = Bank
#         fields = '__all__'

# class SignatoryForm(forms.ModelForm):
    
#     class Meta:
#         model = Signatory
#         fields = '__all__'

# class NextofkinForm(forms.ModelForm):
    
#     class Meta:
#         model = Nextofkin
#         fields = '__all__'
