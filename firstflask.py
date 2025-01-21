from flask import Flask, render_template, request, render_template_string
import random


app = Flask(__name__)

@app.route("/") 
def helloworld():
    return "Hello, World!"

@app.route("/stat") 
def helloSTAT():
    return "Hello, STAT KKU!"

(__name__)

@app.route("/research")
def research_page():
    faculty_research = {
    "Dr. Alice Smith": [
        "Statistical Modeling of Climate Change Impacts",
        "Advanced Methods in Time Series Analysis",
        "Machine Learning Applications in Biostatistics",
    ],
    "Dr. Bob Johnson": [
        "Bayesian Inference in Social Sciences",
        "Quantitative Analysis of Economic Trends",
        "Development of Robust Statistical Software",
    ],
    "Dr. Carol Davis": [
        "Optimization Techniques in Big Data Analytics",
        "Statistical Approaches to Epidemiology",
        "Survey Data Analysis for Policy Decisions",
    ],
    }

    faculty, research_projects = random.choice(list(faculty_research.items()))
    
    return render_template("research.html", faculty=faculty, research_projects=research_projects)


@app.route("/statHTML") 
def helloSTAThtml():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stat KKU - Homepage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            header {
                background-color: #0078d7;
                color: white;
                padding: 1rem 0;
                text-align: center;
            }
            nav {
                background-color: #005ea6;
                display: flex;
                justify-content: center;
                padding: 0.5rem 0;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 1rem;
            }
            nav a:hover {
                text-decoration: underline;
            }
            main {
                padding: 2rem;
                text-align: center;
            }
            footer {
                background-color: #0078d7;
                color: white;
                text-align: center;
                padding: 1rem 0;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Stat KKU</h1>
            <p>Department of Statistics, Khon Kaen University</p>
        </header>
        <nav>
            <a href="/statHTML#about">About Us</a>
            <a href="/statHTML#programs">Programs</a>
            <a href="/research">Research</a>
            <a href="/contact">Contact</a>
        </nav>
        <main>
            <section id="about">
                <h2>About Us</h2>
                <p>The Department of Statistics at Khon Kaen University is a center of excellence for education and research in statistics.</p>
                <p>We strive to nurture students with the knowledge and skills needed for data-driven decision-making in various industries.</p>
                <p>Our department is committed to providing a dynamic learning environment that bridges theoretical knowledge and real-world application.</p>
                <p>We pride ourselves on our highly qualified faculty, who are leaders in their respective areas of statistical expertise.</p>
                <p>With strong ties to industry and academic institutions, we ensure our students are prepared for global challenges.</p>
                <p>We host regular workshops, seminars, and guest lectures to keep our students and faculty updated with the latest advancements in statistics and data science.</p>
                <p>Our state-of-the-art facilities and advanced software tools provide students with a hands-on learning experience.</p>
                <p>Many of our alumni have achieved great success in fields such as finance, healthcare, technology, and academia.</p>
                <p>Our focus on research encourages students to contribute to solving pressing issues in society through statistical methodologies.</p>
                <p>Join us at Stat KKU, where we turn passion for data into impactful solutions for the future.</p>
            </section>
            <section id="programs">
                <h2>Programs</h2>
                <p>We offer undergraduate and postgraduate programs in statistics to prepare students for successful careers.</p>
            </section>
            <section id="research">
                <h2>Research</h2>
                <p>Our faculty members are engaged in cutting-edge research to address real-world challenges using statistical methods.</p>
            </section>
        </main>
        <footer>
            <p>&copy; 2025 Stat KKU. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """

@app.route("/contact",methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        user_email = request.form.get("email")
        with open("email.txt", "a") as myfile:
            myfile.write(f'{user_email} \n')
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contact Us</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f9f9f9;
                    color: #333;
                }
                header {
                    background-color: #0078d7;
                    color: white;
                    text-align: center;
                    padding: 1rem 0;
                }
                main {
                    padding: 2rem;
                    max-width: 600px;
                    margin: auto;
                    text-align: left;
                    background: white;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1 {
                    color: #005ea6;
                }
                p {
                    line-height: 1.6;
                }
                footer {
                    text-align: center;
                    margin-top: 2rem;
                    font-size: 0.9rem;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Contact Us</h1>
            </header>
            <main>
                <h2><a href="/statHTML">Admin</a> Contact Details</h2>
                <p><strong>Name:</strong> John Doe</p>
                <p><strong>Email:</strong> admin@example.com</p>
                <p><strong>Phone:</strong> +1-234-567-890</p>
                <p>If you have any questions or need assistance, please don’t hesitate to reach out. Our admin is here to help you!</p>
                <h2>Thank you {{user}}</h2>
            </main>
            <footer>
                <p>&copy; 2025 Stat KKU. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """,user=user_email)
    else:
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contact Us</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f9f9f9;
                    color: #333;
                }
                header {
                    background-color: #0078d7;
                    color: white;
                    text-align: center;
                    padding: 1rem 0;
                }
                main {
                    padding: 2rem;
                    max-width: 600px;
                    margin: auto;
                    text-align: left;
                    background: white;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1 {
                    color: #005ea6;
                }
                p {
                    line-height: 1.6;
                }
                footer {
                    text-align: center;
                    margin-top: 2rem;
                    font-size: 0.9rem;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Contact Us</h1>
            </header>
            <main>
                <h2><a href="/statHTML">Admin</a> Contact Details</h2>
                <p><strong>Name:</strong> John Doe</p>
                <p><strong>Email:</strong> admin@example.com</p>
                <p><strong>Phone:</strong> +1-234-567-890</p>
                <p>If you have any questions or need assistance, please don’t hesitate to reach out. Our admin is here to help you!</p>
                <h2>Submit Your Email So We Can Contact You Back</h2>
                <form method="POST">
                    <label for="email">Your Email:</label>
                    <input type="email" id="email" name="email" required placeholder="Enter your email">
                    <button type="submit">Submit</button>
                </form>
            </main>
            <footer>
                <p>&copy; 2025 Stat KKU. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """
        
        

if __name__ == "__main__":   # run code 
    app.run()
