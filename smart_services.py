import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# إعداد السجلات لمتابعة عمل البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"أهلاً بك يا {user_name} في بوت الخدمات الذكية!\n"
        "البوت يعمل الآن بنجاح ومستعد لخدمتك."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "الأوامر المتاحة:\n"
        "/start - بدء البوت\n"
        "/help - عرض المساعدة"
    )

def main():
    # ضع توكن البوت الخاص بك هنا بين علامتي التنصيص
    TOKEN = "YOUR_BOT_TOKEN_HERE"
    
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    print("البوت يعمل الآن...")
    application.run_polling()

if __name__ == '__main__':
    main()
