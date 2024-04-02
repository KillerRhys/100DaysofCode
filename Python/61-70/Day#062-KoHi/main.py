from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name: ', validators=[DataRequired()])
    location = URLField(label='Location: ', validators=[DataRequired(), URL()])
    open_time = StringField(label='Opens: ', validators=[DataRequired()])
    close_time = StringField(label='Closes: ', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating:', choices=[(0, '✘'), (1, '☕️'), (2, '☕️☕️'), (3, '☕️☕️☕️'),
                                                      (4, '☕️☕️☕️☕️'), (5, '☕️☕️☕️☕️☕️')])
    wifi = SelectField(label='Wifi Strength:', choices=[(0, '✘'), (1, '💪'), (2, '💪💪️'), (3, '💪💪💪️'),
                                                    (4, '💪💪💪💪'), (5, '💪💪💪💪💪')])
    outlet = SelectField(label='Outlets Available :', choices=[(0, '✘'), (1, '🔌'), (2, '🔌🔌️'), (3, '🔌🔌🔌️'),
                                                    (4, '🔌🔌🔌🔌'), (5, '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode='a', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.outlet.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
