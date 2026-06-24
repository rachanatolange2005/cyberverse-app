# Seed content for CyberVerse's 7 learning modules.
# Each module: theory (HTML-safe string), 5 quiz questions, 6 riddle/term pairs for the memory game.

MODULES = [
    {
        "order": 1,
        "title": "Phishing Awareness",
        "slug": "phishing-awareness",
        "summary": "Spot the bait before you bite.",
        "icon": "fish",
        "theory_html": """
            <p>Phishing is a social-engineering attack where criminals impersonate a trusted entity
            (a bank, a colleague, a delivery company) to trick you into revealing sensitive
            information or installing malware, usually via email, text, or a fake website.</p>
            <h4>Common red flags</h4>
            <ul>
                <li><strong>Urgency and fear:</strong> "Your account will be suspended in 24 hours."</li>
                <li><strong>Mismatched sender domains:</strong> support@paypa1-secure.com instead of paypal.com.</li>
                <li><strong>Generic greetings:</strong> "Dear Customer" instead of your real name.</li>
                <li><strong>Suspicious links:</strong> hover before you click to preview the real URL.</li>
                <li><strong>Unexpected attachments:</strong> invoices or "resumes" you never asked for.</li>
            </ul>
            <h4>Types of phishing</h4>
            <p><strong>Spear phishing</strong> targets a specific person using personal details.
            <strong>Whaling</strong> targets executives. <strong>Smishing</strong> uses SMS text messages.
            <strong>Vishing</strong> uses phone calls.</p>
            <h4>Defence</h4>
            <p>Verify the sender through a separate channel, never enter credentials after clicking
            an email link (type the site address yourself), and enable multi-factor authentication
            so a stolen password alone isn't enough to break in.</p>
        """,
        "quiz": [
            {
                "q": "Which of these is the strongest red flag of a phishing email?",
                "a": "It was sent during work hours",
                "b": "It creates urgency and pressures you to act immediately",
                "c": "It uses a company logo",
                "d": "It is longer than usual",
                "correct": "b",
            },
            {
                "q": "What is 'spear phishing'?",
                "a": "A phishing attack that uses SMS",
                "b": "A random mass phishing email sent to thousands of people",
                "c": "A phishing attack personalized to target one specific individual",
                "d": "A phishing attack made only over the phone",
                "correct": "c",
            },
            {
                "q": "Before clicking a link in a suspicious email, you should:",
                "a": "Click it quickly before it expires",
                "b": "Hover over it to preview the real destination URL",
                "c": "Forward it to a friend to check",
                "d": "Reply asking if it's legitimate",
                "correct": "b",
            },
            {
                "q": "'Vishing' refers to phishing conducted via:",
                "a": "Voice/phone calls",
                "b": "Video messages",
                "c": "Virtual reality apps",
                "d": "Vendor websites",
                "correct": "a",
            },
            {
                "q": "What's the safest way to verify a suspicious request from your 'bank'?",
                "a": "Reply to the email asking for confirmation",
                "b": "Click the link and log in to check",
                "c": "Call the bank using the number on their official website or your card",
                "d": "Ignore it completely and delete it without checking",
                "correct": "c",
            },
        ],
        "riddles": [
            ("Phishing", "Tricking you into giving up info by posing as someone trustworthy"),
            ("Spear Phishing", "A phishing attack aimed at one specific, researched target"),
            ("Smishing", "Phishing delivered through a text message"),
            ("Vishing", "Phishing carried out over a phone call"),
            ("Whaling", "Phishing that targets executives or high-value individuals"),
            ("Spoofed Domain", "A fake web address designed to look like a real one"),
        ],
    },
    {
        "order": 2,
        "title": "Password Security",
        "slug": "password-security",
        "summary": "Your first line of defence.",
        "icon": "key",
        "theory_html": """
            <p>Passwords are still the most common way we authenticate, and the weakest link in
            most breaches. A strong password policy combined with good habits dramatically
            reduces your risk of account takeover.</p>
            <h4>What makes a password strong</h4>
            <ul>
                <li><strong>Length over complexity:</strong> a 16-character passphrase beats an 8-character "P@ssw0rd!".</li>
                <li><strong>Uniqueness:</strong> never reuse a password across multiple sites.</li>
                <li><strong>Unpredictability:</strong> avoid names, birthdays, or dictionary words.</li>
            </ul>
            <h4>Tools that help</h4>
            <p><strong>Password managers</strong> (Bitwarden, 1Password) generate and store unique
            random passwords so you only need to remember one master password.
            <strong>Multi-factor authentication (MFA)</strong> adds a second proof of identity
            (an app code, a hardware key) so a leaked password alone isn't enough.</p>
            <h4>How attackers break passwords</h4>
            <p><strong>Brute force</strong> tries every combination. <strong>Dictionary attacks</strong>
            try common words and known leaked passwords. <strong>Credential stuffing</strong> reuses
            username/password pairs leaked from one breach against other websites — the reason
            password reuse is so dangerous.</p>
            <h4>How sites should store passwords</h4>
            <p>Never in plain text. Passwords should be <strong>hashed</strong> with a slow,
            salted algorithm (bcrypt, Argon2) so that even if a database leaks, the original
            passwords aren't directly exposed.</p>
        """,
        "quiz": [
            {
                "q": "Which password is generally strongest?",
                "a": "Password123",
                "b": "Sunshine!1",
                "c": "correct-horse-battery-staple-42",
                "d": "qwerty",
                "correct": "c",
            },
            {
                "q": "What is 'credential stuffing'?",
                "a": "Saving too many passwords in a browser",
                "b": "Using leaked username/password pairs from one breach to try logging into other sites",
                "c": "A method to strengthen passwords",
                "d": "Typing your password incorrectly multiple times",
                "correct": "b",
            },
            {
                "q": "What should websites use to store passwords securely?",
                "a": "Plain text in the database",
                "b": "Reversible encryption only",
                "c": "A salted hashing algorithm like bcrypt or Argon2",
                "d": "Base64 encoding",
                "correct": "c",
            },
            {
                "q": "What is the main benefit of a password manager?",
                "a": "It makes your internet faster",
                "b": "It generates and securely stores unique passwords for every site",
                "c": "It removes the need for any password at all",
                "d": "It blocks viruses",
                "correct": "b",
            },
            {
                "q": "Why is multi-factor authentication (MFA) important?",
                "a": "It replaces the need for a password entirely",
                "b": "It adds a second proof of identity so a stolen password alone can't grant access",
                "c": "It makes login slower for no benefit",
                "d": "It is only useful for banks",
                "correct": "b",
            },
        ],
        "riddles": [
            ("Hashing", "One-way scrambling of a password so it can't be reversed"),
            ("Salting", "Random data added to a password before hashing it"),
            ("Brute Force", "Trying every possible combination until one works"),
            ("Credential Stuffing", "Reusing leaked login pairs against other sites"),
            ("Password Manager", "A tool that generates and stores unique passwords for you"),
            ("MFA", "A second proof of identity beyond just a password"),
        ],
    },
    {
        "order": 3,
        "title": "Social Engineering",
        "slug": "social-engineering",
        "summary": "Hacking the human, not the machine.",
        "icon": "users",
        "theory_html": """
            <p>Social engineering is the psychological manipulation of people into performing
            actions or divulging confidential information. It exploits trust, fear, curiosity,
            and authority rather than technical vulnerabilities.</p>
            <h4>Common techniques</h4>
            <ul>
                <li><strong>Pretexting:</strong> inventing a fabricated scenario ("I'm from IT support") to gain trust.</li>
                <li><strong>Baiting:</strong> leaving an infected USB drive labeled "Salary Report" for someone to plug in.</li>
                <li><strong>Tailgating:</strong> following an employee through a secure door without a badge.</li>
                <li><strong>Quid pro quo:</strong> offering a fake favor or service in exchange for information.</li>
                <li><strong>Authority impersonation:</strong> posing as a manager or executive to pressure quick compliance.</li>
            </ul>
            <h4>Why it works</h4>
            <p>Humans are wired to trust authority, want to be helpful, and avoid conflict —
            attackers exploit exactly these instincts, often combined with urgency so the
            target doesn't stop to verify.</p>
            <h4>Defence</h4>
            <p>Verify identity through an independent channel, follow procedures even under
            pressure, never let anyone into secure areas without proper badge checks, and
            report suspicious requests instead of quietly going along with them.</p>
        """,
        "quiz": [
            {
                "q": "What is 'pretexting'?",
                "a": "Sending a text message before calling",
                "b": "Creating a fabricated scenario to gain someone's trust",
                "c": "Encrypting a message before sending",
                "d": "A type of malware",
                "correct": "b",
            },
            {
                "q": "An attacker leaves a USB drive labeled 'Confidential Payroll' in a parking lot, hoping someone plugs it in. This is an example of:",
                "a": "Tailgating",
                "b": "Baiting",
                "c": "Phishing",
                "d": "Whaling",
                "correct": "b",
            },
            {
                "q": "'Tailgating' in social engineering refers to:",
                "a": "Following an authorized person through a secure door without credentials",
                "b": "Sending many emails in a row",
                "c": "Driving recklessly to a target's office",
                "d": "Copying someone's writing style",
                "correct": "a",
            },
            {
                "q": "Why are social engineering attacks effective?",
                "a": "They exploit software bugs",
                "b": "They exploit human trust, authority, and urgency rather than technical flaws",
                "c": "They only work on outdated computers",
                "d": "They require expensive hacking tools",
                "correct": "b",
            },
            {
                "q": "What is the best defence against social engineering?",
                "a": "Trusting anyone who sounds confident",
                "b": "Verifying identity through an independent channel before complying",
                "c": "Always complying quickly with authority figures",
                "d": "Disabling all security software",
                "correct": "b",
            },
        ],
        "riddles": [
            ("Pretexting", "Inventing a false scenario to earn someone's trust"),
            ("Baiting", "Luring a victim with a tempting fake item or offer"),
            ("Tailgating", "Sneaking through a secure door behind an authorized person"),
            ("Quid Pro Quo", "Offering a fake favor in exchange for sensitive information"),
            ("Impersonation", "Pretending to be someone in authority to pressure a target"),
            ("Pretext Call", "A phone call built around a fabricated, trust-building story"),
        ],
    },
    {
        "order": 4,
        "title": "Malware",
        "slug": "malware",
        "summary": "Know the enemy code.",
        "icon": "bug",
        "theory_html": """
            <p>Malware (malicious software) is any program designed to damage, disrupt, or gain
            unauthorized access to a system. Understanding the different families helps you
            recognize and respond to infections.</p>
            <h4>Main categories</h4>
            <ul>
                <li><strong>Virus:</strong> attaches itself to a legitimate file and spreads when that file runs.</li>
                <li><strong>Worm:</strong> self-replicates and spreads across networks without needing a host file.</li>
                <li><strong>Trojan:</strong> disguises itself as legitimate software to trick users into installing it.</li>
                <li><strong>Ransomware:</strong> encrypts files and demands payment for the decryption key.</li>
                <li><strong>Spyware:</strong> secretly monitors activity and exfiltrates data (keystrokes, screenshots).</li>
                <li><strong>Rootkit:</strong> hides deep in the OS to maintain persistent, hidden access.</li>
            </ul>
            <h4>Common infection vectors</h4>
            <p>Malicious email attachments, drive-by downloads from compromised websites,
            pirated software, infected USB drives, and exploiting unpatched software
            vulnerabilities.</p>
            <h4>Defence</h4>
            <p>Keep software and OS patched, run reputable antivirus/EDR, avoid downloading
            cracked software, back up data offline (the best defence against ransomware),
            and apply the principle of least privilege so malware can't easily escalate.</p>
        """,
        "quiz": [
            {
                "q": "What distinguishes a worm from a virus?",
                "a": "A worm needs a host file to spread; a virus does not",
                "b": "A worm self-replicates across networks without needing a host file",
                "c": "Worms only infect mobile phones",
                "d": "There is no difference",
                "correct": "b",
            },
            {
                "q": "Ransomware primarily works by:",
                "a": "Stealing your CPU for cryptocurrency mining",
                "b": "Encrypting your files and demanding payment for the decryption key",
                "c": "Slowing down your internet connection",
                "d": "Sending spam from your email account",
                "correct": "b",
            },
            {
                "q": "A Trojan horse malware is characterized by:",
                "a": "Disguising itself as legitimate, desirable software",
                "b": "Self-replicating without user interaction",
                "c": "Only affecting Windows servers",
                "d": "Being harmless once installed",
                "correct": "a",
            },
            {
                "q": "What is the single best defence against ransomware?",
                "a": "A stronger Wi-Fi password",
                "b": "Regular offline backups of important data",
                "c": "Using a louder system alert sound",
                "d": "Disabling your firewall",
                "correct": "b",
            },
            {
                "q": "A rootkit is dangerous primarily because it:",
                "a": "Deletes itself after running once",
                "b": "Hides deep in the operating system to maintain persistent, hidden access",
                "c": "Only works on smartphones",
                "d": "Is easily detected by any antivirus",
                "correct": "b",
            },
        ],
        "riddles": [
            ("Virus", "Malware that attaches to a file and spreads when that file runs"),
            ("Worm", "Self-replicating malware that spreads across a network on its own"),
            ("Trojan", "Malware disguised as legitimate, desirable software"),
            ("Ransomware", "Malware that encrypts files and demands payment to unlock them"),
            ("Spyware", "Malware that secretly monitors and steals your activity"),
            ("Rootkit", "Malware that hides deep in the OS for persistent hidden access"),
        ],
    },
    {
        "order": 5,
        "title": "Safe Internet Browsing",
        "slug": "safe-browsing",
        "summary": "Walk the web without stepping on a landmine.",
        "icon": "globe",
        "theory_html": """
            <p>Most everyday risk comes from browsing itself: malicious ads, fake download
            buttons, insecure connections, and browser extensions with excessive permissions.</p>
            <h4>Key habits</h4>
            <ul>
                <li><strong>Check for HTTPS:</strong> the padlock icon means traffic is encrypted in transit —
                it does not mean the site is trustworthy, just that it can't easily be eavesdropped on.</li>
                <li><strong>Avoid public Wi-Fi for sensitive logins</strong>, or use a VPN if you must.</li>
                <li><strong>Be skeptical of "free" downloads</strong> like cracked software, which are common malware vectors.</li>
                <li><strong>Keep your browser and extensions updated</strong> to patch known vulnerabilities.</li>
                <li><strong>Review extension permissions</strong> — an extension that reads "all data on all websites" is a major risk.</li>
            </ul>
            <h4>Recognizing malicious sites</h4>
            <p>Watch for misspelled domains (amaz0n.com), pop-ups claiming your device is
            infected ("scareware"), and pages demanding you disable your antivirus to continue.</p>
            <h4>Browser security features</h4>
            <p>Modern browsers include Safe Browsing warnings, sandboxing (isolating tabs from
            the OS), and certificate validation. Never click through a certificate warning on
            a site asking for sensitive data.</p>
        """,
        "quiz": [
            {
                "q": "What does the padlock/HTTPS icon in a browser guarantee?",
                "a": "The site is completely trustworthy",
                "b": "The connection between you and the site is encrypted in transit",
                "c": "The site has no malware",
                "d": "The site is owned by a verified company",
                "correct": "b",
            },
            {
                "q": "Why is public Wi-Fi risky for sensitive logins?",
                "a": "It's usually slower than home internet",
                "b": "Traffic can potentially be intercepted by others on the same network",
                "c": "Public Wi-Fi always requires a password",
                "d": "It costs more data",
                "correct": "b",
            },
            {
                "q": "A pop-up claims 'Your device is infected, call this number now!' This is most likely:",
                "a": "A legitimate antivirus alert",
                "b": "Scareware designed to scare you into calling a scam number or installing malware",
                "c": "A normal browser update notice",
                "d": "A Wi-Fi router warning",
                "correct": "b",
            },
            {
                "q": "What should you check before installing a browser extension?",
                "a": "Its file size",
                "b": "Its requested permissions and what data it can access",
                "c": "How many colors it uses",
                "d": "Whether it's free",
                "correct": "b",
            },
            {
                "q": "If your browser shows a certificate warning on a site asking for your password, you should:",
                "a": "Click through and proceed anyway",
                "b": "Avoid entering sensitive data and leave the site",
                "c": "Disable your antivirus to fix it",
                "d": "Ignore it if the site looks nice",
                "correct": "b",
            },
        ],
        "riddles": [
            ("HTTPS", "Encrypts traffic between your browser and a website"),
            ("Scareware", "Fake alerts designed to panic you into calling or installing malware"),
            ("Typosquatting", "A fake domain that relies on a common misspelling of a real one"),
            ("VPN", "Encrypts your traffic, useful protection on public Wi-Fi"),
            ("Sandboxing", "Isolating a browser tab so it can't affect the rest of your system"),
            ("Certificate Warning", "A browser alert that a site's identity can't be verified"),
        ],
    },
    {
        "order": 6,
        "title": "Email Security",
        "slug": "email-security",
        "summary": "Your inbox is a battlefield.",
        "icon": "mail",
        "theory_html": """
            <p>Email remains the number one delivery channel for attacks, from phishing to
            malware to business email compromise. Securing it requires both technical
            controls and personal vigilance.</p>
            <h4>Technical protections</h4>
            <ul>
                <li><strong>SPF (Sender Policy Framework):</strong> specifies which servers may send mail for a domain.</li>
                <li><strong>DKIM (DomainKeys Identified Mail):</strong> cryptographically signs outgoing mail to prove it wasn't tampered with.</li>
                <li><strong>DMARC:</strong> tells receiving servers what to do when SPF/DKIM checks fail (reject, quarantine, or allow).</li>
                <li><strong>Encryption (TLS/S-MIME):</strong> protects message content in transit and, with S-MIME, end-to-end.</li>
            </ul>
            <h4>Business Email Compromise (BEC)</h4>
            <p>Attackers compromise or spoof an executive's email and instruct finance staff to
            make urgent wire transfers. These attacks rely entirely on social engineering and
            urgency, often with no malware involved at all.</p>
            <h4>Personal habits</h4>
            <p>Never enable macros in attachments from unknown senders, verify unusual payment
            requests by phone, check the full sender address (not just the display name), and
            use a separate email for sensitive accounts versus everyday sign-ups.</p>
        """,
        "quiz": [
            {
                "q": "What does SPF (Sender Policy Framework) do?",
                "a": "Encrypts the body of an email",
                "b": "Specifies which mail servers are authorized to send email for a domain",
                "c": "Blocks all attachments automatically",
                "d": "Scans for grammar errors",
                "correct": "b",
            },
            {
                "q": "DKIM helps verify that an email:",
                "a": "Was not tampered with in transit, using a cryptographic signature",
                "b": "Was sent from a mobile device",
                "c": "Has no spelling mistakes",
                "d": "Was opened by the recipient",
                "correct": "a",
            },
            {
                "q": "What is Business Email Compromise (BEC)?",
                "a": "A virus that deletes business emails",
                "b": "An attack where a compromised/spoofed executive email is used to trick staff into urgent transfers",
                "c": "A spam filter malfunction",
                "d": "A type of email encryption standard",
                "correct": "b",
            },
            {
                "q": "Why should you check the full sender address, not just the display name?",
                "a": "Display names can be easily faked while the actual address reveals the true sender",
                "b": "It makes the email load faster",
                "c": "It's required by law",
                "d": "It changes the email's font",
                "correct": "a",
            },
            {
                "q": "What should you do with macro-enabled attachments from unknown senders?",
                "a": "Always enable macros to view content properly",
                "b": "Avoid enabling macros, as they're a common malware delivery method",
                "c": "Forward them to colleagues first",
                "d": "Print them before opening",
                "correct": "b",
            },
        ],
        "riddles": [
            ("SPF", "Defines which servers are allowed to send mail for a domain"),
            ("DKIM", "A cryptographic signature proving an email wasn't tampered with"),
            ("DMARC", "Tells receiving servers what to do when SPF/DKIM checks fail"),
            ("BEC", "A scam using a spoofed executive email to request urgent transfers"),
            ("Spoofed Sender", "A display name faked to look like someone you trust"),
            ("Macro Malware", "Malicious code hidden inside a document's macro feature"),
        ],
    },
    {
        "order": 7,
        "title": "Cyber Hygiene",
        "slug": "cyber-hygiene",
        "summary": "Daily habits that keep you secure.",
        "icon": "shield-check",
        "theory_html": """
            <p>Cyber hygiene is the set of routine practices that keep your devices, accounts,
            and data healthy over time, the digital equivalent of washing your hands.
            Most breaches exploit basic neglect, not sophisticated zero-day exploits.</p>
            <h4>Core habits</h4>
            <ul>
                <li><strong>Patch promptly:</strong> apply OS and app updates as soon as they're available.</li>
                <li><strong>Back up regularly:</strong> follow the 3-2-1 rule — 3 copies, 2 different media, 1 offsite.</li>
                <li><strong>Use unique passwords + MFA</strong> on every account, especially email (the master key to password resets).</li>
                <li><strong>Review account permissions:</strong> periodically audit connected apps and revoke ones you no longer use.</li>
                <li><strong>Lock your devices</strong> with a PIN/biometric and enable auto-lock.</li>
                <li><strong>Minimize your data footprint:</strong> don't overshare personal details that fuel social engineering.</li>
            </ul>
            <h4>Putting it together</h4>
            <p>None of these habits are individually complex, but consistency is what matters.
            A single unpatched device or reused password can undo every other precaution you take.
            Think of cyber hygiene as a continuous practice, not a one-time setup.</p>
            <h4>You've completed CyberVerse!</h4>
            <p>You now understand phishing, password security, social engineering, malware,
            safe browsing, email security, and cyber hygiene — the seven pillars of personal
            cybersecurity awareness.</p>
        """,
        "quiz": [
            {
                "q": "What is the 3-2-1 backup rule?",
                "a": "3 passwords, 2 emails, 1 phone number",
                "b": "3 copies of data, on 2 different media, with 1 copy stored offsite",
                "c": "Back up every 3 hours for 2 minutes, 1 time per day",
                "d": "3 devices, 2 networks, 1 firewall",
                "correct": "b",
            },
            {
                "q": "Why is your email account considered especially critical to secure?",
                "a": "It uses the most storage space",
                "b": "It's typically the master key used to reset passwords for your other accounts",
                "c": "It's the only account that can be hacked",
                "d": "It has no security features available",
                "correct": "b",
            },
            {
                "q": "What does 'patching promptly' mean?",
                "a": "Buying new hardware every year",
                "b": "Applying software/OS updates as soon as they're available to fix known vulnerabilities",
                "c": "Repairing physical cables",
                "d": "Changing your password every update",
                "correct": "b",
            },
            {
                "q": "Why should you periodically review connected app permissions on your accounts?",
                "a": "To free up storage space",
                "b": "To revoke access for apps you no longer use, reducing your attack surface",
                "c": "It improves your internet speed",
                "d": "It's not actually necessary",
                "correct": "b",
            },
            {
                "q": "What best describes 'cyber hygiene'?",
                "a": "A one-time security setup you never need to repeat",
                "b": "A continuous set of routine habits that keep your accounts and devices secure",
                "c": "Software that automatically protects you with zero effort",
                "d": "A type of antivirus brand",
                "correct": "b",
            },
        ],
        "riddles": [
            ("3-2-1 Rule", "3 copies of data, 2 media types, 1 stored offsite"),
            ("Patching", "Applying updates promptly to fix known vulnerabilities"),
            ("Attack Surface", "The total number of points an attacker could exploit"),
            ("Auto-Lock", "A setting that locks your device after inactivity"),
            ("Permission Audit", "Reviewing which apps can access your account and data"),
            ("Digital Footprint", "The trail of personal data you leave across the internet"),
        ],
    },
]
