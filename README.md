🎮 Tic Tac Toe Game

A simple and fun Tic Tac Toe game built using HTML, CSS, and JavaScript.
This project demonstrates basic game logic, event handling, and DOM manipulation — perfect for beginners learning front-end web development.

🚀 Features

🔹 Two-Player Mode: Play between Player X and Player O.

🔹 Real-Time Updates: Instantly shows moves and results.

🔹 Winner Detection: Automatically checks and displays the winner or draw.

🔹 Restart Option: Reset the game anytime without reloading the page.

🔹 Responsive Design: Works smoothly on mobile, tablet, and desktop.

🔹 Attractive UI: Styled using CSS with smooth hover and transition effects.

🧩 Technologies Used
Technology	Description
HTML5	Structure of the game board and buttons
CSS3	Styling and layout for a clean design
JavaScript (ES6)	Game logic, event handling, and win conditions
📁 Folder Structure
tic-tac-toe/
│
├── index.html       # Main HTML file  
├── style.css        # CSS for layout and styling  
└── script.js        # JavaScript for game functionality  

⚙️ How It Works

The board consists of 9 clickable cells (3x3 grid).

Players take turns marking X or O on empty cells.

JavaScript checks all possible winning combinations after each move.

If all cells are filled and no one wins → it’s a Draw!

The Reset button clears the board and starts a new game.

🔍 Winning Combinations Example:
[0, 1, 2]   → Top row  
[3, 4, 5]   → Middle row  
[6, 7, 8]   → Bottom row  
[0, 3, 6]   → Left column  
[1, 4, 7]   → Middle column  
[2, 5, 8]   → Right column  
[0, 4, 8]   → Diagonal  
[2, 4, 6]   → Diagonal  

🎨 Example Enhancements

Add winning line animation using CSS transitions.

Add sound effects when a player wins or the match draws.

Add scoreboard to track wins.

Implement AI Player for single-player mode (using minimax algorithm).



💡 Future Improvements

🧠 Add AI opponent (computer mode)

🌗 Add dark/light theme switcher

💬 Add pop-up modal for game results

📱 Improve mobile responsiveness

🧑‍💻 Author

Prachi Patle
🎓 B.Tech in Information Technology
💻 Passionate about Frontend Development and Interactive Web Projects
