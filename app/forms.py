from flask_wtf import FlaskForm
import wtforms as ws

class TransactionsForm(FlaskForm):
    period = ws.StringField('Период', validators=[ws.validators.DataRequired(), ])
    value = ws.IntegerField('Сумма', validators=[ws.validators.DataRequired(), ])
    status = ws.StringField('Статус', validators=[ws.validators.DataRequired(), ])
    unit = ws.StringField('Валюта', validators=[ws.validators.DataRequired(), ])
    subject = ws.StringField('Коментарии', validators=[ws.validators.DataRequired(), ])


class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=4, max=20)
    ])
    password = ws.PasswordField('Пароль:', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=8, max=24)
    ])
