import pyautogui
import time
import pyperclip
import google.generativeai as palm  # <-- Google PaLM

# Initialize PaLM with your Google API key
palm.configure(api_key="<Your_api_key>")

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    messages = chat_log.strip().split("\n")
    for message in reversed(messages):
        if sender_name in message:
            return True
        elif "]" in message:
            return False
    return False

# Step 1: Click Chrome icon
pyautogui.click(1177, 1061)
time.sleep(1)

while True:
    time.sleep(5)

    # Step 2: Select chat text
    pyautogui.moveTo(740,2555)
    pyautogui.dragTo(745,9035, duration=2.0, button='left')

    # Step 3: Copy
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1994, 281)

    # Step 4: Read from clipboard
    chat_history = pyperclip.paste()
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        # Step 5: Generate a response using Google's PaLM
        prompt = f"""You are a person named <name> who speaks Hindi and English. You are from India and a coder. 
        Analyze the chat and roast people in a funny way. Respond only with the roast (no names/timestamps).
        Chat log:
        {chat_history}
        """

        response = palm.generate_text(
            model="models/text-bison-001",  # Or "gemini-pro" if using Gemini
            prompt=prompt,
            temperature=0.7,
            max_output_tokens=100,
        )

        if response.result:
            roast = response.result.strip()
            pyperclip.copy(roast)

            # Step 6: Paste & send
            pyautogui.click(1063,9622)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')
