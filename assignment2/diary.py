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
   exception_name = type(e).__name__
   print(f'An exception occurred. {exception_name}')
      
        


