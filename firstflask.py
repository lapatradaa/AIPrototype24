from flask import Flask, render_template, request, render_template_string
import random

app = Flask(__name__)

@app.route("/") 
def helloworld():
    return "Hello, World!"

@app.route("/stat") 
def helloSTAT():
    return "Hello, STAT KKU!"

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
            <a href="#about">About Us</a>
            <a href="#programs">Programs</a>
            <a href="/research">Research</a>
            <a href="/htmlcontact">Contact</a>
        </nav>
        <main>
  <section id="about">
                <h2>About Us</h2>
                    <p>
                    1. The Department of Statistics at Khon Kaen University offers a wide range of undergraduate and graduate programs designed to equip students with a deep understanding of statistical theory and its practical applications. The curriculum emphasizes both foundational knowledge and the latest advancements in the field, preparing students for diverse career opportunities in academia, industry, and government.
                    </p>
                    <p>
                    2. Faculty members at the department are accomplished researchers with expertise in areas such as data science, machine learning, biostatistics, econometrics, and experimental design. Their research contributes to solving real-world problems, from analyzing big data to improving healthcare outcomes, making the department a hub for innovative statistical research in Southeast Asia.
                    </p>
                    <p>
                    3. The department prides itself on fostering a supportive learning environment where students are encouraged to explore their interests and develop critical thinking skills. Through interactive lectures, hands-on workshops, and collaborative projects, students gain practical experience in statistical programming, data visualization, and predictive modeling.
                    </p>
                    <p>
                    4. Beyond the classroom, the department is actively engaged in community outreach and collaborative research initiatives. Faculty and students frequently work with local organizations and industries, providing statistical expertise to enhance decision-making processes in areas such as agriculture, education, public health, and environmental management.
                    </p>
                    <p>
                    5. The department also houses state-of-the-art facilities, including computer labs equipped with the latest statistical software and tools. These resources enable students to work on cutting-edge research projects, analyze complex datasets, and apply their skills to solve pressing societal challenges.
                    </p>
                    <p>
                    6. One of the department's key goals is to stay at the forefront of statistical education by integrating emerging technologies such as artificial intelligence and cloud computing into its programs. This ensures that graduates are well-prepared to navigate the rapidly evolving landscape of data science and analytics.
                    </p>
                    <p>
                    7. The department regularly organizes academic events, including workshops, seminars, and conferences, to bring together leading statisticians, researchers, and practitioners from around the world. These events provide valuable networking opportunities for students and faculty and foster a culture of knowledge exchange and innovation.
                    </p>
                    <p>
                    8. In addition to academic pursuits, the department emphasizes the importance of ethics and social responsibility in the application of statistics. Students are encouraged to consider the broader implications of their work, ensuring that statistical analyses are conducted with integrity, transparency, and a focus on societal benefit.
                    </p>
                    <p>
                    9. Alumni of the Department of Statistics at Khon Kaen University have gone on to excel in various fields, including finance, technology, healthcare, and education. Their achievements serve as a testament to the department's commitment to producing well-rounded, skilled professionals who make meaningful contributions to society.
                    </p>
                    <p>
                    10. As the demand for statistical expertise continues to grow, the Department of Statistics at Khon Kaen University remains dedicated to its mission of advancing statistical knowledge through high-quality education, impactful research, and meaningful community engagement. By nurturing the next generation of statisticians, the department aims to play a pivotal role in shaping a data-driven future.
                    </p>

            </section>
            <section id="programs">
                <h2>Programs</h2>
                <p>We offer a comprehensive range of undergraduate and postgraduate programs in statistics, tailored to equip students with the knowledge and skills necessary for success in both academic and professional settings. Our undergraduate program covers fundamental statistical theory, while the graduate programs offer specialized courses in areas such as data science, machine learning, biostatistics, and econometrics. Graduates are well-prepared to embark on diverse career paths in industries such as healthcare, finance, technology, and government.</p>
                <p>Our graduate programs include a Master's degree and a Ph.D. program that focus on advanced statistical techniques, cutting-edge research, and real-world applications. Students have the opportunity to work closely with faculty on innovative research projects, contributing to global advancements in statistical science.</p>
                <p>In addition, we offer professional development programs and workshops designed to help students and industry professionals keep up-to-date with the latest trends and technologies in the field of statistics.</p>
            </section>

            <section id="research">
                <h2>Research</h2>
                <p>Our faculty members are at the forefront of statistical research, contributing to a wide range of interdisciplinary fields. Through their work, they address real-world challenges by applying advanced statistical methods and tools. Research areas include, but are not limited to, data science, artificial intelligence, biostatistics, financial modeling, environmental statistics, and public health analysis. Their efforts have not only expanded the body of statistical knowledge but also provided practical solutions to pressing issues faced by society.</p>
                <p>Our research initiatives often involve collaboration with government agencies, healthcare organizations, and industry leaders, ensuring that our work has a tangible impact on real-world problems. Students and faculty participate in research projects that explore diverse topics such as predictive modeling for healthcare, statistical methods for climate change analysis, and the use of machine learning algorithms for financial forecasting.</p>
                <p>The department organizes and hosts various research seminars, workshops, and conferences to foster collaboration between statisticians, researchers, and practitioners. These events provide an excellent opportunity for students to engage with experts in the field, gain insights into cutting-edge developments, and contribute to ongoing discussions about the future of statistics and data science.</p>
            </section>

            <section id="contact">
                <h2>Contact</h2>
                <p>If you have any questions or inquiries about our programs, research, or any other aspect of the Department of Statistics, please feel free to contact us.</p>
                <p>Email: <a href="mailto:info@statkku.ac.th">info@statkku.ac.th</a></p>
                <p>Phone: <a href="tel:+6612345678">+66-1234-5678</a></p>
                <p>Location: Department of Statistics, Khon Kaen University, Khon Kaen, Thailand.</p>
                <p>Our department is located on the university campus, easily accessible for both visitors and students. Feel free to drop by our office during business hours for more information, or get in touch through email or phone.</p>
                <p>We also have a presence on social media where we share the latest updates, research highlights, and events. Follow us on:</p>

                <p>Our team is happy to assist with any inquiries and provide further details about our department and programs. We look forward to connecting with you!</p>
            </section>
        </main>
        <footer>
            <p>&copy; 2025 Stat KKU. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """

@app.route("/htmlcontact",methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        user_email = request.form.get("email")
        with open("email.text", "a") as myfile:
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
                button {
                    background-color: #0078d7;
                    color: white;
                    padding: 0.5rem 1rem;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #005ea6;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Contact Us</h1>
            </header>
            <main>
                <h2>Admin Contact Details</h2>
                <p><strong>Name:</strong> John Doe</p>
                <p><strong>Email:</strong> admin@example.com</p>
                <p><strong>Phone:</strong> +66-234-567-890</p>
                <p>If you have any questions or need assistance, please don’t hesitate to reach out. Our admin is here to help you!</p>
                <h2>Thank you {{user}}</h2>
                <a href="/statHTML"><button>Back</button></a>
            </main>
            <footer>
                <p>&copy; 2025 Stat KKU. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """, user=user_email)
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
                button {
                    background-color: #0078d7;
                    color: white;
                    padding: 0.5rem 1rem;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #005ea6;
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

##api
@app.route('/simpleAPI', methods=['POST'])
def simpleAPI():
    try:
        # รับข้อมูลจาก request
        payload = request.data.decode("utf-8")
        inmessage = json.loads(payload)

        # แสดงข้อมูลที่ได้รับใน log
        print("\n[INFO] นี่คือข้อมูลที่ได้รับจากผู้ใช้:")
        print(f"----------------------------")
        print(f"ข้อความที่ได้รับ: {inmessage.get('msg')}")
        print(f"ชื่อผู้ส่ง: {inmessage.get('ผู้ส่ง')}")
        print(f"ชื่อผู้รับ: {inmessage.get('ผู้รับ')}")
        print(f"IP ของผู้รับ: {inmessage.get('ip')}")
        print(f"----------------------------\n")

        # สร้างข้อมูลที่ต้องการส่งกลับ
        json_data = json.dumps({'y': 'received!'})

        # ส่งข้อมูลกลับไป
        return json_data, 200  # คืนค่า HTTP Status 200 เพื่อบอกว่า request สำเร็จ

    except Exception as e:
        # ในกรณีเกิดข้อผิดพลาด
        error_message = f"[ERROR] ข้อผิดพลาด: {str(e)}"
        print(error_message)

        # ส่งข้อผิดพลาดกลับไป
        return jsonify({'error': 'เกิดข้อผิดพลาด'}), 400

if __name__ == "__main__":   # run code 
    app.run(host='0.0.0.0',debug=True,port=5000)