from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
cnx = mysql.connector.connect(
    user='root',
    password='ansh#1234',
    host='localhost',
    database='ansh'
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        age = request.form['age']
        salary = request.form['salary']

        # Insert data into the table
        insert_data_query = '''
        INSERT INTO employees (name, age, salary)
        VALUES (%s, %s, %s)
        '''
        cursor = cnx.cursor()
        cursor.execute(insert_data_query, (name, age, salary))
        cnx.commit()

    return render_template('index.html')

if __name__ == '__main__':
    # Create the table if it doesn't exist
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        salary FLOAT
    )
    '''
    cursor = cnx.cursor()
    cursor.execute(create_table_query)
    cnx.commit()

    app.run()

