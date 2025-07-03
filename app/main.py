from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    comments = request.form['comments']

    # Save the data to a CSV file
    with open('registrations.csv', 'a') as f:
        f.write(f'{name},{email},{phone},{course},{comments}\n')

    return render_template('success.html', name=name, course=course)

@app.route('/students')
def students():
    student_list = []
    try:
        with open('registrations.csv', 'r') as file:
            for line in file:
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

# Required for Render.com (bind to 0.0.0.0 and use env PORT)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
