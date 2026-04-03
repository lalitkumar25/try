const express = require('express');
const app = express();

app.set('view engine', 'ejs');
app.set('views', __dirname);
app.use(express.static(__dirname));

const members = [
    { 
        id: 1, 
        name: "Lalit Kumar",
        role: "MCA (Cloud Technology)",
        img: "profile.jpg",
        color: "#38bdf8", 
        email: "2025mcactdlalit24349@poornima.edu.in",
        objective: "With an MCA in Cloud Technology, I aspire to work in a dynamic IT environment where I can apply my skills in cloud infrastructure and application development.",
        education: [
            "MCA - Poornima University Jaipur (2027 Current)",
            "BCA - Lachoo Memorial College (74% - 2025)",
            "12th - Siddharth Vidhya Mandir (78% - 2022)"
        ],
        projects: [
            "AQI: Real-time pollution tracking for multiple locations.",
            "Quiz Website: Level-based programming quizzes."
        ],
        certification: "Web Development by Ducat",
        skills: ["Java", "Python", "C/C++", "AWS", "Docker", "Kubernetes", "Linux", "MySQL"]
    },
    { 
        id: 2, 
        name: "Mayank Mishra",
        role: "MCA (Cloud Technology & DevOps)",
         img: "mayankprofile.jpg",
        color: "#10b981", 
        email: "2025mcactdmayank22447@poornima.edu.in",
        objective: "Enthusiastic MCA student specializing in Cloud Technology & DevOps. Passionate about building scalable and reliable systems.",
        education: [
            "MCA (Cloud Tech & DevOps) - Poornima University (2025-2027)",
            "BCA - Seeta Devi College, Bhilwara (79% - 2025)",
            "12th - Govt. Senior Secondary School (71.60% - 2022)"
        ],
        projects: [
            "Self-Healing Cloud App: Deployed on AWS EC2 with automated recovery.",
            "DevOps Pipeline: High reliability testing with Bash and cron."
        ],
        certification: "Google Cloud Career Launchpad – Cloud Engineer",
        skills: ["Jenkins", "Git", "AWS (EC2, S3, VPC)", "Docker", "Kubernetes", "Linux", "Bash"]
    },
    { 
        id: 3, 
        name: "Ashish Jat",
        role: "MCA (Cloud Technology & DevOps)",
        img: "ashishprofile.jpg",
        color: "#f87171", 
        email: "2025mcactdashish22446@poornima.edu.in",
        objective: "Enthusiastic MCA student specializing in Cloud Technology & DevOps with strong fundamentals in Linux, cloud computing, and automation.",
        education: [
            "MCA (Cloud Technology & DevOps) - Poornima University (Current - 8.0 CGPA)",
            "BCA - Poornima University (2025)",
            "12th - Govt. Senior Secondary School, Mandal (62.40% - 2022)"
        ],
        projects: [
            "Self-Healing Cloud Web Application: Managed on AWS EC2 using systemd, shell scripting, and cron jobs for automatic recovery.",
            "Automated Monitoring: Designed systems to run autonomously, improving reliability and uptime."
        ],
        certification: "Cloud Computing fundamentals",
        skills: ["Git/GitHub", "Jenkins", "AWS (EC2, S3, IAM, VPC)", "Docker", "Kubernetes", "Linux/Bash", "C/C++", "Java", "Python"]
    }
];

app.get('/', (req, res) => res.render('index', { members }));
app.get('/details/:id', (req, res) => {
    const user = members.find(m => m.id == req.params.id);
    res.render('details', { user });
});

app.listen(3000, () => console.log("Server Live: http://localhost:3000"));