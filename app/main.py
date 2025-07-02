from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        comments = request.form['comments']

        # Save to CSV file
        with open('registrations.csv', 'a') as file:
            file.write(f"{name},{email},{phone},{course},{comments}\n")

        return redirect(url_for('success', name=name, course=course))

    return render_template('register.html')

# Success / Thank You Page
@app.route('/success')
def success():
    name = request.args.get('name')
    course = request.args.get('course')
    return render_template('success.html', name=name, course=course)

# Students List Page
@app.route('/students')
def students():
    student_list = []

    try:
        with open('registrations.csv', 'r') as file:
            for line in file:
                # Handle possible missing commas or empty fields
                fields = line.strip().split(',')
                if len(fields) == 5:
                    name, email, phone, course, comments = fields
                    student_list.append({
                        'name': name,
                        'email': email,
                        'phone': phone,
                        'course': course,
                        'comments': comments
                    })
    except FileNotFoundError:
        student_list = []

    return render_template('students.html', students=student_list)

if __name__ == '__main__':
    app.run(debug=True)
