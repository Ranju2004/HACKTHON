![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Server-green.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

<h1>⚠️ Record Telegram Logs Through Bot Token</h1>

<p>This repository is <b>educational</b>. It shows why your <b>Telegram bot token</b> must be protected and how attackers might misuse it if exposed.</p>

<hr>

<h2>📦 Setup </h2>

<blockquote>⚠️ Create A <b>Demo Bot</b>, just for awareness.</blockquote>

<ol>
  <li>Clone this repository:</li>
</ol>

<pre><code>git clone https://github.com/Linuxndroid/BOT-CATCHER.git
cd BOT-CATCHER
</code></pre>

<ol start="2">
  <li>Create A <b> data.json</b> File & Paste Data This Format <b> Social Enginnering Purpose</b></li>
</ol>

<pre><code>{"id":1305437481,"mobile":"0987654321","name":"Little Linuxndroid","father_name":"Linuxndroid","address":"W\/O  Kali Linux Roda,House no 24-35-41!24\/2, Parrot Circule, Hacker, Blackhat522003","alt_mobile":"1234567890","circle":"JIO AP","id_number":"123456","email":"Kali@gmail.com"}
</code></pre>

<ol start="3">
  <li>Paste Your <code>Bot Token</code> in Line 5 <b> app.py</b> file:</li>
</ol>

<pre><code>TOKEN = "3666364477:AAFOtaTTMq7M6JIKIDuvPjHckOBvorm6wH0"
</code></pre>

<ol start="4">
  <li>Run the app.py file :</li>
</ol>

<pre><code>python app.py
</code></pre>

<hr>
<blockquote>⚠️ All Chats From User & Bot, RealTime Save in <b>log.txt</b>, You can Watch it every user logs</blockquote>

<li>Chats Save in Log.txt :</li>
<pre><code>[2025-09-08 15:09:55] Linuxndroid (USER): Nitish
[2025-09-08 15:10:01] Linuxndroid (BOT): ✅ Record Found:
Name:  Linuxndroid
Father:  Linuxndoid
Mobile: 00000000
Alt: 0999976352
Address:   kali linux, Parrot circule, hacker, blackhat, 132103 
Circle:  Parrot
ID: 623673673
Email: kali@gmail.com

</code></pre>

<h2>🚨 Why This Matters</h2>

<p>Your <b>Telegram bot token is like a master key</b>. If leaked, a hacker could:</p>

<ul>
  <li>📩 Read every message users send to your bot.</li>
  <li>🕵️ Pretend to be your bot and send fake replies.</li>
  <li>📥 Collect usernames and sensitive conversations.</li>
</ul>

<p>Even a small leak (like uploading code to GitHub) can put your users at risk.</p>

<hr>

<h2>⚠️ Awareness Scenario</h2>

<p>A malicious actor who gets your token could:</p>

<ol>
  <li>Steal the token from public code.</li>
  <li>Connect to Telegram’s API using that token.</li>
  <li>Record conversations from unsuspecting users.</li>
  <li>Abuse the data for scams, identity theft, or blackmail.</li>
</ol>

<p>👉 This is why <b>never share your bot token publicly</b>.</p>

<hr>

<h2>🔒 Best Practices</h2>

<ul>
  <li>✅ Do Not Share Your Bot Token Someone</li>
  <li>✅ Use Secure Method To Store Bot Token in Your App</li>
  <li>✅ Regenerate your token immediately if it leaks.</li>
  <li>✅ Inform your users that bot chats are <b>not end-to-end encrypted</b>.</li>
</ul>

<hr>

<h2>📌 Key Takeaways</h2>

<ul>
  <li>Your <b>bot token = password</b>. Treat it that way.</li>
  <li>Awareness helps protect both <b>developers and users</b>.</li>
  <li>Always build bots with <b>security first</b>.</li>
</ul>

<hr>


<p>✍️ This repository is for <b>cybersecurity awareness and education only</b>.<br>
Do not use it for malicious purposes.</p>

# Watch Video For More Information.
[![YouTube Video](https://img.youtube.com/vi/lgEBDCMCqNo/0.jpg)](https://youtu.be/lgEBDCMCqNo?feature=shared)

<p align="center">Made with ❤️ By <a href="https://www.youtube.com/channel/UC2O1Hfg-dDCbUcau5QWGcgg">Linuxndroid</a></p>

# Available Our [Hacking Course](https://linuxndroid.in)

# Follow Me on :

[![Instagram](https://img.shields.io/badge/IG-linuxndroid-yellowgreen?style=for-the-badge&logo=instagram)](https://www.instagram.com/linuxndroid)

[![Youtube](https://img.shields.io/badge/Youtube-linuxndroid-redgreen?style=for-the-badge&logo=youtube)](https://www.youtube.com/channel/UC2O1Hfg-dDCbUcau5QWGcgg)

[![Browser](https://img.shields.io/badge/Website-linuxndroid-yellowred?style=for-the-badge&logo=browser)](https://www.linuxndroid.in)
