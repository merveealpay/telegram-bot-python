from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "selam", "slm", "merhaba"):
        return "Hello, selam!"

    if user_message in ("who are you?", "kimsin", "kim", "kimsin?"):
        return "Merve's Bot"

    if user_message in ("time", "time?", "zaman?", "zaman", "saat", "tarih", "tarih?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Seni anlamadim."