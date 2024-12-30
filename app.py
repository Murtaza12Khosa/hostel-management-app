from flask import Flask, render_template,redirect,url_for,request,flash

app = Flask(__name__)
app.secret_key = "your_unique_and_secret_key"

# Home route
@app.route('/')
def home():
    return render_template('base.html')

# Registration route
@app.route('/registration')
def registration():
    return render_template('registration.html')

# User Login route
@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        # Extract the username and password from the form
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate credentials (example with dummy data)
        if username == 'user' and password == 'password':  # Replace with your logic
            return redirect(url_for('user_dashboard'))  # Redirect to the dashboard

        # If credentials are invalid, show an error message
        flash("Invalid username or password. Please try again.")
        return render_template('user_login.html', error=flash)

    # Render the login page for GET requests
    return render_template('user_login.html')

# Admin Login route
ADMIN_USERNAME = 'admin'  # You can change this to the actual username
ADMIN_PASSWORD = 'pass123'  # Change this to the actual password

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the entered credentials are correct
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            # If correct, redirect to the admin dashboard
            return redirect(url_for('admin_dashboard'))
        else:
            # If incorrect, show an error message
            flash('Invalid username or password', 'error')
    
    return render_template('admin_login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')# Render the dashboard template
@app.route('/add_course.html')
def add_course():
    return render_template('add_course.html')
@app.route('/manage_course.html')
def manage_course():
    return render_template('manage_course.html')
@app.route('/add_room.html')
def add_room():
    return render_template('add_room.html')
@app.route('/manage_room.html')
def manage_room():
    return render_template('manage_room.html')
@app.route('/manage_room_edit.html')
def manage_room_edit():
    return render_template('manage_room_edit.html')
@app.route('/admin_student_registration.html')
def admin_student_registration():
    return render_template('admin_student_registration.html')
@app.route('/manage_student.html')
def manage_student():
    return render_template('manage_student.html')
@app.route('/complaint_new.html')
def complaint_new():
    return render_template('complaint_new.html')
@app.route('/complaint_inprocess.html')
def complaint_inprocess():
    return render_template('complaint_inprocess.html')
@app.route('/complaint_closed.html')
def complaint_closed():
    return render_template('complaint_closed.html')
@app.route('/admin_feedback.html')
def admin_feedback():
    return render_template('admin_feedback.html')
@app.route('/user_access.html')
def user_access():
    return render_template('user_access.html')

@app.route('/user_dashboard.html')
def user_dashboard():
    return render_template('user_dashboard.html')
@app.route('/book_hostel.html')
def book_hostel():
    return render_template('book_hostel.html')
@app.route('/complaint.html')
def complaint():
    return render_template('complaint.html')
@app.route('/my_profile.html')
def my_profile():
    return render_template('my_profile.html')
@app.route('/room_detail.html')
def room_detail():
    return render_template('room_detail.html')
@app.route('/registered_complaint.html')
def registered_complaint():
    return render_template('registered_complaint.html')
@app.route('/feedback.html')
def feedback():
    return render_template('feedback.html')
@app.route('/change_password.html')
def change_password():
    return render_template('change_password.html')
@app.route('/access_log.html')
def access_log():
    return render_template('access_log.html')
if __name__ == "__main__":
    app.run(debug=True)
