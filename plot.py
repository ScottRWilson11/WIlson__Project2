import sqlite3
import matplotlib.pyplot as plt

from flask import Flask, render_template

app = Flask(__name__, template_folder='./')

@app.route("/")
@app.route("/index")
def show_index():
        #print("Server request")
        conn =sqlite3.connect('Healthcare_data.db')

        #-------------- Age vs Chol
        result = conn.execute("Select age, avg(chol) from heart group by age")
        Age = []
        Chol = []
        for row in result:   
            Age.append(row[0])
            Chol.append(row[1])

        plt.subplot(3, 1, 1)
        plt.scatter(Age,Chol,30, c='red', label='Cholostrol')
        plt.xlabel("Age")
        plt.ylabel("Cholostrol")
        plt.title("Age vs Cholostrol level")
        plt.xticks(rotation=45)
        #plt.show()

        #-------------- Gender vs Chol
        result = conn.execute("Select sex, avg(chol) from heart group by sex")
        Gender = []
        GChol = []
        for row in result:
                if (row[0] == "0"):
                        Gender.append("F")
                else:
                        Gender.append("M")
                
                GChol.append(row[1])

        plt.subplot(3, 1, 2)
        plt.scatter(Gender,GChol,30, c='red', label='Cholostrol')
        plt.xlabel("Gender")
        plt.ylabel("Cholostrol")
        plt.title("Gender vs Cholostrol level")
       
        #plt.show()

        #-------------- Age vs Cpchest count
        result = conn.execute("Select age, count(cp) from heart group by age")
        CAge = []
        Cpchest = []
        for row in result:   
            CAge.append(row[0])
            Cpchest.append(row[1])

        conn.close()
        plt.subplot(3, 1, 3)
        plt.scatter(CAge,Cpchest,30, c='red', label='Cholostrol')
        plt.xlabel("Age")
        plt.ylabel("Chest Pains")
        plt.title("Age vs chest pains")
        plt.xticks(rotation=45)
        plt.savefig('static/plot.png')
        plt.clf()
        return render_template('index.html')

@app.route("/plot1")
def plot1():
        print("request plot1")
        conn =sqlite3.connect('Healthcare_data.db')

        #-------------- Age vs Chol
        result = conn.execute("Select age, avg(chol) from heart group by age")
        Age = []
        Chol = []
        for row in result:   
                Age.append(row[0])
                Chol.append(row[1])

        conn.close()
        plt.clf()
        plt.scatter(Age,Chol,30, c='red', label='Cholostrol')
        plt.xlabel("Age")
        plt.ylabel("Cholostrol")
        plt.title("Age vs Cholostrol level")
        plt.xticks(rotation=45)
        plt.savefig('static/plot1.png')
        plt.clf()
        return render_template('plot1.html')

@app.route("/plot2")
def plot2():
        print("request plot2")
        conn =sqlite3.connect('Healthcare_data.db')
        #-------------- Gender vs Chol
        result = conn.execute("Select sex, avg(chol) from heart group by sex")
        Gender = []
        GChol = []
        for row in result:
                if (row[0] == "0"):
                        Gender.append("F")
                else:
                        Gender.append("M")
                
                GChol.append(row[1])

        conn.close()
        plt.clf()
        plt.scatter(Gender,GChol,30, c='red', label='Cholostrol')
        plt.xlabel("Gender")
        plt.ylabel("Cholostrol")
        plt.title("Gender vs Cholostrol level")
        plt.xticks(rotation=45)
        plt.savefig('static/plot2.png')
        plt.clf()
        return render_template('plot2.html')

@app.route("/plot3")
def plot3():
        print("request plot3")
        conn =sqlite3.connect('Healthcare_data.db')

        #-------------- Age vs Chol
        result = conn.execute("Select age, count(cp) from heart group by age")
        CAge = []
        Cpchest = []
        for row in result:   
            CAge.append(row[0])
            Cpchest.append(row[1])

        conn.close()
        plt.clf()
        plt.scatter(CAge,Cpchest,30, c='red', label='Cholostrol')
        plt.xlabel("Age")
        plt.ylabel("Chest Pains")
        plt.title("Age vs chest pains")
        plt.xticks(rotation=45)
        plt.savefig('static/plot3.png')
        plt.clf()
        return render_template('plot3.html')

if __name__== "__main__":
	app.run()
