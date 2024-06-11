
   <h1>n1x Discord Bot</h1>
    <p>This project is a Discord bot developed in Python, featuring various functionalities including moderation, user commands, and interaction with the OpenAI API.</p>
    <p><strong>Note:</strong> This project contains NSFW content.</p>

<h2>Getting Started</h2>
    <p>To use this bot, you need to set up your Discord bot token and OpenAI API key.</p>

   <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.6 or higher</li>
        <li>Discord.py library</li>
        <li>OpenAI API key</li>
    </ul>

   <h3>Installation</h3>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/yourusername/n1x-discord-bot.git
cd n1x-discord-bot</code></pre>
        <li>Create a <code>.env</code> file in the root directory and add your Discord bot token and OpenAI API key:</li>
        <pre><code>token="your_token"
openai_api_key="your_api"</code></pre>
        <li>Install the required dependencies:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
        <li>Run the bot:</li>
        <pre><code>python index.py</code></pre>
    </ol>

   <h2>Usage</h2>
    <p>Once the bot is up and running, you can interact with it using various commands. Here are some of the available commands:</p>
    <ul>
        <li><code>!8ball [question]</code>: Ask the Magic 8-Ball a question.</li>
        <li><code>!neko</code>: Get a random neko image.</li>
        <li><code>!nsfw</code>: Get a random NSFW image (only in NSFW channels).</li>
        <li><code>!kick @user [reason]</code>: Kick a user from the server (requires appropriate permissions).</li>
        <li><code>!mute @user [duration]</code>: Mute a user for a specified duration (requires appropriate permissions).</li>
    </ul>

  <h2>Project Structure</h2>
    <p>The project contains the following files:</p>
    <ul>
        <li><code>index.py</code>: Main entry point of the bot.</li>
        <li><code>.env</code>: Configuration file for storing sensitive information.</li>
        <li><code>cogs/</code>: Directory containing various modules (cogs) for different bot functionalities.</li>
        <ul>
            <li><code>8_ball.py</code>: Module for handling the Magic 8-Ball command.</li>
            <li><code>botevents.py</code>: Module for handling bot events.</li>
            <li><code>moderation.py</code>: Module for moderation commands.</li>
            <li><code>neko.py</code>: Module for fetching neko images.</li>
            <li><code>nsfw.py</code>: Module for handling NSFW commands.</li>
            <li><code>user_comnd.py</code>: Module for user-defined commands.</li>
        </ul>
    </ul>

   <h2>Contributing</h2>
    <p>Contributions to the project are welcome! Feel free to open an issue or submit a pull request to suggest improvements or add new features.</p>

  <h2>Contact</h2>
    <p>For any questions or suggestions, feel free to contact the repository owner at <a href="mailto:nikhilkanojia693@gmail.com">nikhilkanojia693@gmail.com</a>.</p>
