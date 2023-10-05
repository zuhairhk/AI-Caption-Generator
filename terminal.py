import mp4totxt
import ai_gen

video = "video4.mp4"
generated_caption = ""
sys_instruct = "You are a social media platform's caption generator. I will give you text, you must reply with a related and relevant caption to be used from the transcribed video text. Use of a few emojis is encouraged."

input_text = mp4totxt.main(video)
while(True):
    generated_caption = ai_gen.generate_caption(input_text, sys_instruct)
    print('Generated Caption: ', generated_caption)
    sys_instruct = input('\nEnter prompt to edit or `1` to break: ')

    if sys_instruct == '1':
        break

print(f'\n******************************\nFinal caption: {generated_caption}\n******************************')