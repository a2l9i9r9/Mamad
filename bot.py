from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import re
import os

TOKEN = os.getenv(8399356480:AAFShivOk9pi2iv1N-7FbKSJoVoKK6jgqh0)

BAD_PATTERNS = [
    r"فردین\s*پور",
    r"فردینپور",
    r"فردین"
]

REPLY_TEXT = "خودت روش کراش داری روت نمیشه منو میندازی وسط"

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg or not msg.text:
        return

    # فقط پیام‌های داخل discussion group (کامنت کانال)
    if not msg.is_automatic_forward and not msg.sender_chat:
        pass

    for p in BAD_PATTERNS:
        if re.search(p, msg.text):

            user = msg.from_user
            mention = user.mention_html()

            try:
                await msg.delete()
            except:
                pass

            # 👇 این بخش کلید اصلی threaded comment هست
            await context.bot.send_message(
                chat_id=msg.chat.id,
                text=f"{REPLY_TEXT}\n👤 {mention}",
                parse_mode="HTML",
                reply_to_message_id=msg.message_id
            )

            break

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler))

app.run_polling()
