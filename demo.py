"""
==============================================================================
💎 KRONOS CUSTOM EMOJI SYSTEM — INTERACTIVE SHOWCASE & DEMO
👑 Architect: Aryan (@thatonearyan)
==============================================================================
This script demonstrates:
  1. Rendering animated custom emojis in text messages via <tg-emoji>
  2. Automatic upgrade of plain emojis to custom stickers via premiumize_text()
  3. Building interactive Inline Buttons with animated custom icons (icon_custom_emoji_id)
  4. Setting button colors, styles, and visual palettes
  5. Sending live interactive messages to Telegram

Usage:
  python3 demo.py
==============================================================================
"""

import asyncio
import os
import sys
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Import the master toolkit
from custom_emojis import (
    custom_tag,
    premiumize_text,
    get_custom_emoji_id,
    styled_btn,
    calendar_day_tag,
    calendar_weekday_tag,
    calendar_month_tag,
    school_number_tag,
    divider_tag,
    EMOJI_ICONS,
    CALENDAR_WEEKDAYS,
    CALENDAR_MONTHS
)


def local_demo():
    print("=" * 70)
    print("💎 KRONOS CUSTOM EMOJI TOOLKIT — LOCAL DEMO")
    print("=" * 70)

    # 1. Generating single tags
    print("\n--- 1. SINGLE CUSTOM EMOJI TAGS ---")
    trophy_tag = custom_tag("VIOLET_TROPHY")
    diamond_tag = custom_tag("VIOLET_DIAMOND")
    heart_tag = custom_tag("TBOI_SACRED_HEART")
    dice_tag = custom_tag("TBOI_RED_D6_DIE")
    print(f"Trophy Tag : {trophy_tag}")
    print(f"Diamond Tag: {diamond_tag}")
    print(f"Heart Tag  : {heart_tag}")
    print(f"Dice Tag   : {dice_tag}")

    # 2. Automated Text Upgrade (premiumize_text)
    print("\n--- 2. AUTOMATIC TEXT UPGRADE (premiumize_text) ---")
    raw_message = "Welcome to Kronos Casino! 🎰 Roll the dice 🎲 and win 💎 diamonds! 🚀"
    upgraded = premiumize_text(raw_message)
    print("Raw Input      :", raw_message)
    print("Upgraded Output:", upgraded)

    # 3. Calendar Engine
    print("\n--- 3. DYNAMIC CALENDAR ENGINE ---")
    print("Today: ", calendar_weekday_tag("MON") + " " + calendar_day_tag(12) + " " + calendar_month_tag("SEP"))

    # 4. School 3D Digit Engine
    print("\n--- 4. 3D SCHOOL NUMBERS ---")
    print("Score: ", school_number_tag("2026"))

    # 5. Inline Keyboard Button with Custom Icon
    print("\n--- 5. INLINE BUTTONS WITH CUSTOM ICONS ---")
    btn1 = styled_btn("Claim Daily Bonus", callback_data="claim_bonus", icon="VIOLET_TROPHY", style="success")
    btn2 = styled_btn("High Roller Casino", callback_data="play_casino", icon="TBOI_RED_D6_DIE", style="primary")
    btn3 = styled_btn("VIP Support", url="https://t.me/thatonearyan", icon="EDU_STAR")
    
    print("Button 1 dict:", btn1.model_dump(exclude_none=True))
    print("Button 2 dict:", btn2.model_dump(exclude_none=True))
    print("Button 3 dict:", btn3.model_dump(exclude_none=True))
    print("\n✅ Local demonstration complete!")


async def telegram_live_demo():
    """
    Sends an interactive demo message to the Admin ID if .env credentials exist.
    """
    env_path = ".env"
    if not os.path.exists(env_path):
        print("Note: .env file not found. Skipping live Telegram dispatch.")
        return

    env = {}
    with open(env_path) as f:
        for line in f:
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.strip().split("=", 1)
                env[k] = v

    token = env.get("BOT_TOKEN")
    admins = env.get("ADMINS", "")
    if not token or not admins:
        return

    admin_id = int(admins.split(",")[0])
    bot = Bot(token=token)

    # Build demo message
    t_trophy = custom_tag("VIOLET_TROPHY")
    t_dice = custom_tag("TBOI_RED_D6_DIE")
    t_heart = custom_tag("TBOI_SACRED_HEART")
    t_div = divider_tag(0)

    html_message = (
        f"{t_trophy} <b>KRONOS CUSTOM EMOJI SHOWCASE</b> {t_trophy}\n"
        f"{t_div}\n\n"
        f"👑 <b>Lead Architect:</b> Aryan (<code>@thatonearyan</code>)\n"
        f"💎 <b>Active Inventory:</b> 1,316 High-Definition Emojis\n"
        f"🎨 <b>Total Named Icons:</b> 1,471 Tokens\n\n"
        f"<b>Featured Live Integrations:</b>\n"
        f"• {t_dice} <b>Casino D6 Gaming Dice:</b> Active in Kronos Casino\n"
        f"• {t_heart} <b>Sacred Heart:</b> Red alert & VIP health icon\n"
        f"• {custom_tag('EDU_LAPTOP')} <b>White Education Laptop:</b> Item #185\n"
        f"• {custom_tag('EDU_STAR')} <b>5-Point Star:</b> Item #186\n"
        f"• {custom_tag('CALENDAR_MON')} <b>Monday Calendar Flip:</b> Item #33\n\n"
        f"👇 <i>Check the styled buttons below with animated icons:</i>"
    )

    # Build keyboard with animated icon_custom_emoji_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            styled_btn(
                text="Play Casino Games",
                callback_data="demo_play",
                icon="TBOI_RED_D6_DIE",
                style="primary"
            ),
            styled_btn(
                text="Daily Reward",
                callback_data="demo_reward",
                icon="VIOLET_TROPHY",
                style="success"
            )
        ],
        [
            styled_btn(
                text="Danger Zone",
                callback_data="demo_danger",
                icon="TBOI_SACRED_HEART",
                style="danger"
            )
        ],
        [
            styled_btn(
                text="Contact Architect",
                url="https://t.me/thatonearyan",
                icon="EDU_STAR"
            )
        ]
    ])

    try:
        msg = await bot.send_message(
            chat_id=admin_id,
            text=html_message,
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML
        )
        print(f"🚀 Live Telegram showcase dispatched to Admin {admin_id}! (Message ID: {msg.message_id})")
    except Exception as e:
        print(f"Error sending live demo: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    local_demo()
    # If called with --live, send to Telegram
    if "--live" in sys.argv:
        asyncio.run(telegram_live_demo())
