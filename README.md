## Design for a Flask Application to Teach Beginner Marathi

### HTML Files

- **index.html:** The landing page of the application, featuring buttons or links to different sections of the learning materials.
- **lessons.html:** A page that displays the lessons, organized into different levels (e.g., beginner, intermediate, advanced).
- **quiz.html:** A page that presents quizzes or exercises to test the learner's understanding.
- **resources.html:** A page that provides supplemental resources for learning Marathi, such as dictionaries, grammar references, or links to online communities.

### Routes

- **@app.route('/')** (index page): The home page of the application where the user has options to begin learning or access the lessons.
- **@app.route('/lessons')** (lessons page): Displays the list of lessons available. Each lesson can be linked to a separate page with more detailed content.
- **@app.route('/quiz')** (quiz page): Presents a quiz to test the user's knowledge. The quiz can have multiple-choice questions, fill-in-the-blank exercises, or other interactive elements.
- **@app.route('/resources')** (resources page): Provides links to various helpful resources for learning Marathi, such as online dictionaries, grammar references, or language learning apps.