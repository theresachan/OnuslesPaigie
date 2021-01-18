from flask import Flask, render_template, request, redirect, url_for, session
from Forms import CreateEntryForm
from Forms import CreateReturnForm
import shelve, Entry
import shelve, Returns

app = Flask(__name__)
app.secret_key = 'any_random_string'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/deleteReturn/<int:id>', methods=['POST'])
def delete_return(id):
    users_dict = {}
    db = shelve.open('storage.db', 'w')
    users_dict = db['Returns']

    users_dict.pop(id)

    db['Returns'] = users_dict
    db.close()

    return redirect(url_for('retrieve_returns'))



@app.route('/createReturn', methods=['GET', 'POST'])
def create_return():
    create_return_form = CreateReturnForm(request.form)
    if request.method == 'POST' and create_return_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            users_dict = db['Returns']
        except:
            print("Error in retrieving Users from storage.db.")

        user = Returns.Returns(create_return_form.product.data, create_return_form.quantity.data, create_return_form.reason.data, create_return_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Returns'] = users_dict

        db.close()


        return redirect(url_for('retrieve_returns'))
    return render_template('createReturn.html', form=create_return_form)


@app.route('/retrieveReturn')
def retrieve_returns():
    users_dict = {}
    db = shelve.open('storage.db', 'r')
    users_dict = db['Returns']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)


    return render_template('retrieveReturn.html', count=len(users_list), users_list=users_list)

@app.route('/updateReturn/<int:id>/', methods=['GET', 'POST'])
def update_return(id):
    update_return_form = CreateReturnForm(request.form)
    if request.method == 'POST' and update_return_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'w')
        users_dict = db['Returns']

        user = users_dict.get(id)
        user.set_product(update_return_form.product.data)
        user.set_quantity(update_return_form.quantity.data)
        user.set_reason(update_return_form.reason.data)
        user.set_remarks(update_return_form.remarks.data)

        db['Returns'] = users_dict
        db.close()

        return redirect(url_for('retrieve_returns'))
    else:
        db = shelve.open('storage.db', 'r')
        users_dict = db['Returns']
        db.close()

        user = users_dict.get(id)
        update_return_form.product.data = user.get_product()
        update_return_form.quantity.data = user.get_quantity()
        update_return_form.reason.data = user.get_reason()
        update_return_form.remarks.data = user.get_remarks()

        return render_template('updateReturn.html', form=update_return_form)

@app.route("/trackShipment")
def trackShipment():
    return render_template('trackShipment.html')

@app.route("/aboutus")
def blog():
    return render_template('about.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')

@app.route("/checkout")
def checkout():
    return render_template('checkout.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/myorders")
def myorders():
    return render_template('myorders.html')

@app.route("/shopgrid")
def shopgrid():
    return render_template('shop_grid.html')

@app.route("/pay")
def pay():
    return render_template("pay.html")

@app.route("/order", methods=["GET"])
def order():
    return render_template("ordersummary.html")

@app.route("/staff", methods=['GET', 'POST'])
def staff():
    create_entry_form = CreateEntryForm(request.form)
    if request.method == 'POST' and create_entry_form.validate():
        entries_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            entries_dict = db['Entries']
        except:
            print("Error in retrieving Users from storage.db.")

        entry = Entry.Entry(create_entry_form.cost_category.data, create_entry_form.expenses.data
                            )
        entries_dict[entry.get_entry_id()] = entry
        db['Entries'] = entries_dict

        # Test codes
        entries_dict = db['Entries']
        entry = entries_dict[entry.get_entry_id()]
        print(entry.get_cost_category(), "was stored in storage.db successfully with entry_id ==",
              entry.get_entry_id())

        db.close()

        session['entry_created'] = entry.get_cost_category()

        return redirect(url_for('retrieve_entries'))
    return render_template("staff.html",form=create_entry_form)

@app.route('/retrieveEntry')
def retrieve_entries():
    entries_dict = {}
    db = shelve.open('storage.db', 'r')
    entries_dict = db['Entries']
    db.close()

    entries_list = []
    for key in entries_dict:
        entry = entries_dict.get(key)
        entries_list.append(entry)
    return render_template('retrieveEntries.html', count=len(entries_list), entries_list=entries_list)

@app.route('/updateEntry/<int:id>/', methods=['GET','POST'])
def update_entry(id):
    update_entry_form = CreateEntryForm(request.form)
    if request.method == 'POST' and update_entry_form.validate():
        entries_dict = {}
        db = shelve.open('storage.db', 'w')
        entries_dict = db['Entries']

        entry = entries_dict.get(id)
        entry.set_cost_category(update_entry_form.cost_category.data)
        entry.set_expenses(update_entry_form.expenses.data)

        db['Entries'] = entries_dict
        db.close()

        session['entry_updated'] = entry.get_cost_category()

        return redirect(url_for('retrieve_entries'))
    else:
        entries_dict = {}
        db = shelve.open('storage.db', 'r')
        entries_dict = db['Entries']
        db.close()

        entry = entries_dict.get(id)
        update_entry_form.cost_category.data = entry.get_cost_category()
        update_entry_form.expenses.data = entry.get_expenses()

        return render_template('updateEntry.html', form=update_entry_form)

@app.route('/deleteEntry/<int:id>', methods=['POST'])
def delete_entry(id):
    entries_dict = {}
    db = shelve.open('storage.db', 'w')
    entries_dict = db['Entries']

    entry = entries_dict.pop(id)

    db['Entries'] = entries_dict
    db.close()

    session['entry_deleted'] = entry.get_cost_category()

    return redirect(url_for('retrieve_entries'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run()

