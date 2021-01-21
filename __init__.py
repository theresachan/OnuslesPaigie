from flask import Flask, render_template, request, redirect, url_for, session
from Forms import CreateEntryForm, CheckoutForm
import shelve, Entry, Order

app = Flask(__name__)
app.secret_key = 'any_random_string'

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/aboutus")
def blog():
    return render_template('about.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    create_checkout_form = CheckoutForm(request.form)
    if request.method == 'POST' and create_checkout_form.validate():
        orders_dict = {}
        db = shelve.open('orders.db', 'c')
        try:
            orders_dict = db['Orders']
        except:
            print("Error in retrieving Orders from storage.db.")

        order = Order.Order(create_checkout_form.email.data, create_checkout_form.address1.data,
                            create_checkout_form.address2.data
                            )
        orders_dict[order.get_order_id()] = order
        db['Orders'] = orders_dict
        # Test codes
        orders_dict = db['Orders']
        order = orders_dict[order.get_order_id()]
        print(order.get_email(), "was stored in storage.db successfully with order_id ==",
              order.get_order_id())

        db.close()

        return redirect(url_for('retrieve_order'))
    return render_template('checkout.html', title="Onusles - Checkout", form=create_checkout_form)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/shopgrid")
def shopgrid():
    return render_template('shop_grid.html')

@app.route("/order")
def retrieve_order():
    orders_dict = {}
    db = shelve.open('orders.db', 'c')
    orders_dict = db['Orders']
    db.close()

    orders_list = []
    for key in orders_dict:
        order = orders_dict.get(key)
        orders_list.append(order)
    return render_template('retrieveOrder.html', count=len(orders_list), orders_list=orders_list)

@app.route("/staff", methods=['GET', 'POST'])
def staff():
    create_entry_form = CreateEntryForm(request.form)
    if request.method == 'POST' and create_entry_form.validate():
        entries_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            entries_dict = db['Entries']
        except:
            print("Error in retrieving Entries from storage.db.")

        entry = Entry.Entry(create_entry_form.cost_category.data, create_entry_form.expenses.data, create_entry_form.description.data
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
        entry.set_description(update_entry_form.description.data)

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
        update_entry_form.description.data = entry.get_description()

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

