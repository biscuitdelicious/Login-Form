from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, EmailField, validators
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(),
                                                  validators.Length(min=4)], render_kw={'autofocus': True})
    password = PasswordField(label='Password',
                             validators=[DataRequired(),
                                         validators.Length(min=8)])
    submit = SubmitField(label='Go')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'





@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('index.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
