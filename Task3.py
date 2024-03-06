#Task 3 MySQL Database Operations with Python
#importing required libraries
import mysql.connector
#function for creating table
def create_table(connection):
    cursorObject = connection.cursor()
    cursorObject.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            age INT,
            grade FLOAT
        )
    """)
    connection.commit()
    cursorObject.close()

#function for inserting data
def insert_student(connection, first_name, last_name, age, grade):
    cursorObject = connection.cursor()
    cursorObject.execute("""
        INSERT INTO students (first_name, last_name, age, grade)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, age, grade))
    connection.commit()
    cursorObject.close()
#function for updating data
def update_grade(connection, first_name, new_grade):
    cursorObject = connection.cursor()
    cursorObject.execute("""
        UPDATE students
        SET grade = %s
        WHERE first_name = %s
    """, (new_grade, first_name))
    connection.commit()
    cursorObject.close()
#function for delete
def delete_student(connection, last_name):
    cursorObject = connection.cursor()
    cursorObject.execute("""
        DELETE FROM students
        WHERE last_name = %s
    """, (last_name,))
    connection.commit()
    cursorObject.close()
#fucntion fro fetching table
def fetch_all_students(connection):
    cursorObject = connection.cursor()
    cursorObject.execute("SELECT * FROM students")
    records =  cursorObject.fetchall()
    cursorObject.close()
    for record in records:
        print(record)

if __name__ == "__main__":
#for creating connection  
    connection = mysql.connector.connect(
      host ="localhost",
      user ="anand",
      passwd ="root",
  
    )
 
    # preparing a cursor object
    cursorObject = connection.cursor()

    #creating database
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS Samtadb")
    #using the created database
    cursorObject.execute("USE Samtadb")

    #calling create table function to Create the "students" table
    create_table(connection)

    #Insert a new student record
    insert_student(connection, "Alice", "Smith", 18, 92.5)
    insert_student(connection, "Troy", "Jane", 18, 95.5)
    insert_student(connection, "Philip", "Smith", 18, 93.5)
    insert_student(connection, "King", "Junior", 18, 94.5)
    insert_student(connection, "Lory", "Jane", 18, 94.5)

    #Update the grade of the student with the first name "Alice"
    update_grade(connection, "Alice", 97.0)
    print("Table after Updating:")
    fetch_all_students(connection)

    #Delete the student with the last name "Smith"
    delete_student(connection, "Smith")

    # Fetch and display all student records
    print("Final Data after deleting all record with surname Smith")
    fetch_all_students(connection)

    # Close the database connection
    connection.close()




