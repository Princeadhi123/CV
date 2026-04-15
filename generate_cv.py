from xhtml2pdf import pisa
import os

# Define the HTML content for the CV
# Uses table-based layouts for xhtml2pdf compatibility (no flexbox support)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Prince Adhikary - CV</title>
    <style>
        @page {
            size: A4;
            margin: 20mm 18mm;
        }
        body {
            font-family: Helvetica, Arial, sans-serif;
            color: #333333;
            line-height: 1.4;
            margin: 0;
            padding: 0;
            font-size: 10pt;
        }
        .container {
            width: 100%;
        }
        header {
            text-align: center;
            padding-bottom: 10px;
            margin-bottom: 15px;
            border-bottom: 2px solid #1a5276;
        }
        h1 {
            margin: 0 0 8px 0;
            color: #1a5276;
            font-size: 24pt;
            font-weight: bold;
        }
        .contact-line {
            font-size: 9pt;
            color: #555555;
            margin-bottom: 3px;
        }
        .contact-line a {
            color: #2874a6;
            text-decoration: none;
        }
        .section-title {
            color: #1a5276;
            font-size: 11pt;
            font-weight: bold;
            text-transform: uppercase;
            margin-top: 14px;
            margin-bottom: 8px;
            padding-bottom: 3px;
            border-bottom: 1px solid #1a5276;
        }
        .summary {
            text-align: justify;
            margin-left: 10px;
            color: #444444;
        }
        .item {
            margin-bottom: 10px;
            margin-left: 10px;
        }
        .row-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 2px;
        }
        .row-table td {
            padding: 0;
            vertical-align: top;
        }
        .row-left {
            font-weight: bold;
            color: #333333;
            font-size: 10.5pt;
        }
        .row-right {
            text-align: right;
            font-weight: bold;
            color: #2874a6;
            font-size: 9.5pt;
        }
        .sub-left {
            color: #555555;
            font-size: 9.5pt;
        }
        .sub-right {
            text-align: right;
            font-style: italic;
            color: #666666;
            font-size: 9pt;
        }
        ul {
            margin: 4px 0 0 0;
            padding-left: 16px;
        }
        li {
            margin-bottom: 2px;
            color: #444444;
        }
        .skills-container {
            margin-left: 10px;
        }
        .skill-block {
            margin-bottom: 5px;
        }
        .skill-category-inline {
            font-weight: bold;
            color: #333333;
        }
        .skill-items {
            color: #555555;
        }
        .publication {
            margin-bottom: 8px;
            margin-left: 10px;
        }
        .doi {
            font-family: Courier, monospace;
            font-size: 8.5pt;
            color: #666666;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>PRINCE DAS ADHIKARY</h1>
            <div class="contact-line">
                princeadhi123@gmail.com | +358 46 8011795 | Turku, Finland (Willing to Relocate)
            </div>
            <div class="contact-line">
                <a href="https://linkedin.com/in/prince-adhikary-037719102">linkedin.com/in/prince-adhikary</a> |
                <a href="https://github.com/Princeadhi123">github.com/Princeadhi123</a>
            </div>
        </header>

        <div class="section-title">PROFESSIONAL SUMMARY</div>
        <p class="summary">
            Doctoral Researcher and Software Engineer specializing in empirical machine learning and the architectural design of scalable AI-driven systems. Concurrently advancing Knowledge Tracing models at TRILA while actively engineering foundational backend infrastructure for an institution-wide item bank alongside the software team. Backed by rigorous industry software engineering experience and independent development of complex quantitative Python systems (algorithmic trading engines). Proven ability to balance research exploration with engineering rigor, and currently designing protocols for safely integrating Large Language Models (LLMs) into educational feedback systems.
        </p>

        <div class="section-title">EDUCATION &amp; RESEARCH</div>
        <div class="item">
            <table class="row-table">
                <tr>
                    <td class="row-left">PhD in Learning Analytics</td>
                    <td class="row-right">Jan 2025 – Present</td>
                </tr>
                <tr>
                    <td class="sub-left">University of Turku (TRILA)</td>
                    <td class="sub-right">Turku, Finland</td>
                </tr>
            </table>
            <ul>
                <li><strong>Educational Infrastructure &amp; Engineering:</strong> Functioning as a core Software Engineer alongside TRILA's development team to architect and prototype the foundational backend infrastructure for a comprehensive educational item bank.</li>
                <li><strong>Empirical ML Research:</strong> Designing and testing machine learning models (utilizing Python, PyTorch, Scikit-learn) for Knowledge Tracing to predict student knowledge states and model complex learning trajectories.</li>
                <li><strong>Ethical Data &amp; Profiling:</strong> Navigating strict ethical constraints and data privacy protocols to conduct empirical evaluations of student learning data, specifically contrasting semantic versus numeric profiling.</li>
                <li><strong>Upcoming LLM Integration (Phase 3):</strong> Designing the architectural framework to integrate LLMs into existing Knowledge Tracing models to develop a steerable, intelligent feedback system.</li>
            </ul>
        </div>

        <div class="item">
            <table class="row-table">
                <tr>
                    <td class="row-left">MSc, Finance and Big Data Analytics</td>
                    <td class="row-right">Sept 2022 – Dec 2023</td>
                </tr>
                <tr>
                    <td class="sub-left">Swansea University</td>
                    <td class="sub-right">Honors: First Class | "Best Performing Student Award"</td>
                </tr>
            </table>
            <ul>
                <li>Thesis: "Predicting the Stock Market Using Machine Learning Algorithms: Evidence from India and Brazil". <br/>
                <span class="doi">DOI: 10.13140/RG.2.2.15118.68169</span></li>
                <li>Conducted empirical research utilizing Python and R to model complex financial time-series data.</li>
            </ul>
        </div>

        <div class="item">
            <table class="row-table">
                <tr>
                    <td class="row-left">BE, Computer Technology</td>
                    <td class="row-right">June 2015 – June 2019</td>
                </tr>
                <tr>
                    <td class="sub-left">YCCE, India</td>
                    <td class="sub-right">Honors: First Class</td>
                </tr>
            </table>
            <ul>
                <li>Focus: Data Structures, Machine Learning, Cloud Computing, and Network Security.</li>
            </ul>
        </div>

        <div class="section-title">INDEPENDENT TECHNICAL PROJECTS</div>
        <div class="item">
            <table class="row-table">
                <tr>
                    <td class="row-left">Algorithmic Trading Engine (Ongoing)</td>
                    <td class="row-right" style="font-size: 8.5pt;">github.com/Princeadhi123/Crypto-trading-bot</td>
                </tr>
            </table>
            <ul>
                <li><strong>System Architecture:</strong> Architected a highly modular, asynchronous Python trading bot (ccxt, FastAPI), balancing complex quantitative logic (Statistical Arbitrage, Market Regime Detection) with strict software engineering principles.</li>
                <li><strong>Data Pipelines &amp; ML Preparation:</strong> Engineered robust data extraction pipelines to log empirical trade features (ensemble confidence, ATR volatility percentiles, funding rates). Currently preparing to implement an XGBoost classifier for post-trade predictive modeling.</li>
                <li><strong>Quantitative Risk Management:</strong> Implemented robust financial modeling modules, including automated Value at Risk (VaR) calculators and sentiment filters.</li>
            </ul>
        </div>

        <div class="section-title">PROFESSIONAL EXPERIENCE</div>
        <div class="item">
            <table class="row-table">
                <tr>
                    <td class="row-left">Software Engineer</td>
                    <td class="row-right">July 2021 – July 2022</td>
                </tr>
                <tr>
                    <td class="sub-left">NEC Software Solutions India</td>
                    <td class="sub-right"></td>
                </tr>
            </table>
            <ul>
                <li><strong>System Optimization:</strong> Implemented strategic enhancements to backend business flows, increasing system efficiency by 20% and reducing operational costs by 10%.</li>
                <li><strong>Technical Leadership:</strong> Directed an agile team of 6 engineers to deliver robust code across cross-functional environments, improving project delivery timelines by 15%.</li>
                <li><strong>Operational Reliability:</strong> Partnered with QA to resolve complex systemic issues during intensive regression testing, earning the "Rising Star Award" for exceptional technical execution.</li>
            </ul>
        </div>

        <div class="item">
            <table class="row-table">
                <tr>
                    <td class="row-left">Associate Software Engineer</td>
                    <td class="row-right">July 2019 – June 2021</td>
                </tr>
                <tr>
                    <td class="sub-left">NEC Software Solutions India</td>
                    <td class="sub-right"></td>
                </tr>
            </table>
            <ul>
                <li><strong>Infrastructure &amp; APIs:</strong> Spearheaded the development of scalable RESTful services utilizing the Spring Framework, SQL, and AWS.</li>
                <li><strong>Engineering Rigor:</strong> Streamlined code development and deployment processes utilizing Jira and GitHub to maintain an error-free, rapidly iterating codebase.</li>
            </ul>
        </div>

        <div class="section-title">TECHNICAL SKILLS</div>
        <div class="skills-container">
            <div class="skill-block">
                <span class="skill-category-inline">AI/ML Research:</span>
                <span class="skill-items">Empirical Evaluation, Knowledge Tracing, Predictive Modeling</span>
            </div>
            <div class="skill-block">
                <span class="skill-category-inline">Python Data Stack:</span>
                <span class="skill-items">Python, PyTorch, Pandas, Scikit-learn, Jupyter Notebook</span>
            </div>
            <div class="skill-block">
                <span class="skill-category-inline">Systems Engineering:</span>
                <span class="skill-items">AWS, Spring Boot, REST APIs, Java, SQL, Foundational System Architecture</span>
            </div>
            <div class="skill-block">
                <span class="skill-category-inline">Engineering Rigor:</span>
                <span class="skill-items">Git, Jira, Agile/Scrum, CI/CD, Cross-functional Collaboration</span>
            </div>
        </div>

        <div class="section-title">PUBLICATIONS</div>
        <div class="publication">
            Das Adhikary, P., et al. (2026). "Knowledge Tracing Models in Educational Data Mining: Historical Evolution, Categorization, and Empirical Evaluation." <strong>IEEE Access</strong>. <br/>
            <span class="doi">DOI: 10.1109/ACCESS.2025.11457580</span>
        </div>
        <div class="publication">
            Das Adhikary, P., et al. (2026). "From Numbers to Narratives: A comparative analysis of semantic versus numeric student profiling." <strong>ResearchGate</strong>. <br/>
            <span class="doi">DOI: 10.13140/RG.2.2.10642.41927</span>
        </div>
    </div>
</body>
</html>
"""

# Generate PDF
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(script_dir, "Prince_Adhikary_CV.pdf")

with open(pdf_path, "w+b") as pdf_file:
    status = pisa.CreatePDF(html_content, dest=pdf_file)

if status.err:
    print(f"Error generating PDF: {status.err}")
else:
    print(f"CV generated successfully: {pdf_path}")
