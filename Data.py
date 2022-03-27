from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to generate pyrogram and telethon string session. Use the below buttons to know more!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" Generating Session ", callback_data="generate")],
        [InlineKeyboardButton(text=" Back ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Generating Session 🔥", callback_data="generate")]
    ]

    support_button = [
        [InlineKeyboardButton("🖕 Support 🖕", url="https://t.me/Baapjiiiiiiiiii")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("👨‍💻 Repo subscribe 🔥 and come to get repo ❣️ 👨‍💻", url="https://youtube.com/channel/UCE5jPA5zAKw37gM7tptdJew")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton(" About", callback_data="about")
        ],
        [InlineKeyboardButton("🇮🇳 Owner 🇮🇳", url="t.me/legit_adder_01")],
    ]

    # Help Message
    HELP = """
» Click the below button or use /generate command to start generating session!
» Click the required button; [Pyrogram/Telethon]
» Enter the required variables when asked.
"""

    # About Message
    ABOUT = """
👨‍💻 **About Me** 

A telegram bot to generate pyrogram and telethon string session...

[Pyrogram](docs.pyrogram.org)
[Telethon](docs.telethon.org)

Language : [Python](www.python.org)
            **Regarding ~ **@legit_adder_01
"""
