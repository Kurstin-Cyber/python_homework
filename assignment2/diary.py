import traceback



try:
    with open('diary.txt', 'a') as file:
       prompt = 'What happened today? '
       while True:
           line = input(prompt)
           file.write(line + "\n")

           if line == "done for now":
              break
           
           prompt = "What else? "

except Exception as e:
  print('An exception occurred.')
  print(type(e).__name__)
  trace_back = traceback.extract_tb(e.__traceback__)
        


