from flask import Flask, render_template, request


def yearly_total_needed(monthly_need, time_to_save, inflation):
    return round((monthly_need * 12) * ((1 + inflation) ** time_to_save))

def current_savings_compounded(current_savings, return_rate, time_to_save):
    return round((current_savings * (1 + (return_rate)) ** time_to_save), 2)

def total_savings_needed(yearly_total_needed, return_rate):
    return round((yearly_total_needed / (return_rate)))

def yearly_savings_rate(F, i, n):
    return F * (i) / (((1+i) ** (n)) - 1)


app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def index():
    # greeting = "Hello World"

    if request.method == "POST":
        global yearly_total_needed
        # global total_savings_needed
        # global return_rate
        name = request.form['name']
        current_age = int(request.form['current_age'])
        retirement_age = int(request.form['retirement_age'])
        current_savings = int(request.form['current_savings'])
        return_rate = float(request.form['return_rate'])
        income = int(request.form['income'])
        monthly_need = int(request.form['monthly_need'])
        inflation = .0275
        compounding_length = int(retirement_age - current_age)
        savings_compounded = current_savings_compounded(current_savings, return_rate, compounding_length)
        yearly_total_goal = yearly_total_needed(monthly_need, compounding_length, inflation)
        total_savings_goal = total_savings_needed(yearly_total_goal, return_rate/2)
        need_to_save = total_savings_goal - savings_compounded
        savings_rate = yearly_savings_rate(need_to_save, return_rate / 12 , compounding_length * 12)
        monthly_savings_rate = round(savings_rate)

        greeting = f"""
        To meet your goal of retiring at {retirement_age}, you'll need
        ${total_savings_goal} to make that possible.  If you save at least
        ${monthly_savings_rate} per month and your investments perform well,
        you can make that happen!"""
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")


if __name__ == "__main__":
    app.run(debug=True)
